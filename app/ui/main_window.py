from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton
from PyQt6.QtCore import QTimer
import logging

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Activity Tracker")
        self.resize(900, 600)

        layout = QVBoxLayout()
        self.status_label = QLabel("Tracker is idle")
        self.start_button = QPushButton("Start Tracking")
        self.start_button.clicked.connect(self.start_tracking)

        layout.addWidget(self.status_label)
        layout.addWidget(self.start_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.tracker_timer = QTimer()
        self.tracker_timer.timeout.connect(self.update_status)

    def start_tracking(self):
        self.tracker_timer.start(1000)
        self.status_label.setText("Tracking active...")
        logging.info("Tracking started")

    def update_status(self):
        logging.debug("Checking active window...")  # placeholder
