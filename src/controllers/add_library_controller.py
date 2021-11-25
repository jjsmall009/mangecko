from PySide6.QtWidgets import QDialog, QListWidgetItem, QFileDialog
from PySide6 import QtCore

from models.manga_model import Manga
from models import database_manager
from utilities.manga_scraper import series_scraper
from views.ui_add_library_dialog import Ui_AddLibraryDialog

class AddLibraryDialog(QDialog, Ui_AddLibraryDialog):
    def __init__(self, parent=None):
        super().__init__()

        self.setupUi(self)

        # Create our signals and slots
        self.open_btn.clicked.connect(self.open_file)
        self.add_library_btn.clicked.connect(self.add_library)
        self.done_btn.clicked.connect(self.close)
        self.cancel_btn.clicked.connect(self.close)

    def open_file(self):
        fname = QFileDialog.getExistingDirectory(self, 'Open file', 'c:\\')
        self.path_field.setText(fname)

    def add_library(self):
        pass
