# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_library_dialogqAocTp.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_AddLibraryDialog(object):
    def setupUi(self, AddLibraryDialog):
        if not AddLibraryDialog.objectName():
            AddLibraryDialog.setObjectName(u"AddLibraryDialog")
        AddLibraryDialog.resize(900, 600)
        font = QFont()
        font.setPointSize(10)
        AddLibraryDialog.setFont(font)
        self.outer_layout = QVBoxLayout(AddLibraryDialog)
        self.outer_layout.setObjectName(u"outer_layout")
        self.upper_grid_layout = QGridLayout()
        self.upper_grid_layout.setObjectName(u"upper_grid_layout")
        self.label = QLabel(AddLibraryDialog)
        self.label.setObjectName(u"label")

        self.upper_grid_layout.addWidget(self.label, 0, 0, 1, 1)

        self.path_field = QLineEdit(AddLibraryDialog)
        self.path_field.setObjectName(u"path_field")

        self.upper_grid_layout.addWidget(self.path_field, 1, 0, 1, 1)

        self.open_btn = QPushButton(AddLibraryDialog)
        self.open_btn.setObjectName(u"open_btn")

        self.upper_grid_layout.addWidget(self.open_btn, 1, 1, 1, 1)

        self.add_library_btn = QPushButton(AddLibraryDialog)
        self.add_library_btn.setObjectName(u"add_library_btn")
        self.add_library_btn.setFont(font)

        self.upper_grid_layout.addWidget(self.add_library_btn, 1, 2, 1, 1)


        self.outer_layout.addLayout(self.upper_grid_layout)

        self.scrollArea = QScrollArea(AddLibraryDialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 880, 488))
        self.scroll_layout_dummy = QHBoxLayout(self.scrollAreaWidgetContents)
        self.scroll_layout_dummy.setObjectName(u"scroll_layout_dummy")
        self.series_table = QTableWidget(self.scrollAreaWidgetContents)
        if (self.series_table.columnCount() < 5):
            self.series_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.series_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.series_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.series_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.series_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.series_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.series_table.setObjectName(u"series_table")
        self.series_table.setShowGrid(True)
        self.series_table.verticalHeader().setVisible(True)
        self.series_table.verticalHeader().setHighlightSections(True)

        self.scroll_layout_dummy.addWidget(self.series_table)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.outer_layout.addWidget(self.scrollArea)

        self.bottom_btn_layout = QHBoxLayout()
        self.bottom_btn_layout.setObjectName(u"bottom_btn_layout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bottom_btn_layout.addItem(self.horizontalSpacer)

        self.loading_label = QLabel(AddLibraryDialog)
        self.loading_label.setObjectName(u"loading_label")

        self.bottom_btn_layout.addWidget(self.loading_label)

        self.done_btn = QPushButton(AddLibraryDialog)
        self.done_btn.setObjectName(u"done_btn")

        self.bottom_btn_layout.addWidget(self.done_btn)

        self.cancel_btn = QPushButton(AddLibraryDialog)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.bottom_btn_layout.addWidget(self.cancel_btn)


        self.outer_layout.addLayout(self.bottom_btn_layout)


        self.retranslateUi(AddLibraryDialog)

        QMetaObject.connectSlotsByName(AddLibraryDialog)
    # setupUi

    def retranslateUi(self, AddLibraryDialog):
        AddLibraryDialog.setWindowTitle(QCoreApplication.translate("AddLibraryDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("AddLibraryDialog", u"Library Path", None))
        self.path_field.setText("")
        self.open_btn.setText(QCoreApplication.translate("AddLibraryDialog", u"Open Library", None))
        self.add_library_btn.setText(QCoreApplication.translate("AddLibraryDialog", u"Add Library", None))
        ___qtablewidgetitem = self.series_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AddLibraryDialog", u"Title", None));
        ___qtablewidgetitem1 = self.series_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AddLibraryDialog", u"Site ID", None));
        ___qtablewidgetitem2 = self.series_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AddLibraryDialog", u"My Volumes", None));
        ___qtablewidgetitem3 = self.series_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AddLibraryDialog", u"English Volumes", None));
        ___qtablewidgetitem4 = self.series_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AddLibraryDialog", u"Source Volumes", None));
        self.loading_label.setText("")
        self.done_btn.setText(QCoreApplication.translate("AddLibraryDialog", u"Done", None))
        self.cancel_btn.setText(QCoreApplication.translate("AddLibraryDialog", u"Cancel", None))
    # retranslateUi

