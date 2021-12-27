from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QListWidgetItem, QWidget

from .new_volume_controller import NewVolumeDialog
from .scan_library_controller import ScanDialog
from .update_controller import UpdateDialog
from .add_library_controller import AddLibraryDialog
from ..models import database_manager
from ..views.ui_main_layout import Ui_main_window
from ..views.ui_card_widget import Ui_CardWidget
from ..views.ui_flow_layout import FlowLayout


class CardWidget(QWidget, Ui_CardWidget):
    def __init__(self):
        super().__init__()

        # Initialize and set up various things
        self.setupUi(self)


class MainWindow(QWidget, Ui_main_window):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.add_icons()
        self.setup_flow_layout()
        self.connect_slots()

        # If there are no libraries yet, disable the buttons to make it not error out
        self.populate_library_list()
        if self.libraries_list_widget.count() > 0:
            self.libraries_list_widget.setCurrentRow(0)
        else:
            self.scan_library_btn.setEnabled(False)
            self.update_library_btn.setEnabled(False)
            self.new_volumes_btn.setEnabled(False)

        self.libraries_list_widget.model().rowsInserted.connect(self.new_library)

        
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


    def setup_flow_layout(self):
        self.series_layout = FlowLayout()
        self.series_layout.setSpacing(12)
        self.series_wrapper_layout_useless.addLayout(self.series_layout)
        

    def connect_slots(self):
        # Connect slots to signals
        self.libraries_list_widget.currentRowChanged.connect(self.populate_series_grid)
        self.add_library_btn.clicked.connect(self.add_library)
        self.settings_btn.clicked.connect(self.show_settings)
        self.scan_library_btn.clicked.connect(self.scan_library)
        self.update_library_btn.clicked.connect(self.update_library)
        self.new_volumes_btn.clicked.connect(self.view_new_volumes)


    def populate_library_list(self):
        self.libraries_list_widget.clear()
        list = database_manager.get_libraries()
        if list is None:
            return
        
        for library in list:
            self.libraries_list_widget.addItem(QListWidgetItem(library[1]))


    def populate_series_grid(self):
        """
        TODO - Redo the series grid to a flow layout so the card widgets wrap when the
               screen gets resized.
        """

        self.deleteItemsOfLayout(self.series_layout)
        print("updating series grid...")

        library_name = self.libraries_list_widget.currentItem().text()
        library_id = database_manager.get_library_id(library_name)[0]

        series_list = database_manager.get_series_from_library(library_id)
        self.current_library_label.setText(f"{library_name} | {len(series_list)}")

        for series in series_list:
            card = CardWidget()

            cover = QPixmap(f"data/covers/{series[2]}.jpg")
            if cover.isNull():
                cover = QPixmap("data/covers/no-image.png")

            card.cover_label.setPixmap(cover)
            card.series_label.setText(series[0])
            card.series_label.setToolTip(series[0])
            card.volume_label.setText(f"Volumes - {series[1]}")

            self.series_layout.addWidget(card)


    def add_library(self):
        print("You clicked add library")

        dlg = AddLibraryDialog(self)
        dlg.exec()
        name = dlg.get_name()

        if name != "":
            self.libraries_list_widget.addItem(QListWidgetItem(name))      


    def new_library(self):
        last_row = self.libraries_list_widget.count() - 1
        self.libraries_list_widget.setCurrentRow(last_row)

        self.scan_library_btn.setEnabled(True)
        self.update_library_btn.setEnabled(True)
        self.new_volumes_btn.setEnabled(True)



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


    def deleteItemsOfLayout(self, layout):
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
                    self.deleteItemsOfLayout(item.layout())