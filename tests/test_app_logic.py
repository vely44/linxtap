from src.core.app_logic import AppLogic


def test_initial_state():
    """Test that AppLogic initializes in disconnected state"""
    logic = AppLogic()
    assert logic.connected is False
    assert logic.socket is None
    assert logic.current_ip is None
    assert logic.current_port is None
    assert logic.remote_os is None
    assert logic.is_gateway_device is False


def test_connect_empty_inputs():
    """Test connection with empty IP and port"""
    logic = AppLogic()
    result = logic.connect("", "")
    assert result['status'] == 'error'
    assert 'required' in result['message'].lower()


def test_connect_invalid_port():
    """Test connection with invalid port number"""
    logic = AppLogic()

    # Non-numeric port
    result = logic.connect("127.0.0.1", "abc")
    assert result['status'] == 'error'
    assert 'valid number' in result['message'].lower()

    # Port out of range
    result = logic.connect("127.0.0.1", "99999")
    assert result['status'] == 'error'
    assert 'between 1 and 65535' in result['message'].lower()


def test_connect_refused():
    """Test connection to non-existent server"""
    logic = AppLogic()
    # Using a port that's unlikely to be open
    result = logic.connect("127.0.0.1", "54321")

    # Should get either connection refused or timeout
    assert result['status'] == 'error'
    assert 'refused' in result['message'].lower() or 'timeout' in result['message'].lower()


def test_connect_invalid_ip():
    """Test connection with invalid IP address"""
    logic = AppLogic()
    result = logic.connect("invalid.ip.address", "8080")
    assert result['status'] == 'error'


def test_disconnect_logic():
    """Test that attempting to connect when already 'connected' triggers disconnect"""
    logic = AppLogic()

    # Simulate a connected state
    logic.connected = True
    logic.current_ip = "127.0.0.1"
    logic.current_port = 8080

    result = logic.connect("192.168.1.1", "9090")

    assert result['status'] == 'disconnected'
    assert 'disconnected' in result['message'].lower()
