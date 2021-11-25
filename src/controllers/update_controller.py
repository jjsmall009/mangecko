from PySide6.QtWidgets import QDialog, QListWidgetItem
from PySide6 import QtCore

from models.manga_model import Manga
from models import database_manager
from utilities.manga_scraper import series_scraper
from views.ui_update_dialog import Ui_Dialog


class UpdateDialog(QDialog, Ui_Dialog):
    def __init__(self, library_id, parent=None):
        super().__init__()
        self.id = library_id

        # Initialize and set up various things
        self.setupUi(self)
        self.update_button.clicked.connect(self.update)
        self.close_button.clicked.connect(self.close)


    def update(self):
        # Query DB and get ongoing series
        ongoing_series = database_manager.get_ongoing(self.id)
        manga = []

        # Series tuple = (local_title, my_volumes, site_id)
        for series in ongoing_series:
            current_manga = Manga(series[0], series[1])
            current_manga.site_id = series[2]

            series_scraper(series[2], current_manga)

            manga.append(current_manga)
            database_manager.update_manga(current_manga)

        self.update_view(manga)


    def update_view(self, manga):
        for series in manga:
            text = f"{series.local_title} - {series.my_volumes} - {series.eng_volumes} - {series.eng_status}"
            item = QListWidgetItem(text)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            self.list_widget.addItem(item)
        