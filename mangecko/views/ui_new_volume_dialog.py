# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_volume_dialogqsxirn.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QProgressBar, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_NewVolumeDialog(object):
    def setupUi(self, NewVolumeDialog):
        if not NewVolumeDialog.objectName():
            NewVolumeDialog.setObjectName(u"NewVolumeDialog")
        NewVolumeDialog.resize(600, 400)
        font = QFont()
        font.setPointSize(10)
        NewVolumeDialog.setFont(font)
        self.verticalLayout = QVBoxLayout(NewVolumeDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(NewVolumeDialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.label_widget = QWidget()
        self.label_widget.setObjectName(u"label_widget")
        self.label_widget.setGeometry(QRect(0, 0, 582, 348))
        self.label_layout = QVBoxLayout(self.label_widget)
        self.label_layout.setObjectName(u"label_layout")
        self.label_layout.setContentsMargins(9, 9, 9, 9)
        self.scrollArea.setWidget(self.label_widget)

        self.verticalLayout.addWidget(self.scrollArea)

        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.setObjectName(u"bottom_layout")
        self.loading_bar = QProgressBar(NewVolumeDialog)
        self.loading_bar.setObjectName(u"loading_bar")
        self.loading_bar.setValue(24)
        self.loading_bar.setInvertedAppearance(False)
        self.loading_bar.setTextDirection(QProgressBar.TopToBottom)

        self.bottom_layout.addWidget(self.loading_bar)

        self.view_button = QPushButton(NewVolumeDialog)
        self.view_button.setObjectName(u"view_button")
        self.view_button.setFont(font)

        self.bottom_layout.addWidget(self.view_button)

        self.close_button = QPushButton(NewVolumeDialog)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setFont(font)

        self.bottom_layout.addWidget(self.close_button)


        self.verticalLayout.addLayout(self.bottom_layout)


        self.retranslateUi(NewVolumeDialog)

        QMetaObject.connectSlotsByName(NewVolumeDialog)
    # setupUi

    def retranslateUi(self, NewVolumeDialog):
        NewVolumeDialog.setWindowTitle(QCoreApplication.translate("NewVolumeDialog", u"New Volumes", None))
        self.view_button.setText(QCoreApplication.translate("NewVolumeDialog", u"View", None))
        self.close_button.setText(QCoreApplication.translate("NewVolumeDialog", u"Close", None))
    # retranslateUi

