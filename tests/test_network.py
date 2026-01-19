from src.utils.network import get_local_ip, get_hostname


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
