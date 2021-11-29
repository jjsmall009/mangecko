# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_volume_dialogRobKUv.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_NewVolumeDialog(object):
    def setupUi(self, NewVolumeDialog):
        if not NewVolumeDialog.objectName():
            NewVolumeDialog.setObjectName(u"NewVolumeDialog")
        NewVolumeDialog.resize(600, 400)
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(10)
        NewVolumeDialog.setFont(font)
        self.verticalLayout = QVBoxLayout(NewVolumeDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(NewVolumeDialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.label_widget = QWidget()
        self.label_widget.setObjectName(u"label_widget")
        self.label_widget.setGeometry(QRect(0, 0, 580, 346))
        self.label_layout = QVBoxLayout(self.label_widget)
        self.label_layout.setObjectName(u"label_layout")
        self.scrollArea.setWidget(self.label_widget)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.view_button = QPushButton(NewVolumeDialog)
        self.view_button.setObjectName(u"view_button")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        self.view_button.setFont(font1)

        self.horizontalLayout.addWidget(self.view_button)

        self.close_button = QPushButton(NewVolumeDialog)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setFont(font1)

        self.horizontalLayout.addWidget(self.close_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(NewVolumeDialog)

        QMetaObject.connectSlotsByName(NewVolumeDialog)
    # setupUi

    def retranslateUi(self, NewVolumeDialog):
        NewVolumeDialog.setWindowTitle(QCoreApplication.translate("NewVolumeDialog", u"New Volumes", None))
        self.view_button.setText(QCoreApplication.translate("NewVolumeDialog", u"View", None))
        self.close_button.setText(QCoreApplication.translate("NewVolumeDialog", u"Close", None))
    # retranslateUi

