from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LinxTap")
        self.setMinimumSize(400, 300)

        # Central widget
        central = QWidget()
        self.setCentralWidget(central)

        # Layout
        layout = QVBoxLayout(central)
        layout.setAlignment(Qt.AlignCenter)

        # Placeholder label
        label = QLabel("LinxTap")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
