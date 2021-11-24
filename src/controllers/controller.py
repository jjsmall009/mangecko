from PySide6.QtWidgets import (
    QApplication, QDialog, QListWidgetItem, QMainWindow, QMessageBox, QWidget
)

from models import database_manager
from views.ui_main_layout import Ui_main_window
from views.ui_card_widget import Ui_CardWidget

class CardWidget(QWidget, Ui_CardWidget):
    def __init__(self):
        super().__init__()

        # Initialize and set up various things
        self.setupUi(self)

class MainWindow(QWidget, Ui_main_window):
    def __init__(self):
        super().__init__()

        # Initialize and set up various things
        self.setupUi(self)
        self.initialize_library_list()

        # Connect slots to signals
        self.libraries_list_widget.itemClicked.connect(self.populate_series_grid)
        self.add_library_btn.clicked.connect(self.add_library)
        self.settings_btn.clicked.connect(self.show_settings)
        self.scan_library_btn.clicked.connect(self.scan_library)
        self.update_library_btn.clicked.connect(self.update_library)
        self.new_volumes_btn.clicked.connect(self.view_new_volumes)

    def initialize_library_list(self):
        list = database_manager.get_libraries()

        if list is None:
            return
        
        for library in list:
            self.libraries_list_widget.addItem(QListWidgetItem(library[1]))

    def populate_series_grid(self):
        library_name = self.libraries_list_widget.currentItem().text()
        library_id = database_manager.get_library_id(library_name)[0]

        series_list = database_manager.get_series_from_library(library_id)
        print(series_list)

        row, col = 0, 0
        for series in series_list:
            card = CardWidget()
            card.cover_label.setText(str(series[2]))
            card.series_label.setText(series[0])
            card.volume_label.setText(str(series[1]))

            self.series_grid_layout.addWidget(card, row, col)

            if col == 5:
                col = 0
                row += 1
            else:
                col += 1


    def add_library(self):
        print("You clicked add library")

    def show_settings(self):
        print("You clicked settings")

    def scan_library(self):
        print("You clicked scan library")

    def update_library(self):
        print("You clicked update library")

    def view_new_volumes(self):
        print("You clicked view new volumes")

