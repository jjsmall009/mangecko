from PySide6.QtWidgets import (
    QApplication, QDialog, QListWidgetItem, QMainWindow, QMessageBox, QWidget
)

from models import database_manager
from views.ui_main_layout import Ui_main_window

class MainWindow(QWidget, Ui_main_window):
    def __init__(self):
        super().__init__()

        # Initialize and set up various things
        self.setupUi(self)
        self.initialize_libraries()

        # Connect slots to signals
        self.libraries_list_widget.itemClicked.connect(self.display_library_items)

    def initialize_libraries(self):
        list = database_manager.get_libraries()

        if list is None:
            return
        
        for library in list:
            self.libraries_list_widget.addItem(QListWidgetItem(library[1]))

    def display_library_items(self):
        print(self.libraries_list_widget.currentItem().text())