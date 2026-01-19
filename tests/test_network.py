from src.utils.network import (get_local_ip, get_hostname, get_default_gateway,
                              detect_os_from_ttl, is_gateway)


def test_get_local_ip_returns_string():
    """Test that get_local_ip returns a string"""
    ip = get_local_ip()
    assert isinstance(ip, str)
    assert len(ip) > 0


def test_get_local_ip_format():
    """Test that get_local_ip returns a valid format"""
    ip = get_local_ip()

    # Should either be 'Unknown' or a valid IP format
    if ip != 'Unknown':
        parts = ip.split('.')
        # Valid IP has 4 parts
        assert len(parts) == 4
        # Each part should be a number between 0-255
        for part in parts:
            num = int(part)
            assert 0 <= num <= 255


def test_get_hostname_returns_string():
    """Test that get_hostname returns a string"""
    hostname = get_hostname()
    assert isinstance(hostname, str)
    assert len(hostname) > 0


def test_get_hostname_not_empty():
    """Test that get_hostname returns something meaningful"""
    hostname = get_hostname()
    # Should not be empty or just whitespace
    assert hostname.strip() != ''


def test_get_default_gateway():
    """Test that get_default_gateway returns None or a valid IP"""
    gateway = get_default_gateway()

    if gateway is not None:
        assert isinstance(gateway, str)
        parts = gateway.split('.')
        assert len(parts) == 4
        for part in parts:
            num = int(part)
            assert 0 <= num <= 255


def test_detect_os_from_ttl():
    """Test OS detection from TTL values"""
    # Test common TTL values
    assert detect_os_from_ttl(64) == 'Linux/Unix'
    assert detect_os_from_ttl(128) == 'Windows'
    assert detect_os_from_ttl(255) == 'Cisco/Network Device'
    assert detect_os_from_ttl(32) == 'Unknown'


def test_is_gateway():
    """Test gateway detection"""
    # Test with obviously non-gateway IP
    assert is_gateway('0.0.0.0') is False

    # Test with localhost
    assert is_gateway('127.0.0.1') is False
