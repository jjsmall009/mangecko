# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scan_dialoglpChAn.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGroupBox,
    QHBoxLayout, QListWidget, QListWidgetItem, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_ScanDialog(object):
    def setupUi(self, ScanDialog):
        if not ScanDialog.objectName():
            ScanDialog.setObjectName(u"ScanDialog")
        ScanDialog.resize(650, 600)
        font = QFont()
        font.setPointSize(10)
        ScanDialog.setFont(font)
        self.verticalLayout = QVBoxLayout(ScanDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(ScanDialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 632, 154))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.new_series_list = QListWidget(self.groupBox)
        self.new_series_list.setObjectName(u"new_series_list")

        self.horizontalLayout_5.addWidget(self.new_series_list)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.scrollArea_2 = QScrollArea(ScanDialog)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        self.scrollArea_2.setFont(font1)
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 632, 191))
        self.horizontalLayout_3 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.new_vol_list = QListWidget(self.groupBox_2)
        self.new_vol_list.setObjectName(u"new_vol_list")

        self.horizontalLayout_6.addWidget(self.new_vol_list)


        self.horizontalLayout_3.addWidget(self.groupBox_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.scrollArea_2)

        self.scrollArea_3 = QScrollArea(ScanDialog)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setFrameShape(QFrame.NoFrame)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 632, 191))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.removed_list = QListWidget(self.groupBox_3)
        self.removed_list.setObjectName(u"removed_list")

        self.horizontalLayout_7.addWidget(self.removed_list)


        self.horizontalLayout_4.addWidget(self.groupBox_3)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout.addWidget(self.scrollArea_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.scan_button = QPushButton(ScanDialog)
        self.scan_button.setObjectName(u"scan_button")

        self.horizontalLayout.addWidget(self.scan_button)

        self.close_button = QPushButton(ScanDialog)
        self.close_button.setObjectName(u"close_button")

        self.horizontalLayout.addWidget(self.close_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ScanDialog)

        QMetaObject.connectSlotsByName(ScanDialog)
    # setupUi

    def retranslateUi(self, ScanDialog):
        ScanDialog.setWindowTitle(QCoreApplication.translate("ScanDialog", u"Scan Library", None))
        self.groupBox.setTitle(QCoreApplication.translate("ScanDialog", u"New Series", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ScanDialog", u"New Volumes", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ScanDialog", u"Removed Series", None))
        self.scan_button.setText(QCoreApplication.translate("ScanDialog", u"Scan", None))
        self.close_button.setText(QCoreApplication.translate("ScanDialog", u"Close", None))
    # retranslateUi

