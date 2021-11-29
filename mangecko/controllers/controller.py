from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (QListWidgetItem, QMessageBox, QWidget)

from pathlib import Path

from controllers.new_volume_controller import NewVolumeDialog
from controllers.scan_library_controller import ScanDialog
from controllers.update_controller import UpdateDialog
from controllers.add_library_controller import AddLibraryDialog
from models.manga_model import Manga
from models import database_manager
from utilities.manga_scraper import series_scraper, series_search
from utilities.library_scanner import LibraryScanner
from views.ui_main_layout import Ui_main_window
from views.ui_card_widget import Ui_CardWidget


def deleteItemsOfLayout(layout):
    """
    Prevents the series grid layout from overlaying cards on top of one another
    when you switch back and forth between libraries. Not the most elegant...
    """
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
            else:
                deleteItemsOfLayout(item.layout())


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
        self.add_icons()
        self.initialize_library_list()

        # Connect slots to signals
        self.libraries_list_widget.currentRowChanged.connect(self.populate_series_grid)
        self.add_library_btn.clicked.connect(self.add_library)
        self.settings_btn.clicked.connect(self.show_settings)
        self.scan_library_btn.clicked.connect(self.scan_library)
        self.update_library_btn.clicked.connect(self.update_library)
        self.new_volumes_btn.clicked.connect(self.view_new_volumes)
        

    def initialize_library_list(self):
        self.libraries_list_widget.clear()
        list = database_manager.get_libraries()
        if list is None:
            return
        
        for library in list:
            self.libraries_list_widget.addItem(QListWidgetItem(library[1]))


    def add_icons(self):
        """
        Qt Designer adds in the wrong path so here you go.
        """
        icon1 = QIcon()
        icon1.addFile("resources/icons/add-128.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_library_btn.setIcon(icon1)

        icon2 = QIcon()
        icon2.addFile("resources/icons/settings-4-128.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_btn.setIcon(icon2)


    def populate_series_grid(self):
        """
        TODO - Redo the series grid to a flow layout so the card widgets wrap when the
               screen gets resized.
        """
        deleteItemsOfLayout(self.series_grid_layout)
        print("updating series grid...")

        library_name = self.libraries_list_widget.currentItem().text()
        library_id = database_manager.get_library_id(library_name)[0]

        series_list = database_manager.get_series_from_library(library_id)
        self.current_library_label.setText(f"{library_name} | {len(series_list)}")

        row, col = 0, 0
        for series in series_list:
            card = CardWidget()
            if series[2] == None:
                cover = QPixmap("data/covers/no-image.png")
            else:
                cover = QPixmap(f"data/covers/{series[2]}.jpg")
            card.cover_label.setPixmap(cover)
            card.series_label.setText(series[0])
            card.volume_label.setText(f"Volumes - {series[1]}")

            self.series_grid_layout.addWidget(card, row, col)

            if col == 5:
                col = 0
                row += 1
            else:
                col += 1

    def add_library(self):
        print("You clicked add library")

        dlg = AddLibraryDialog(self)
        dlg.exec()

        self.initialize_library_list()

    def show_settings(self):
        print("You clicked settings! No settings currently...")

    def scan_library(self):
        print("You clicked scan library")
        library_name = self.libraries_list_widget.currentItem().text()
        library_id = database_manager.get_library_id(library_name)[0]

        dlg = ScanDialog(library_id, self)
        dlg.exec()

        self.populate_series_grid()

    def update_library(self):
        print("You clicked update library")
        
        library_name = self.libraries_list_widget.currentItem().text()
        library_id = database_manager.get_library_id(library_name)[0]
        
        dlg = UpdateDialog(library_id, self)
        dlg.exec()

        self.populate_series_grid()

    def view_new_volumes(self):
        print("You clicked view new volumes")
        library_name = self.libraries_list_widget.currentItem().text()
        library_id = database_manager.get_library_id(library_name)[0]

        dlg = NewVolumeDialog(library_id, self)
        dlg.exec()