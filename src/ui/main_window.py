from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QPushButton, QLineEdit, QGroupBox, QFrame, QTextEdit)
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QFont
from src.core.app_logic import AppLogic
from src.utils.network import get_local_ip, get_hostname
from datetime import datetime


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.logic = AppLogic()
        self._setup_ui()

    def _setup_ui(self):
        self.setWindowTitle("LinxTap")
        self.setMinimumSize(500, 650)

        # Central widget
        central = QWidget()
        self.setCentralWidget(central)

        # Main layout
        layout = QVBoxLayout(central)
        layout.setAlignment(Qt.AlignTop)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        # Title label
        title = QLabel("LinxTap")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        # Connection settings group
        connection_group = QGroupBox("Connection Settings")
        connection_layout = QVBoxLayout()

        # IP address input
        ip_layout = QHBoxLayout()
        ip_label = QLabel("IP Address:")
        ip_label.setMinimumWidth(80)
        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("e.g., 192.168.1.100")
        self.ip_input.setText("127.0.0.1")
        ip_layout.addWidget(ip_label)
        ip_layout.addWidget(self.ip_input)
        connection_layout.addLayout(ip_layout)

        # Port input
        port_layout = QHBoxLayout()
        port_label = QLabel("Port:")
        port_label.setMinimumWidth(80)
        self.port_input = QLineEdit()
        self.port_input.setPlaceholderText("e.g., 8080")
        self.port_input.setText("8080")
        port_layout.addWidget(port_label)
        port_layout.addWidget(self.port_input)
        connection_layout.addLayout(port_layout)

        connection_group.setLayout(connection_layout)
        layout.addWidget(connection_group)

        # Status label
        self.status_label = QLabel("Not connected")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("padding: 10px; background-color: #f0f0f0; border-radius: 5px;")
        layout.addWidget(self.status_label)

        # Connect button
        self.connect_button = QPushButton("Connect")
        self.connect_button.setMinimumHeight(40)
        self.connect_button.clicked.connect(self._on_connect_click)
        layout.addWidget(self.connect_button)

        # Remote device information (hidden by default)
        self.remote_info_group = QGroupBox("Remote Device Information")
        remote_info_layout = QVBoxLayout()

        # Remote OS display
        remote_os_layout = QHBoxLayout()
        remote_os_label = QLabel("Detected OS:")
        remote_os_label.setMinimumWidth(100)
        self.remote_os_value = QLabel("N/A")
        self.remote_os_value.setStyleSheet("font-weight: bold;")
        remote_os_layout.addWidget(remote_os_label)
        remote_os_layout.addWidget(self.remote_os_value)
        remote_os_layout.addStretch()
        remote_info_layout.addLayout(remote_os_layout)

        # Gateway status display
        gateway_layout = QHBoxLayout()
        gateway_label = QLabel("Device Type:")
        gateway_label.setMinimumWidth(100)
        self.gateway_value = QLabel("N/A")
        self.gateway_value.setStyleSheet("font-weight: bold;")
        gateway_layout.addWidget(gateway_label)
        gateway_layout.addWidget(self.gateway_value)
        gateway_layout.addStretch()
        remote_info_layout.addLayout(gateway_layout)

        self.remote_info_group.setLayout(remote_info_layout)
        layout.addWidget(self.remote_info_group)
        self.remote_info_group.hide()  # Hidden by default

        # Message sending section (hidden by default)
        self.message_group = QGroupBox("Send Message")
        message_main_layout = QVBoxLayout()

        # Message log (console output)
        log_label = QLabel("Message Log:")
        message_main_layout.addWidget(log_label)

        self.message_log = QTextEdit()
        self.message_log.setReadOnly(True)
        self.message_log.setMaximumHeight(150)
        font = QFont("Monospace", 9)
        self.message_log.setFont(font)
        self.message_log.setPlaceholderText("Connection log will appear here...")
        message_main_layout.addWidget(self.message_log)

        # Message input area
        input_label = QLabel("Message to send:")
        message_main_layout.addWidget(input_label)

        message_input_layout = QHBoxLayout()
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Type your message here...")
        self.message_input.returnPressed.connect(self._on_send_message)
        message_input_layout.addWidget(self.message_input)

        self.send_button = QPushButton("Send")
        self.send_button.setMinimumWidth(80)
        self.send_button.clicked.connect(self._on_send_message)
        message_input_layout.addWidget(self.send_button)

        message_main_layout.addLayout(message_input_layout)

        self.message_group.setLayout(message_main_layout)
        layout.addWidget(self.message_group)
        self.message_group.hide()  # Hidden by default

        # Add stretch to push device info to the bottom
        layout.addStretch()

        # Separator line
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator)

        # Local device information
        device_info_group = QGroupBox("Local Device Information")
        device_info_layout = QVBoxLayout()

        # Get local IP and hostname
        local_ip = get_local_ip()
        hostname = get_hostname()

        # Hostname display
        hostname_layout = QHBoxLayout()
        hostname_label = QLabel("Hostname:")
        hostname_label.setMinimumWidth(80)
        hostname_value = QLabel(hostname)
        hostname_value.setStyleSheet("font-weight: bold;")
        hostname_layout.addWidget(hostname_label)
        hostname_layout.addWidget(hostname_value)
        hostname_layout.addStretch()
        device_info_layout.addLayout(hostname_layout)

        # Local IP display
        ip_info_layout = QHBoxLayout()
        ip_info_label = QLabel("Local IP:")
        ip_info_label.setMinimumWidth(80)
        self.local_ip_value = QLabel(local_ip)
        self.local_ip_value.setStyleSheet("font-weight: bold; color: #0066cc;")
        ip_info_layout.addWidget(ip_info_label)
        ip_info_layout.addWidget(self.local_ip_value)
        ip_info_layout.addStretch()
        device_info_layout.addLayout(ip_info_layout)

        device_info_group.setLayout(device_info_layout)
        layout.addWidget(device_info_group)

    @Slot()
    def _on_connect_click(self):
        ip = self.ip_input.text()
        port = self.port_input.text()

        result = self.logic.connect(ip, port)

        # Update status label with appropriate styling
        self.status_label.setText(result['message'])

        if result['status'] == 'connected':
            self.status_label.setStyleSheet("padding: 10px; background-color: #d4edda; color: #155724; border-radius: 5px;")
            self.connect_button.setText("Disconnect")

            # Show and update remote device information
            remote_os = result.get('remote_os', 'Unknown')
            is_gateway = result.get('is_gateway', False)

            self.remote_os_value.setText(remote_os)

            if is_gateway:
                self.gateway_value.setText("Gateway (Router)")
                self.gateway_value.setStyleSheet("font-weight: bold; color: #ff6600;")
            else:
                self.gateway_value.setText("Network Device")
                self.gateway_value.setStyleSheet("font-weight: bold;")

            self.remote_info_group.show()

            # Show message sending section and log connection
            self.message_group.show()
            self._log_message(f"Connected to {ip}:{port}", "system")

        elif result['status'] == 'disconnected':
            self.status_label.setStyleSheet("padding: 10px; background-color: #f0f0f0; border-radius: 5px;")
            self.connect_button.setText("Connect")

            # Hide remote device information and message sending
            self.remote_info_group.hide()
            self.message_group.hide()
            self._log_message("Disconnected", "system")

        elif result['status'] == 'error':
            self.status_label.setStyleSheet("padding: 10px; background-color: #f8d7da; color: #721c24; border-radius: 5px;")

            # Hide remote device information and message sending on error
            self.remote_info_group.hide()
            self.message_group.hide()

    @Slot()
    def _on_send_message(self):
        """Handle sending a message to the connected device"""
        message = self.message_input.text()

        if not message:
            return

        # Send the message
        result = self.logic.send_message(message)

        if result['status'] == 'success':
            # Log the sent message
            self._log_message(f"SENT: {message}", "sent")
            self._log_message(f"✓ {result['message']}", "confirm")

            # If there's a response, log it
            if 'response' in result:
                self._log_message(f"RESPONSE: {result['response']}", "response")

            # Clear input field
            self.message_input.clear()

        elif result['status'] == 'error':
            self._log_message(f"✗ {result['message']}", "error")

            # If connection was broken, update UI
            if not self.logic.connected:
                self.status_label.setText("Connection lost")
                self.status_label.setStyleSheet("padding: 10px; background-color: #f8d7da; color: #721c24; border-radius: 5px;")
                self.connect_button.setText("Connect")
                self.remote_info_group.hide()
                self.message_group.hide()

    def _log_message(self, message: str, msg_type: str = "info"):
        """Add a message to the log with timestamp and formatting"""
        timestamp = datetime.now().strftime("%H:%M:%S")

        # Format based on message type
        if msg_type == "sent":
            formatted = f"<span style='color: #0066cc;'>[{timestamp}] {message}</span>"
        elif msg_type == "response":
            formatted = f"<span style='color: #009900;'>[{timestamp}] {message}</span>"
        elif msg_type == "confirm":
            formatted = f"<span style='color: #666666;'>[{timestamp}] {message}</span>"
        elif msg_type == "error":
            formatted = f"<span style='color: #cc0000;'>[{timestamp}] {message}</span>"
        elif msg_type == "system":
            formatted = f"<span style='color: #666666; font-weight: bold;'>[{timestamp}] {message}</span>"
        else:
            formatted = f"[{timestamp}] {message}"

        self.message_log.append(formatted)
