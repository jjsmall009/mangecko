# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'card_widgetYMxJPX.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

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
        self.card_layout = QVBoxLayout(CardWidget)
        self.card_layout.setObjectName(u"card_layout")
        self.cover_label = QLabel(CardWidget)
        self.cover_label.setObjectName(u"cover_label")

        self.card_layout.addWidget(self.cover_label)

        self.series_label = QLabel(CardWidget)
        self.series_label.setObjectName(u"series_label")

        self.card_layout.addWidget(self.series_label)

        self.volume_label = QLabel(CardWidget)
        self.volume_label.setObjectName(u"volume_label")

        self.card_layout.addWidget(self.volume_label)


        self.retranslateUi(CardWidget)

        QMetaObject.connectSlotsByName(CardWidget)
    # setupUi

    def retranslateUi(self, CardWidget):
        CardWidget.setWindowTitle(QCoreApplication.translate("CardWidget", u"Form", None))
        self.cover_label.setText(QCoreApplication.translate("CardWidget", u"Cover Image", None))
        self.series_label.setText(QCoreApplication.translate("CardWidget", u"Series Name", None))
        self.volume_label.setText(QCoreApplication.translate("CardWidget", u"Volume Info", None))
    # retranslateUi

