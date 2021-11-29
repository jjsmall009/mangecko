# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'card_widgetLOjbts.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_CardWidget(object):
    def setupUi(self, CardWidget):
        if not CardWidget.objectName():
            CardWidget.setObjectName(u"CardWidget")
        CardWidget.resize(150, 250)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CardWidget.sizePolicy().hasHeightForWidth())
        CardWidget.setSizePolicy(sizePolicy)
        CardWidget.setMinimumSize(QSize(150, 250))
        CardWidget.setMaximumSize(QSize(150, 250))
        CardWidget.setStyleSheet(u"")
        self.card_outer_layout = QVBoxLayout(CardWidget)
        self.card_outer_layout.setSpacing(0)
        self.card_outer_layout.setObjectName(u"card_outer_layout")
        self.card_outer_layout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(CardWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame#frame {\n"
"background-color:white;\n"
"border:1px solid grey;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QFrame#frame::hover {\n"
"border:2px solid grey;\n"
"background-color:#edf2f4;\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame_layout = QVBoxLayout(self.frame)
        self.frame_layout.setSpacing(6)
        self.frame_layout.setObjectName(u"frame_layout")
        self.frame_layout.setContentsMargins(2, 2, 2, 2)
        self.cover_label = QLabel(self.frame)
        self.cover_label.setObjectName(u"cover_label")
        self.cover_label.setScaledContents(True)
        self.cover_label.setWordWrap(True)

        self.frame_layout.addWidget(self.cover_label)

        self.series_label = QLabel(self.frame)
        self.series_label.setObjectName(u"series_label")
        self.series_label.setWordWrap(True)

        self.frame_layout.addWidget(self.series_label)

        self.volume_label = QLabel(self.frame)
        self.volume_label.setObjectName(u"volume_label")
        self.volume_label.setWordWrap(True)

        self.frame_layout.addWidget(self.volume_label)

        self.frame_layout.setStretch(0, 1)

        self.card_outer_layout.addWidget(self.frame)


        self.retranslateUi(CardWidget)

        QMetaObject.connectSlotsByName(CardWidget)
    # setupUi

    def retranslateUi(self, CardWidget):
        CardWidget.setWindowTitle(QCoreApplication.translate("CardWidget", u"Form", None))
        self.cover_label.setText("")
        self.series_label.setText(QCoreApplication.translate("CardWidget", u"Series Name", None))
        self.volume_label.setText(QCoreApplication.translate("CardWidget", u"Volume Info", None))
    # retranslateUi

