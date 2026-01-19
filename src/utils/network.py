"""Network utility functions"""
import socket
import subprocess
import re
from typing import Optional


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


def get_default_gateway() -> Optional[str]:
    """
    Get the default gateway IP address.
    Returns the gateway IP or None if it cannot be determined.
    """
    try:
        # Try using ip route command
        result = subprocess.run(['ip', 'route'],
                              capture_output=True,
                              text=True,
                              timeout=2)
        if result.returncode == 0:
            # Look for default route
            for line in result.stdout.split('\n'):
                if line.startswith('default'):
                    # Extract gateway IP
                    parts = line.split()
                    if len(parts) >= 3 and parts[1] == 'via':
                        return parts[2]
    except Exception:
        pass

    # Fallback: try reading /proc/net/route
    try:
        with open('/proc/net/route', 'r') as f:
            lines = f.readlines()
            for line in lines[1:]:  # Skip header
                parts = line.split()
                if parts[1] == '00000000':  # Default route
                    # Gateway is in hex, reversed byte order
                    gateway_hex = parts[2]
                    # Convert hex to IP
                    gateway_ip = '.'.join([
                        str(int(gateway_hex[i:i+2], 16))
                        for i in range(6, -1, -2)
                    ])
                    return gateway_ip
    except Exception:
        pass

    return None


def detect_os_from_ttl(ttl: int) -> str:
    """
    Attempt to detect OS based on TTL value.
    Different operating systems use different default TTL values.

    Returns a best-guess OS name or 'Unknown'.
    """
    # Common default TTL values
    if ttl <= 64:
        if ttl > 32:
            return 'Linux/Unix'
        else:
            return 'Unknown'
    elif ttl <= 128:
        return 'Windows'
    elif ttl <= 255:
        return 'Cisco/Network Device'
    else:
        return 'Unknown'


def get_remote_ttl(ip: str, port: int, timeout: float = 2.0) -> Optional[int]:
    """
    Get the TTL value from a remote host by analyzing socket options.
    Returns TTL value or None if it cannot be determined.
    """
    try:
        # Create a socket and connect
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((ip, port))

        # Try to get TTL from socket options
        # This may not work on all systems
        try:
            ttl = sock.getsockopt(socket.IPPROTO_IP, socket.IP_TTL)
            sock.close()
            return ttl
        except:
            sock.close()

        # Alternative: use ping to get TTL
        result = subprocess.run(['ping', '-c', '1', '-W', '1', ip],
                              capture_output=True,
                              text=True,
                              timeout=3)
        if result.returncode == 0:
            # Parse TTL from ping output
            match = re.search(r'ttl=(\d+)', result.stdout.lower())
            if match:
                return int(match.group(1))
    except Exception:
        pass

    return None


def is_gateway(ip: str) -> bool:
    """
    Check if the given IP address is the default gateway.
    Returns True if it's the gateway, False otherwise.
    """
    gateway = get_default_gateway()
    if gateway is None:
        return False
    return ip == gateway
