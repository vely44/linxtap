"""Network utility functions"""
import socket


def get_local_ip() -> str:
    """
    Get the local network IP address of this device.
    Returns the local IP address or 'Unknown' if it cannot be determined.
    """
    try:
        # Create a socket connection to determine local IP
        # This doesn't actually send data, just determines routing
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Connect to a public DNS server (doesn't need to be reachable)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        # Fallback method: get hostname IP
        try:
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            # Filter out localhost
            if local_ip.startswith('127.'):
                return 'Unknown'
            return local_ip
        except Exception:
            return 'Unknown'


def get_hostname() -> str:
    """
    Get the hostname of this device.
    Returns the hostname or 'Unknown' if it cannot be determined.
    """
    try:
        return socket.gethostname()
    except Exception:
        return 'Unknown'
