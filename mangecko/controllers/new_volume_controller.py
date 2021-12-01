from PySide6.QtWidgets import QCheckBox, QDialog, QLabel

from ..models import database_manager
from ..views.ui_new_volume_dialog import Ui_NewVolumeDialog


class NewVolumeDialog(QDialog, Ui_NewVolumeDialog):
    def __init__(self, library_id, parent=None):
        super().__init__()
        self.id = library_id

        # Initialize and set up various things
        self.setupUi(self)
        self.view_button.clicked.connect(self.display)
        self.close_button.clicked.connect(self.close)

    def display(self):
        self.view_button.setEnabled(False)
        # Display series with new volumes
        series = database_manager.series_with_new_volumes(self.id)
        
        for series in series:
            text = f"{series[0]}: Volume {series[1]} -> Volume {series[2]}"
            item = QCheckBox(text)
            self.label_layout.addWidget(item)