import socket
from src.utils.network import get_remote_ttl, detect_os_from_ttl, is_gateway


class AppLogic:
    def __init__(self):
        self.connected = False
        self.socket = None
        self.current_ip = None
        self.current_port = None
        self.remote_os = None
        self.is_gateway_device = False

    def connect(self, ip: str, port: str) -> dict:
        """
        Attempt to connect to the specified IP and port.
        Returns a dict with 'status' and 'message' keys.
        """
        # If already connected, disconnect
        if self.connected:
            return self._disconnect()

        # Validate inputs
        if not ip or not port:
            return {
                'status': 'error',
                'message': 'Error: IP address and port are required'
            }

        # Validate port is a number
        try:
            port_num = int(port)
            if port_num < 1 or port_num > 65535:
                return {
                    'status': 'error',
                    'message': 'Error: Port must be between 1 and 65535'
                }
        except ValueError:
            return {
                'status': 'error',
                'message': 'Error: Port must be a valid number'
            }

        # Attempt connection
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(5)  # 5 second timeout
            self.socket.connect((ip, port_num))

            self.connected = True
            self.current_ip = ip
            self.current_port = port_num

            # Detect remote device information
            self.is_gateway_device = is_gateway(ip)

            # Try to detect OS via TTL
            ttl = get_remote_ttl(ip, port_num, timeout=2.0)
            if ttl:
                self.remote_os = detect_os_from_ttl(ttl)
            else:
                self.remote_os = 'Unknown'

            return {
                'status': 'connected',
                'message': f'Connected to {ip}:{port_num}',
                'remote_os': self.remote_os,
                'is_gateway': self.is_gateway_device
            }
        except socket.timeout:
            self._cleanup_socket()
            return {
                'status': 'error',
                'message': f'Error: Connection timeout to {ip}:{port_num}'
            }
        except socket.gaierror:
            self._cleanup_socket()
            return {
                'status': 'error',
                'message': f'Error: Invalid IP address {ip}'
            }
        except ConnectionRefusedError:
            self._cleanup_socket()
            return {
                'status': 'error',
                'message': f'Error: Connection refused by {ip}:{port_num}'
            }
        except OSError as e:
            self._cleanup_socket()
            return {
                'status': 'error',
                'message': f'Error: {str(e)}'
            }
        except Exception as e:
            self._cleanup_socket()
            return {
                'status': 'error',
                'message': f'Error: Unexpected error - {str(e)}'
            }

    def _disconnect(self) -> dict:
        """Disconnect from current connection"""
        self._cleanup_socket()
        self.connected = False

        old_connection = f"{self.current_ip}:{self.current_port}" if self.current_ip else "server"
        self.current_ip = None
        self.current_port = None
        self.remote_os = None
        self.is_gateway_device = False

        return {
            'status': 'disconnected',
            'message': f'Disconnected from {old_connection}'
        }

    def _cleanup_socket(self):
        """Clean up socket connection"""
        if self.socket:
            try:
                self.socket.close()
            except:
                pass
            self.socket = None

    def send_message(self, message: str) -> dict:
        """
        Send a message via TCP to the connected device.
        Returns a dict with 'status', 'message', and optionally 'response' keys.
        """
        if not self.connected or not self.socket:
            return {
                'status': 'error',
                'message': 'Not connected to any device'
            }

        if not message:
            return {
                'status': 'error',
                'message': 'Message cannot be empty'
            }

        try:
            # Encode and send the message
            message_bytes = message.encode('utf-8')
            self.socket.sendall(message_bytes)

            # Try to receive a response (with short timeout)
            self.socket.settimeout(1.0)
            try:
                response = self.socket.recv(4096)
                if response:
                    response_text = response.decode('utf-8', errors='replace')
                    return {
                        'status': 'success',
                        'message': f'Sent {len(message_bytes)} bytes',
                        'bytes_sent': len(message_bytes),
                        'response': response_text
                    }
                else:
                    return {
                        'status': 'success',
                        'message': f'Sent {len(message_bytes)} bytes (no response)',
                        'bytes_sent': len(message_bytes)
                    }
            except socket.timeout:
                # No response received, but message was sent
                return {
                    'status': 'success',
                    'message': f'Sent {len(message_bytes)} bytes (no response)',
                    'bytes_sent': len(message_bytes)
                }

        except BrokenPipeError:
            self._cleanup_socket()
            self.connected = False
            return {
                'status': 'error',
                'message': 'Connection broken - device disconnected'
            }
        except ConnectionResetError:
            self._cleanup_socket()
            self.connected = False
            return {
                'status': 'error',
                'message': 'Connection reset by remote device'
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': f'Failed to send: {str(e)}'
            }
        finally:
            # Restore original timeout
            if self.socket:
                try:
                    self.socket.settimeout(5.0)
                except:
                    pass

    def __del__(self):
        """Cleanup when object is destroyed"""
        self._cleanup_socket()
