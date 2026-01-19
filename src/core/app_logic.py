import socket


class AppLogic:
    def __init__(self):
        self.connected = False
        self.socket = None
        self.current_ip = None
        self.current_port = None

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

            return {
                'status': 'connected',
                'message': f'Connected to {ip}:{port_num}'
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

    def __del__(self):
        """Cleanup when object is destroyed"""
        self._cleanup_socket()
