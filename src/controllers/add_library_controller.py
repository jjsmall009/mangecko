from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox, QTableWidgetItem
from PySide6 import QtCore
from pathlib import Path

from models.manga_model import Manga
from models import database_manager
from utilities.manga_scraper import series_scraper, series_search
from utilities.library_scanner import LibraryScanner
from views.ui_add_library_dialog import Ui_AddLibraryDialog

class AddLibraryDialog(QDialog, Ui_AddLibraryDialog):
    def __init__(self, parent=None):
        super().__init__()

        self.setupUi(self)
        self.add_library_btn.setEnabled(False)

        # Create our signals and slots
        self.open_btn.clicked.connect(self.open_file)
        self.add_library_btn.clicked.connect(self.add_library)
        self.done_btn.clicked.connect(self.close)
        self.cancel_btn.clicked.connect(self.close)

    def open_file(self):
        fname = QFileDialog.getExistingDirectory(self, 'c:\\')
        self.path_field.setText(fname)

        self.add_library_btn.setEnabled(True)

    def add_library(self):
        """
        A library is just a collection of series that are related to one another 
        (Completed, Ongoing, Favorites, Raw, etc.)

        A library in the database stores info about all matching series in the folder, 
        even ones that don't have a MangaUpdates match.
        """

        path = Path(self.path_field.text())

        if not Path(path).exists():
            QMessageBox.about(self, "Not valid path", "Not a valid path")
            return

        scanner = LibraryScanner(path)
        scanner.scan_directory()
        valid_series = scanner.valid_folders
        manga = []

        if len(scanner.valid_folders) == 0:
            QMessageBox.about(self, "No folders", "No folders founds. Not a valid library.")
            return
        else:
            if not database_manager.insert_library(path.name, str(path)):
                QMessageBox.about(self, "Library exists", "Library already exists")
                return

            # For each valid folder, create a Manga object and then get some precious data
            for series, vol_count in valid_series.items():
                current_manga = Manga(series, vol_count)
                id = series_search(series)

                if id != None:
                    current_manga.site_id = id
                    current_manga.has_match = True
                    series_scraper(id, current_manga)

                manga.append(current_manga)

            database_manager.insert_manga(manga, path.name)

        self.update_view(manga)


    def update_view(self, manga):
        for row, series in enumerate(manga):
            self.series_table.insertRow(row)
            self.series_table.setItem(row, 0, QTableWidgetItem(series.local_title))
            self.series_table.setItem(row, 1, QTableWidgetItem(str(series.site_id)))
            self.series_table.setItem(row, 2, QTableWidgetItem(str(series.my_volumes)))
            self.series_table.setItem(row, 3, QTableWidgetItem(str(series.eng_volumes)))
            self.series_table.setItem(row, 4, QTableWidgetItem(str(series.source_volumes)))

        self.series_table.resizeColumnsToContents()
