# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_layoutJYIBYz.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QListWidget, QListWidgetItem,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(1200, 800)
        main_window.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(main_window)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.left_section = QWidget(main_window)
        self.left_section.setObjectName(u"left_section")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_section.sizePolicy().hasHeightForWidth())
        self.left_section.setSizePolicy(sizePolicy)
        self.left_section.setMinimumSize(QSize(200, 0))
        self.left_section.setMaximumSize(QSize(200, 16777215))
        self.left_section.setStyleSheet(u"")
        self.left_section_layout = QVBoxLayout(self.left_section)
        self.left_section_layout.setObjectName(u"left_section_layout")
        self.logo_label = QLabel(self.left_section)
        self.logo_label.setObjectName(u"logo_label")
        font = QFont()
        font.setPointSize(20)
        self.logo_label.setFont(font)
        self.logo_label.setStyleSheet(u"")
        self.logo_label.setAlignment(Qt.AlignCenter)

        self.left_section_layout.addWidget(self.logo_label)

        self.libraries_list_label = QLabel(self.left_section)
        self.libraries_list_label.setObjectName(u"libraries_list_label")
        self.libraries_list_label.setStyleSheet(u"margin-top:10px;")

        self.left_section_layout.addWidget(self.libraries_list_label)

        self.libraries_list_widget = QListWidget(self.left_section)
        self.libraries_list_widget.setObjectName(u"libraries_list_widget")
        self.libraries_list_widget.setStyleSheet(u"")

        self.left_section_layout.addWidget(self.libraries_list_widget)

        self.add_library_btn = QPushButton(self.left_section)
        self.add_library_btn.setObjectName(u"add_library_btn")
        self.add_library_btn.setStyleSheet(u"")

        self.left_section_layout.addWidget(self.add_library_btn)

        self.divider = QFrame(self.left_section)
        self.divider.setObjectName(u"divider")
        self.divider.setStyleSheet(u"")
        self.divider.setFrameShadow(QFrame.Plain)
        self.divider.setLineWidth(2)
        self.divider.setFrameShape(QFrame.HLine)

        self.left_section_layout.addWidget(self.divider)

        self.settings_btn = QPushButton(self.left_section)
        self.settings_btn.setObjectName(u"settings_btn")

        self.left_section_layout.addWidget(self.settings_btn)


        self.horizontalLayout_3.addWidget(self.left_section)

        self.right_section = QVBoxLayout()
        self.right_section.setObjectName(u"right_section")
        self.library_upper_wrapper = QWidget(main_window)
        self.library_upper_wrapper.setObjectName(u"library_upper_wrapper")
        self.library_upper_wrapper.setMinimumSize(QSize(0, 50))
        self.library_upper_wrapper.setMaximumSize(QSize(16777215, 50))
        self.library_upper_wrapper.setStyleSheet(u"")
        self.library_upper_layout = QHBoxLayout(self.library_upper_wrapper)
        self.library_upper_layout.setObjectName(u"library_upper_layout")
        self.library_upper_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.current_library_label = QLabel(self.library_upper_wrapper)
        self.current_library_label.setObjectName(u"current_library_label")
        sizePolicy.setHeightForWidth(self.current_library_label.sizePolicy().hasHeightForWidth())
        self.current_library_label.setSizePolicy(sizePolicy)
        self.current_library_label.setMinimumSize(QSize(200, 0))
        self.current_library_label.setAlignment(Qt.AlignCenter)
        self.current_library_label.setMargin(0)

        self.library_upper_layout.addWidget(self.current_library_label)

        self.current_library_buttons_layout = QHBoxLayout()
        self.current_library_buttons_layout.setObjectName(u"current_library_buttons_layout")
        self.current_library_buttons_layout.setContentsMargins(-1, -1, 0, -1)
        self.scan_library_btn = QPushButton(self.library_upper_wrapper)
        self.scan_library_btn.setObjectName(u"scan_library_btn")
        self.scan_library_btn.setMaximumSize(QSize(100, 16777215))

        self.current_library_buttons_layout.addWidget(self.scan_library_btn)

        self.update_library_btn = QPushButton(self.library_upper_wrapper)
        self.update_library_btn.setObjectName(u"update_library_btn")
        self.update_library_btn.setMaximumSize(QSize(100, 16777215))

        self.current_library_buttons_layout.addWidget(self.update_library_btn)

        self.new_volumes_btn = QPushButton(self.library_upper_wrapper)
        self.new_volumes_btn.setObjectName(u"new_volumes_btn")
        self.new_volumes_btn.setMinimumSize(QSize(0, 0))
        self.new_volumes_btn.setMaximumSize(QSize(100, 16777215))

        self.current_library_buttons_layout.addWidget(self.new_volumes_btn)


        self.library_upper_layout.addLayout(self.current_library_buttons_layout)


        self.right_section.addWidget(self.library_upper_wrapper)

        self.series_scroll_area = QScrollArea(main_window)
        self.series_scroll_area.setObjectName(u"series_scroll_area")
        self.series_scroll_area.setWidgetResizable(True)
        self.series_grid_wrapper = QWidget()
        self.series_grid_wrapper.setObjectName(u"series_grid_wrapper")
        self.series_grid_wrapper.setGeometry(QRect(0, 0, 972, 722))
        self.series_wrapper_layout_useless = QHBoxLayout(self.series_grid_wrapper)
        self.series_wrapper_layout_useless.setObjectName(u"series_wrapper_layout_useless")
        self.series_wrapper_layout_useless.setContentsMargins(0, 0, 0, 0)
        self.series_grid_layout = QGridLayout()
        self.series_grid_layout.setObjectName(u"series_grid_layout")

        self.series_wrapper_layout_useless.addLayout(self.series_grid_layout)

        self.series_scroll_area.setWidget(self.series_grid_wrapper)

        self.right_section.addWidget(self.series_scroll_area)


        self.horizontalLayout_3.addLayout(self.right_section)


        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"Manga Manager", None))
        self.logo_label.setText(QCoreApplication.translate("main_window", u"Manga Manager", None))
        self.libraries_list_label.setText(QCoreApplication.translate("main_window", u"Libraries", None))
        self.add_library_btn.setText(QCoreApplication.translate("main_window", u"Add Library", None))
        self.settings_btn.setText(QCoreApplication.translate("main_window", u"Settings", None))
        self.current_library_label.setText(QCoreApplication.translate("main_window", u"Library Name", None))
        self.scan_library_btn.setText(QCoreApplication.translate("main_window", u"Scan Library", None))
        self.update_library_btn.setText(QCoreApplication.translate("main_window", u"Update Library", None))
        self.new_volumes_btn.setText(QCoreApplication.translate("main_window", u"New Volumes", None))
    # retranslateUi

