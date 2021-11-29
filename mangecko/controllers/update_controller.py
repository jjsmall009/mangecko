from PySide6.QtWidgets import QDialog, QListWidgetItem
from PySide6.QtCore import QObject, QThread, Signal

from models.manga_model import Manga
from models import database_manager
from utilities.manga_scraper import series_scraper
from views.ui_update_dialog import Ui_Dialog


class Updater(QObject):
    counter = Signal(int)
    current_series = Signal(Manga)
    finished = Signal()

    def __init__(self, series):
        super().__init__()
        self.ongoing_series = series
        
    def update(self):
        updated_manga = []

        # Series tuple = (local_title, my_volumes, site_id)
        for count, series in enumerate(self.ongoing_series):
            current_manga = Manga(series[0], series[1])
            current_manga.site_id = series[2]

            series_scraper(series[2], current_manga)

            updated_manga.append(current_manga)
            database_manager.update_manga(current_manga)

            self.counter.emit(count + 1)
            self.current_series.emit(current_manga)
        
        self.finished.emit()    

class UpdateDialog(QDialog, Ui_Dialog):
    def __init__(self, library_id, parent=None):
        super().__init__()
        self.id = library_id
        self.ongoing_series = database_manager.get_ongoing(self.id)
        self.total_series = len(self.ongoing_series)

        # Initialize and set up various things
        self.setupUi(self)
        self.updater = Updater(self.ongoing_series)

        self.update_button.clicked.connect(self.do_the_update)
        self.close_button.clicked.connect(self.close)

    def do_the_update(self):
        self.update_button.setEnabled(False)
        self.thread = QThread()
        self.updater.moveToThread(self.thread)
        self.thread.started.connect(self.updater.update)

        self.updater.counter.connect(self.update_progress)
        self.updater.current_series.connect(self.update_list)
        self.updater.finished.connect(self.thread.quit)
        self.updater.finished.connect(self.updater.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

    def update_list(self, series):
        text = f"{series.local_title} - {series.my_volumes} - {series.eng_volumes} - {series.eng_status}"
        item = QListWidgetItem(text)
        self.list_widget.addItem(item)

    def update_progress(self, count):
        progressPercent = int(count / self.total_series * 100)
        self.progressBar.setValue(progressPercent)