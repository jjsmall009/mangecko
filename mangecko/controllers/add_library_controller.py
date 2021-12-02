from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QObject, QThread, Signal
from pathlib import Path

from ..models.manga_model import Manga
from ..models import database_manager
from ..utilities.manga_scraper import series_scraper, series_search
from ..utilities.library_scanner import LibraryScanner
from ..views.ui_add_library_dialog import Ui_AddLibraryDialog


class LibraryAdder(QObject):
    counter = Signal(int)
    current_series = Signal(Manga)
    exists = Signal()
    finished = Signal()

    def __init__(self, path, valid):
        super().__init__()
        self.library_path = path
        self.valid_series = valid

    def add_library(self):
        """
        A library is just a collection of series that are related to one another 
        (Completed, Ongoing, Favorites, Raw, etc.)

        A library in the database stores info about all matching series in the folder, 
        even ones that don't have a MangaUpdates match.
        """
        manga = []

        if not database_manager.insert_library(self.library_path.name, str(self.library_path)):
            self.exists.emit()
            print("I have emitted failure")
            return

        # For each valid folder, create a Manga object and then get some precious data
        for count, (series, vol_count) in enumerate(self.valid_series.items()):
            current_manga = Manga(series, vol_count)
            id = series_search(series)

            if id != None:
                current_manga.site_id = id
                current_manga.has_match = True
                series_scraper(id, current_manga)

            manga.append(current_manga)

            self.counter.emit(count + 1)
            self.current_series.emit(current_manga)

        database_manager.insert_manga(manga, self.library_path.name)
        self.finished.emit()


class AddLibraryDialog(QDialog, Ui_AddLibraryDialog):
    def __init__(self, parent=None):
        super().__init__()

        self.setupUi(self)
        self.done_btn.setEnabled(False)
        self.count = 0
        self.thread = QThread(parent=self)
        self.series_table.setColumnWidth(0,400)

        # Create our signals and slots
        self.open_btn.clicked.connect(self.open_file)
        self.add_library_btn.clicked.connect(self.setup_library)
        self.done_btn.clicked.connect(self.terminate)
        self.cancel_btn.clicked.connect(self.terminate)


    def open_file(self):
        fname = QFileDialog.getExistingDirectory(self, 'c:\\')
        self.path_field.setText(fname)

        self.add_library_btn.setEnabled(True)


    def setup_library(self):
        self.path = Path(self.path_field.text())

        if not Path(self.path).exists():
            QMessageBox.about(self, "Not valid path", "Not a valid path")
            return

        scanner = LibraryScanner(self.path)
        scanner.scan_directory()
        self.valid_series = scanner.valid_folders

        if len(scanner.valid_folders) == 0:
            QMessageBox.about(self, "No folders", "No folders founds. Not a valid library.")
            return

        # Thread it up
        self.adder = LibraryAdder(self.path, self.valid_series)
        
        self.adder.moveToThread(self.thread)
        self.thread.started.connect(self.adder.add_library)

        self.adder.counter.connect(self.update_progress)
        self.adder.current_series.connect(self.update_list)
        self.adder.exists.connect(self.library_exists)
        self.adder.finished.connect(self.cleanup)
        self.thread.start()


    def cleanup(self):
        self.done_btn.setEnabled(True)
        self.adder.finished.connect(self.thread.quit)
        self.adder.finished.connect(self.adder.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)


    def terminate(self):
        if self.thread.isRunning():
            self.thread.quit()
        self.close()
        

    def library_exists(self):
        QMessageBox.about(self, "Library exists", "Library already exists")


    def update_list(self, series):
        self.series_table.insertRow(self.count)
        self.series_table.setItem(self.count, 0, QTableWidgetItem(series.local_title))
        self.series_table.setItem(self.count, 1, QTableWidgetItem(str(series.site_id)))
        self.series_table.setItem(self.count, 2, QTableWidgetItem(str(series.my_volumes)))
        self.series_table.setItem(self.count, 3, QTableWidgetItem(str(series.eng_volumes)))
        self.series_table.setItem(self.count, 4, QTableWidgetItem(str(series.source_volumes)))
        self.count += 1
        

    def update_progress(self, count):
        progressPercent = int(count / len(self.valid_series) * 100)
        self.progressBar.setValue(progressPercent)