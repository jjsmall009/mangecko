from PySide6.QtWidgets import QDialog, QListWidgetItem
from pathlib import Path

from models.manga_model import Manga
from models import database_manager
from utilities.manga_scraper import series_scraper, series_search
from utilities.library_scanner import LibraryScanner
from views.ui_scan_dialog import Ui_ScanDialog

class ScanDialog(QDialog, Ui_ScanDialog):
    def __init__(self, library_id, parent=None):
        super().__init__()
        self.id = library_id

        # Initialize and set up various things
        self.setupUi(self)
        self.scan_button.clicked.connect(self.scan)
        self.close_button.clicked.connect(self.close)

    def scan(self):
        path = Path(database_manager.get_library_path(self.id))
        scanner = LibraryScanner(path)
        scanner.scan_directory()
        valid_series = scanner.valid_folders
        new_manga = []
        updated_manga = []
        removed = []

        for series, vol_count in valid_series.items():
            has_match = database_manager.series_exists(series, self.id)
            if has_match:
                if vol_count != has_match[4]:
                    database_manager.update_volume_info(series, vol_count)
                    updated_manga.append((series, vol_count))
            else:
                print(f"New series added -> {series}")
                current_manga = Manga(series, vol_count)
                id = series_search(series)

                if id != None:
                    current_manga.site_id = id
                    current_manga.has_match = True
                    series_scraper(id, current_manga)

                new_manga.append(current_manga)
        database_manager.insert_manga(new_manga, path.name)

        db_series = database_manager.get_series(self.id)
        for series in db_series:
            if series not in valid_series:
                print(f"Deleting {series}...")
                database_manager.delete_series(series)
                removed.append(series)

        self.update_view(new_manga, updated_manga, removed)
        
    def update_view(self, new_manga, updated_manga, removed):
        if (len(new_manga) and len(updated_manga) and len(removed)) == 0:
            self.info_label.setText("No changes have been found")
            return

        for series in new_manga:
            text = f"{series.local_title} - {series.my_volumes} volumes"
            self.new_series_list.addItem(QListWidgetItem(text))
        
        for series in updated_manga:
            text = f"{series[0]} -> {series[1]} volumes"
            self.new_vol_list.addItem(QListWidgetItem(text))

        for series in removed:
            text = f"{series}"
            self.removed_list.addItem(QListWidgetItem(text))

        self.info_label.setText("Library has been updated")