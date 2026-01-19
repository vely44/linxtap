from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QPushButton, QLineEdit, QFrame, QTextEdit, QFileDialog)
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
        self.setMinimumSize(550, 600)

        # Modern dark theme with terminal aesthetics
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e1e;
            }
            QWidget {
                background-color: #1e1e1e;
                color: #d4d4d4;
                font-family: 'Monospace', 'Consolas', 'Courier New';
            }
            QLabel {
                color: #d4d4d4;
                font-size: 11px;
            }
            QLineEdit {
                background-color: #2d2d2d;
                border: 1px solid #3e3e3e;
                border-radius: 3px;
                padding: 6px 8px;
                color: #d4d4d4;
                font-size: 11px;
            }
            QLineEdit:focus {
                border: 1px solid #007acc;
            }
            QPushButton {
                background-color: #0e639c;
                border: none;
                border-radius: 3px;
                padding: 8px 16px;
                color: #ffffff;
                font-weight: 500;
                font-size: 11px;
            }
            QPushButton:hover {
                background-color: #1177bb;
            }
            QPushButton:pressed {
                background-color: #0d5a8f;
            }
            QTextEdit {
                background-color: #1e1e1e;
                border: 1px solid #3e3e3e;
                border-radius: 3px;
                color: #d4d4d4;
                padding: 4px;
            }
            QFrame#divider {
                background-color: #3e3e3e;
            }
        """)

        # Central widget
        central = QWidget()
        self.setCentralWidget(central)

        # Main layout
        layout = QVBoxLayout(central)
        layout.setSpacing(12)
        layout.setContentsMargins(16, 16, 16, 16)

        # Title with modern styling
        title = QLabel("● LinxTap")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: #4ec9b0; padding: 8px;")
        layout.addWidget(title)

        # Connection inputs in a card-like container
        connection_container = QFrame()
        connection_container.setStyleSheet("""
            QFrame {
                background-color: #252526;
                border-radius: 4px;
                padding: 12px;
            }
        """)
        connection_layout = QVBoxLayout(connection_container)
        connection_layout.setSpacing(8)

        # IP address input
        ip_layout = QHBoxLayout()
        ip_label = QLabel("IP")
        ip_label.setMinimumWidth(60)
        ip_label.setStyleSheet("color: #9cdcfe; font-weight: 500;")
        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("127.0.0.1")
        self.ip_input.setText("127.0.0.1")
        ip_layout.addWidget(ip_label)
        ip_layout.addWidget(self.ip_input)
        connection_layout.addLayout(ip_layout)

        # Port input
        port_layout = QHBoxLayout()
        port_label = QLabel("PORT")
        port_label.setMinimumWidth(60)
        port_label.setStyleSheet("color: #9cdcfe; font-weight: 500;")
        self.port_input = QLineEdit()
        self.port_input.setPlaceholderText("8080")
        self.port_input.setText("8080")
        port_layout.addWidget(port_label)
        port_layout.addWidget(self.port_input)
        connection_layout.addLayout(port_layout)

        layout.addWidget(connection_container)

        # Status display with icon
        self.status_label = QLabel("○ Not connected")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("""
            padding: 8px;
            background-color: #3c3c3c;
            border-radius: 3px;
            color: #858585;
            font-size: 11px;
        """)
        layout.addWidget(self.status_label)

        # Connect button
        self.connect_button = QPushButton("⚡ CONNECT")
        self.connect_button.setMinimumHeight(36)
        self.connect_button.clicked.connect(self._on_connect_click)
        layout.addWidget(self.connect_button)

        # Remote device info panel (hidden by default)
        self.remote_info_panel = QFrame()
        self.remote_info_panel.setStyleSheet("""
            QFrame {
                background-color: #252526;
                border-radius: 4px;
                padding: 10px;
            }
        """)
        remote_info_layout = QVBoxLayout(self.remote_info_panel)
        remote_info_layout.setSpacing(6)

        remote_title = QLabel("▸ REMOTE DEVICE")
        remote_title.setStyleSheet("color: #4ec9b0; font-weight: bold; font-size: 10px;")
        remote_info_layout.addWidget(remote_title)

        # Remote OS
        remote_os_layout = QHBoxLayout()
        remote_os_label = QLabel("OS:")
        remote_os_label.setStyleSheet("color: #858585;")
        remote_os_label.setMinimumWidth(80)
        self.remote_os_value = QLabel("N/A")
        self.remote_os_value.setStyleSheet("color: #d4d4d4; font-weight: 500;")
        remote_os_layout.addWidget(remote_os_label)
        remote_os_layout.addWidget(self.remote_os_value)
        remote_os_layout.addStretch()
        remote_info_layout.addLayout(remote_os_layout)

        # Gateway status
        gateway_layout = QHBoxLayout()
        gateway_label = QLabel("Type:")
        gateway_label.setStyleSheet("color: #858585;")
        gateway_label.setMinimumWidth(80)
        self.gateway_value = QLabel("N/A")
        self.gateway_value.setStyleSheet("color: #d4d4d4; font-weight: 500;")
        gateway_layout.addWidget(gateway_label)
        gateway_layout.addWidget(self.gateway_value)
        gateway_layout.addStretch()
        remote_info_layout.addLayout(gateway_layout)

        layout.addWidget(self.remote_info_panel)
        self.remote_info_panel.hide()

        # Message panel (hidden by default)
        self.message_panel = QFrame()
        self.message_panel.setStyleSheet("""
            QFrame {
                background-color: #252526;
                border-radius: 4px;
                padding: 10px;
            }
        """)
        message_main_layout = QVBoxLayout(self.message_panel)
        message_main_layout.setSpacing(6)

        # Message log header with export button
        log_header = QHBoxLayout()
        log_title = QLabel("▸ MESSAGE LOG")
        log_title.setStyleSheet("color: #4ec9b0; font-weight: bold; font-size: 10px;")
        log_header.addWidget(log_title)
        log_header.addStretch()

        self.export_button = QPushButton("💾 Export")
        self.export_button.setStyleSheet("""
            QPushButton {
                background-color: #3c3c3c;
                padding: 4px 10px;
                font-size: 9px;
            }
            QPushButton:hover {
                background-color: #505050;
            }
        """)
        self.export_button.clicked.connect(self._export_log)
        log_header.addWidget(self.export_button)
        message_main_layout.addLayout(log_header)

        # Message log
        self.message_log = QTextEdit()
        self.message_log.setReadOnly(True)
        self.message_log.setMaximumHeight(100)
        font = QFont("Monospace", 9)
        self.message_log.setFont(font)
        self.message_log.setPlaceholderText("Connection log appears here...")
        message_main_layout.addWidget(self.message_log)

        # Message input
        message_input_layout = QHBoxLayout()
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Type message and press Enter...")
        self.message_input.returnPressed.connect(self._on_send_message)
        message_input_layout.addWidget(self.message_input)

        self.send_button = QPushButton("→ Send")
        self.send_button.setMinimumWidth(70)
        self.send_button.setStyleSheet("""
            QPushButton {
                background-color: #0e639c;
                font-size: 11px;
            }
        """)
        self.send_button.clicked.connect(self._on_send_message)
        message_input_layout.addWidget(self.send_button)
        message_main_layout.addLayout(message_input_layout)

        layout.addWidget(self.message_panel)
        self.message_panel.hide()

        # Add stretch to push local info to bottom
        layout.addStretch()

        # Divider
        divider = QFrame()
        divider.setObjectName("divider")
        divider.setFrameShape(QFrame.HLine)
        divider.setFixedHeight(1)
        layout.addWidget(divider)

        # Local device info panel
        local_info_panel = QFrame()
        local_info_panel.setStyleSheet("""
            QFrame {
                background-color: #252526;
                border-radius: 4px;
                padding: 10px;
            }
        """)
        local_info_layout = QVBoxLayout(local_info_panel)
        local_info_layout.setSpacing(6)

        local_title = QLabel("▸ LOCAL DEVICE")
        local_title.setStyleSheet("color: #4ec9b0; font-weight: bold; font-size: 10px;")
        local_info_layout.addWidget(local_title)

        # Get local IP and hostname
        local_ip = get_local_ip()
        hostname = get_hostname()

        # Hostname
        hostname_layout = QHBoxLayout()
        hostname_label = QLabel("Host:")
        hostname_label.setStyleSheet("color: #858585;")
        hostname_label.setMinimumWidth(80)
        hostname_value = QLabel(hostname)
        hostname_value.setStyleSheet("color: #d4d4d4; font-weight: 500;")
        hostname_layout.addWidget(hostname_label)
        hostname_layout.addWidget(hostname_value)
        hostname_layout.addStretch()
        local_info_layout.addLayout(hostname_layout)

        # Local IP
        ip_info_layout = QHBoxLayout()
        ip_info_label = QLabel("IP:")
        ip_info_label.setStyleSheet("color: #858585;")
        ip_info_label.setMinimumWidth(80)
        self.local_ip_value = QLabel(local_ip)
        self.local_ip_value.setStyleSheet("color: #569cd6; font-weight: 500;")
        ip_info_layout.addWidget(ip_info_label)
        ip_info_layout.addWidget(self.local_ip_value)
        ip_info_layout.addStretch()
        local_info_layout.addLayout(ip_info_layout)

        layout.addWidget(local_info_panel)

    @Slot()
    def _on_connect_click(self):
        ip = self.ip_input.text()
        port = self.port_input.text()

        result = self.logic.connect(ip, port)

        # Update status label with modern styling
        if result['status'] == 'connected':
            self.status_label.setText(f"● Connected to {ip}:{port}")
            self.status_label.setStyleSheet("""
                padding: 8px;
                background-color: #2d5016;
                border-radius: 3px;
                color: #8fd460;
                font-size: 11px;
            """)
            self.connect_button.setText("⚠ DISCONNECT")
            self.connect_button.setStyleSheet("""
                QPushButton {
                    background-color: #8b0000;
                    border: none;
                    border-radius: 3px;
                    padding: 8px 16px;
                    color: #ffffff;
                    font-weight: 500;
                    font-size: 11px;
                }
                QPushButton:hover {
                    background-color: #a00000;
                }
            """)

            # Update remote device information
            remote_os = result.get('remote_os', 'Unknown')
            is_gateway = result.get('is_gateway', False)

            self.remote_os_value.setText(remote_os)

            if is_gateway:
                self.gateway_value.setText("Gateway (Router)")
                self.gateway_value.setStyleSheet("color: #ff9800; font-weight: 500;")
            else:
                self.gateway_value.setText("Network Device")
                self.gateway_value.setStyleSheet("color: #d4d4d4; font-weight: 500;")

            self.remote_info_panel.show()
            self.message_panel.show()
            self._log_message(f"Connected to {ip}:{port}", "system")

        elif result['status'] == 'disconnected':
            self.status_label.setText("○ Not connected")
            self.status_label.setStyleSheet("""
                padding: 8px;
                background-color: #3c3c3c;
                border-radius: 3px;
                color: #858585;
                font-size: 11px;
            """)
            self.connect_button.setText("⚡ CONNECT")
            self.connect_button.setStyleSheet("""
                QPushButton {
                    background-color: #0e639c;
                    border: none;
                    border-radius: 3px;
                    padding: 8px 16px;
                    color: #ffffff;
                    font-weight: 500;
                    font-size: 11px;
                }
                QPushButton:hover {
                    background-color: #1177bb;
                }
            """)

            self.remote_info_panel.hide()
            self.message_panel.hide()
            self._log_message("Disconnected", "system")

        elif result['status'] == 'error':
            self.status_label.setText(f"✗ {result['message']}")
            self.status_label.setStyleSheet("""
                padding: 8px;
                background-color: #5a1d1d;
                border-radius: 3px;
                color: #f48771;
                font-size: 11px;
            """)

            self.remote_info_panel.hide()
            self.message_panel.hide()

    @Slot()
    def _on_send_message(self):
        """Handle sending a message to the connected device"""
        message = self.message_input.text()

        if not message:
            return

        # Send the message
        result = self.logic.send_message(message)

        if result['status'] == 'success':
            self._log_message(f"SENT: {message}", "sent")
            self._log_message(f"✓ {result['message']}", "confirm")

            if 'response' in result:
                self._log_message(f"RESPONSE: {result['response']}", "response")

            self.message_input.clear()

        elif result['status'] == 'error':
            self._log_message(f"✗ {result['message']}", "error")

            # If connection was broken, update UI
            if not self.logic.connected:
                self.status_label.setText("✗ Connection lost")
                self.status_label.setStyleSheet("""
                    padding: 8px;
                    background-color: #5a1d1d;
                    border-radius: 3px;
                    color: #f48771;
                    font-size: 11px;
                """)
                self.connect_button.setText("⚡ CONNECT")
                self.connect_button.setStyleSheet("""
                    QPushButton {
                        background-color: #0e639c;
                        border: none;
                        border-radius: 3px;
                        padding: 8px 16px;
                        color: #ffffff;
                        font-weight: 500;
                        font-size: 11px;
                    }
                    QPushButton:hover {
                        background-color: #1177bb;
                    }
                """)
                self.remote_info_panel.hide()
                self.message_panel.hide()

    def _log_message(self, message: str, msg_type: str = "info"):
        """Add a message to the log with timestamp and modern terminal formatting"""
        timestamp = datetime.now().strftime("%H:%M:%S")

        # Modern terminal color scheme
        if msg_type == "sent":
            formatted = f"<span style='color: #569cd6;'>[{timestamp}] {message}</span>"
        elif msg_type == "response":
            formatted = f"<span style='color: #4ec9b0;'>[{timestamp}] {message}</span>"
        elif msg_type == "confirm":
            formatted = f"<span style='color: #6a9955;'>[{timestamp}] {message}</span>"
        elif msg_type == "error":
            formatted = f"<span style='color: #f48771;'>[{timestamp}] {message}</span>"
        elif msg_type == "system":
            formatted = f"<span style='color: #9cdcfe; font-weight: bold;'>[{timestamp}] {message}</span>"
        else:
            formatted = f"<span style='color: #d4d4d4;'>[{timestamp}] {message}</span>"

        self.message_log.append(formatted)

    @Slot()
    def _export_log(self):
        """Export the message log to a text file"""
        if not self.message_log.toPlainText():
            return

        # Open save dialog
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Export Message Log",
            f"linxtap_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            "Text Files (*.txt);;All Files (*)"
        )

        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(self.message_log.toPlainText())
                self._log_message(f"Log exported to {file_path}", "system")
            except Exception as e:
                self._log_message(f"Export failed: {str(e)}", "error")
