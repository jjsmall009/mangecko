from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication, QDialog, QListWidgetItem, QMainWindow, QMessageBox, QWidget
)
from pathlib import Path
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
        deleteItemsOfLayout(self.series_grid_layout)

        library_name = self.libraries_list_widget.currentItem().text()
        self.current_library_label.setText(library_name)
        library_id = database_manager.get_library_id(library_name)[0]

        series_list = database_manager.get_series_from_library(library_id)

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

    def show_settings(self):
        print("You clicked settings")

    def scan_library(self):
        print("You clicked scan library")
        library_name = self.libraries_list_widget.currentItem().text()
        library_id = database_manager.get_library_id(library_name)[0]
        print(library_id)

        path = Path(database_manager.get_library_path(library_id))
        scanner = LibraryScanner(path)
        scanner.scan_directory()
        valid_series = scanner.valid_folders
        manga = []

        for series, vol_count in valid_series.items():
            has_match = database_manager.series_exists(series, library_id)
            if has_match:
                database_manager.update_volume_info(series, vol_count)
            else:
                print(f"New series added -> {series}")
                current_manga = Manga(series, vol_count)
                id = series_search(series)

                if id != None:
                    current_manga.site_id = id
                    current_manga.has_match = True
                    series_scraper(id, current_manga)

                manga.append(current_manga)
        database_manager.insert_manga(manga, path.name)

        db_series = database_manager.get_series(library_id)
        for series in db_series:
            if series not in valid_series:
                print(f"Deleting {series}...")
                database_manager.delete_series(series)

        self.populate_series_grid()

    def update_library(self):
        print("You clicked update library")
        library_name = self.libraries_list_widget.currentItem().text()
        library_id = database_manager.get_library_id(library_name)[0]

        # Query DB and get ongoing series
        ongoing_series = database_manager.get_ongoing(library_id)

        # Series tuple = (local_title, my_volumes, site_id)
        for series in ongoing_series:
            current_manga = Manga(series[0], series[1])
            current_manga.site_id = series[2]

            series_scraper(series[2], current_manga)

            database_manager.update_manga(current_manga)

        self.populate_series_grid()

    def view_new_volumes(self):
        print("You clicked view new volumes")

