from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QPushButton, QLineEdit, QGroupBox)
from PySide6.QtCore import Qt, Slot
from src.core.app_logic import AppLogic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.logic = AppLogic()
        self._setup_ui()

    def _setup_ui(self):
        self.setWindowTitle("LinxTap")
        self.setMinimumSize(450, 350)

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

        # Add stretch to push everything to the top
        layout.addStretch()

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
        elif result['status'] == 'disconnected':
            self.status_label.setStyleSheet("padding: 10px; background-color: #f0f0f0; border-radius: 5px;")
            self.connect_button.setText("Connect")
        elif result['status'] == 'error':
            self.status_label.setStyleSheet("padding: 10px; background-color: #f8d7da; color: #721c24; border-radius: 5px;")
