"""
Setup and run our gui based manga manager application.
"""
from PySide6.QtWidgets import QApplication

from .controllers.controller import MainWindow
from .models import database_manager


def main():
    app = QApplication([])

    # Initialize our database and setup our connection
    database_manager.initialize()

    window = MainWindow()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()