# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_layoutYvVhYd.ui'
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
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(1200, 800)
        main_window.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(main_window)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.left_section = QWidget(main_window)
        self.left_section.setObjectName(u"left_section")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_section.sizePolicy().hasHeightForWidth())
        self.left_section.setSizePolicy(sizePolicy)
        self.left_section.setMinimumSize(QSize(200, 0))
        self.left_section.setMaximumSize(QSize(200, 16777215))
        self.left_section.setStyleSheet(u"QWidget{\n"
"background-color:#2a2d31;\n"
"color:#faf9f9;\n"
"}\n"
"\n"
"QPushButton {\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton#add_library_btn::hover {\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#settings_btn::hover {\n"
"font-weight: bold;\n"
"}")
        self.left_section_layout = QVBoxLayout(self.left_section)
        self.left_section_layout.setObjectName(u"left_section_layout")
        self.logo_label = QLabel(self.left_section)
        self.logo_label.setObjectName(u"logo_label")
        font = QFont()
        font.setFamilies([u"Impact"])
        font.setPointSize(20)
        self.logo_label.setFont(font)
        self.logo_label.setStyleSheet(u"")
        self.logo_label.setAlignment(Qt.AlignCenter)

        self.left_section_layout.addWidget(self.logo_label)

        self.libraries_list_label = QLabel(self.left_section)
        self.libraries_list_label.setObjectName(u"libraries_list_label")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semilight"])
        font1.setPointSize(12)
        self.libraries_list_label.setFont(font1)
        self.libraries_list_label.setStyleSheet(u"margin-top:10px;")

        self.left_section_layout.addWidget(self.libraries_list_label)

        self.libraries_list_widget = QListWidget(self.left_section)
        self.libraries_list_widget.setObjectName(u"libraries_list_widget")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        self.libraries_list_widget.setFont(font2)
        self.libraries_list_widget.setStyleSheet(u"")
        self.libraries_list_widget.setFrameShape(QFrame.Box)
        self.libraries_list_widget.setFrameShadow(QFrame.Sunken)
        self.libraries_list_widget.setLineWidth(1)

        self.left_section_layout.addWidget(self.libraries_list_widget)

        self.add_lib_layout = QHBoxLayout()
        self.add_lib_layout.setObjectName(u"add_lib_layout")
        self.add_lib_layout.setContentsMargins(2, -1, -1, -1)
        self.add_library_btn = QPushButton(self.left_section)
        self.add_library_btn.setObjectName(u"add_library_btn")
        self.add_library_btn.setFont(font1)
        self.add_library_btn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"../../../resources/icons/add-128.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_library_btn.setIcon(icon)

        self.add_lib_layout.addWidget(self.add_library_btn)

        self.add_lib_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.add_lib_layout.addItem(self.add_lib_spacer)


        self.left_section_layout.addLayout(self.add_lib_layout)

        self.divider = QFrame(self.left_section)
        self.divider.setObjectName(u"divider")
        self.divider.setStyleSheet(u"")
        self.divider.setFrameShadow(QFrame.Plain)
        self.divider.setLineWidth(1)
        self.divider.setFrameShape(QFrame.HLine)

        self.left_section_layout.addWidget(self.divider)

        self.settings_layout = QHBoxLayout()
        self.settings_layout.setObjectName(u"settings_layout")
        self.settings_layout.setContentsMargins(2, -1, -1, -1)
        self.settings_btn = QPushButton(self.left_section)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setFont(font1)
        self.settings_btn.setStyleSheet(u"color:#f48c06;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../../../resources/icons/settings-4-128.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_btn.setIcon(icon1)

        self.settings_layout.addWidget(self.settings_btn)

        self.settings_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.settings_layout.addItem(self.settings_spacer)


        self.left_section_layout.addLayout(self.settings_layout)


        self.horizontalLayout_3.addWidget(self.left_section)

        self.right_section = QVBoxLayout()
        self.right_section.setObjectName(u"right_section")
        self.library_upper_wrapper = QWidget(main_window)
        self.library_upper_wrapper.setObjectName(u"library_upper_wrapper")
        sizePolicy.setHeightForWidth(self.library_upper_wrapper.sizePolicy().hasHeightForWidth())
        self.library_upper_wrapper.setSizePolicy(sizePolicy)
        self.library_upper_wrapper.setMinimumSize(QSize(0, 50))
        self.library_upper_wrapper.setMaximumSize(QSize(16777215, 50))
        self.library_upper_wrapper.setStyleSheet(u"QWidget{\n"
"background-color:#33373d;\n"
"}\n"
"\n"
"QLabel {\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color:#f8f9fa;\n"
"color:#f48c06;\n"
"border:2px solid black;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"border:2px solid grey;\n"
"}")
        self.library_upper_layout = QHBoxLayout(self.library_upper_wrapper)
        self.library_upper_layout.setObjectName(u"library_upper_layout")
        self.library_upper_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.current_library_label = QLabel(self.library_upper_wrapper)
        self.current_library_label.setObjectName(u"current_library_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.current_library_label.sizePolicy().hasHeightForWidth())
        self.current_library_label.setSizePolicy(sizePolicy1)
        self.current_library_label.setMinimumSize(QSize(200, 0))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Semibold"])
        font3.setPointSize(12)
        self.current_library_label.setFont(font3)
        self.current_library_label.setAlignment(Qt.AlignCenter)
        self.current_library_label.setMargin(0)

        self.library_upper_layout.addWidget(self.current_library_label)

        self.current_library_buttons_layout = QHBoxLayout()
        self.current_library_buttons_layout.setObjectName(u"current_library_buttons_layout")
        self.current_library_buttons_layout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.current_library_buttons_layout.addItem(self.horizontalSpacer)

        self.scan_library_btn = QPushButton(self.library_upper_wrapper)
        self.scan_library_btn.setObjectName(u"scan_library_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scan_library_btn.sizePolicy().hasHeightForWidth())
        self.scan_library_btn.setSizePolicy(sizePolicy2)
        self.scan_library_btn.setMinimumSize(QSize(125, 0))
        self.scan_library_btn.setMaximumSize(QSize(125, 16777215))
        self.scan_library_btn.setFont(font3)
        self.scan_library_btn.setFlat(False)

        self.current_library_buttons_layout.addWidget(self.scan_library_btn)

        self.update_library_btn = QPushButton(self.library_upper_wrapper)
        self.update_library_btn.setObjectName(u"update_library_btn")
        sizePolicy2.setHeightForWidth(self.update_library_btn.sizePolicy().hasHeightForWidth())
        self.update_library_btn.setSizePolicy(sizePolicy2)
        self.update_library_btn.setMinimumSize(QSize(125, 0))
        self.update_library_btn.setMaximumSize(QSize(125, 16777215))
        self.update_library_btn.setFont(font3)

        self.current_library_buttons_layout.addWidget(self.update_library_btn)

        self.new_volumes_btn = QPushButton(self.library_upper_wrapper)
        self.new_volumes_btn.setObjectName(u"new_volumes_btn")
        sizePolicy2.setHeightForWidth(self.new_volumes_btn.sizePolicy().hasHeightForWidth())
        self.new_volumes_btn.setSizePolicy(sizePolicy2)
        self.new_volumes_btn.setMinimumSize(QSize(125, 0))
        self.new_volumes_btn.setMaximumSize(QSize(125, 16777215))
        self.new_volumes_btn.setFont(font3)

        self.current_library_buttons_layout.addWidget(self.new_volumes_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.current_library_buttons_layout.addItem(self.horizontalSpacer_2)


        self.library_upper_layout.addLayout(self.current_library_buttons_layout)


        self.right_section.addWidget(self.library_upper_wrapper)

        self.series_scroll_area = QScrollArea(main_window)
        self.series_scroll_area.setObjectName(u"series_scroll_area")
        self.series_scroll_area.setFrameShape(QFrame.NoFrame)
        self.series_scroll_area.setFrameShadow(QFrame.Raised)
        self.series_scroll_area.setWidgetResizable(True)
        self.series_grid_wrapper = QWidget()
        self.series_grid_wrapper.setObjectName(u"series_grid_wrapper")
        self.series_grid_wrapper.setGeometry(QRect(0, 0, 998, 742))
        self.series_wrapper_layout_useless = QHBoxLayout(self.series_grid_wrapper)
        self.series_wrapper_layout_useless.setObjectName(u"series_wrapper_layout_useless")
        self.series_wrapper_layout_useless.setContentsMargins(0, 6, 0, 6)
        self.series_grid_layout = QGridLayout()
        self.series_grid_layout.setSpacing(10)
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
        self.current_library_label.setText("")
        self.scan_library_btn.setText(QCoreApplication.translate("main_window", u"Scan Library", None))
        self.update_library_btn.setText(QCoreApplication.translate("main_window", u"Update Library", None))
        self.new_volumes_btn.setText(QCoreApplication.translate("main_window", u"New Volumes", None))
    # retranslateUi

