import sys
import logging
from PyQt6.QtWidgets import QApplication
from app.ui.main_window import MainWindow
from app.core.logger import setup_logger

def main():
    setup_logger()
    logging.info("Starting User Activity Tracker")

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
