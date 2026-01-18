from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt, Slot
from src.core.app_logic import AppLogic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.logic = AppLogic()
        self._setup_ui()

    def _setup_ui(self):
        self.setWindowTitle("LinxTap")
        self.setMinimumSize(400, 300)

        # Central widget
        central = QWidget()
        self.setCentralWidget(central)

        # Layout
        layout = QVBoxLayout(central)
        layout.setAlignment(Qt.AlignCenter)

        # Title label
        title = QLabel("LinxTap")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Status label
        self.status_label = QLabel("Click the button")
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

        # Button with signal/slot
        button = QPushButton("Click Me")
        button.clicked.connect(self._on_button_click)
        layout.addWidget(button)

    @Slot()
    def _on_button_click(self):
        result = self.logic.process_click()
        self.status_label.setText(result)
