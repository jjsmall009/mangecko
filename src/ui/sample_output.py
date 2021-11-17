# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout 3CRJWuY.ui'
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
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(1200, 800)
        main_window.setStyleSheet(u"")
        self.main_window_layout = QHBoxLayout(main_window)
        self.main_window_layout.setSpacing(0)
        self.main_window_layout.setObjectName(u"main_window_layout")
        self.main_window_layout.setContentsMargins(0, 0, 0, 0)
        self.left_section_wrapper = QWidget(main_window)
        self.left_section_wrapper.setObjectName(u"left_section_wrapper")
        self.left_section_wrapper.setMaximumSize(QSize(200, 16777215))
        self.left_section_wrapper.setStyleSheet(u"background-color:#213447;color:white;")
        self.left_outer_layout = QVBoxLayout(self.left_section_wrapper)
        self.left_outer_layout.setObjectName(u"left_outer_layout")
        self.left_outer_layout.setContentsMargins(9, 9, 9, 9)
        self.logo_label = QLabel(self.left_section_wrapper)
        self.logo_label.setObjectName(u"logo_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_label.sizePolicy().hasHeightForWidth())
        self.logo_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Impact"])
        font.setPointSize(20)
        self.logo_label.setFont(font)
        self.logo_label.setStyleSheet(u"border-top:2px solid white; border-bottom:2px solid white;")
        self.logo_label.setAlignment(Qt.AlignCenter)

        self.left_outer_layout.addWidget(self.logo_label)

        self.libraries_list_header = QLabel(self.left_section_wrapper)
        self.libraries_list_header.setObjectName(u"libraries_list_header")
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(12)
        self.libraries_list_header.setFont(font1)

        self.left_outer_layout.addWidget(self.libraries_list_header)

        self.libraries_list = QListWidget(self.left_section_wrapper)
        QListWidgetItem(self.libraries_list)
        QListWidgetItem(self.libraries_list)
        QListWidgetItem(self.libraries_list)
        QListWidgetItem(self.libraries_list)
        self.libraries_list.setObjectName(u"libraries_list")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.libraries_list.sizePolicy().hasHeightForWidth())
        self.libraries_list.setSizePolicy(sizePolicy1)
        self.libraries_list.setStyleSheet(u"border-style:none;")

        self.left_outer_layout.addWidget(self.libraries_list)

        self.add_library_layout = QHBoxLayout()
        self.add_library_layout.setSpacing(6)
        self.add_library_layout.setObjectName(u"add_library_layout")
        self.add_library_icon = QLabel(self.left_section_wrapper)
        self.add_library_icon.setObjectName(u"add_library_icon")

        self.add_library_layout.addWidget(self.add_library_icon)

        self.add_library_btn = QPushButton(self.left_section_wrapper)
        self.add_library_btn.setObjectName(u"add_library_btn")
        self.add_library_btn.setFont(font1)

        self.add_library_layout.addWidget(self.add_library_btn)


        self.left_outer_layout.addLayout(self.add_library_layout)

        self.divider_1 = QFrame(self.left_section_wrapper)
        self.divider_1.setObjectName(u"divider_1")
        self.divider_1.setFrameShadow(QFrame.Plain)
        self.divider_1.setLineWidth(2)
        self.divider_1.setFrameShape(QFrame.HLine)

        self.left_outer_layout.addWidget(self.divider_1)

        self.settings_layout = QHBoxLayout()
        self.settings_layout.setObjectName(u"settings_layout")
        self.settings_icon = QLabel(self.left_section_wrapper)
        self.settings_icon.setObjectName(u"settings_icon")

        self.settings_layout.addWidget(self.settings_icon)

        self.settings_btn = QPushButton(self.left_section_wrapper)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setFont(font1)
        self.settings_btn.setStyleSheet(u"color:orange;")

        self.settings_layout.addWidget(self.settings_btn)


        self.left_outer_layout.addLayout(self.settings_layout)


        self.main_window_layout.addWidget(self.left_section_wrapper)

        self.right_section_wrapper = QWidget(main_window)
        self.right_section_wrapper.setObjectName(u"right_section_wrapper")
        self.verticalLayout = QVBoxLayout(self.right_section_wrapper)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_action_header = QWidget(self.right_section_wrapper)
        self.left_action_header.setObjectName(u"left_action_header")
        sizePolicy.setHeightForWidth(self.left_action_header.sizePolicy().hasHeightForWidth())
        self.left_action_header.setSizePolicy(sizePolicy)
        self.left_action_header.setMaximumSize(QSize(16777215, 50))
        self.left_action_header.setStyleSheet(u"background-color:#18263d; color:white;")
        self.horizontalLayout_2 = QHBoxLayout(self.left_action_header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.library_name_label = QLabel(self.left_action_header)
        self.library_name_label.setObjectName(u"library_name_label")
        self.library_name_label.setFont(font1)
        self.library_name_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.library_name_label)

        self.library_button_layout = QHBoxLayout()
        self.library_button_layout.setObjectName(u"library_button_layout")
        self.scan_library_btn = QPushButton(self.left_action_header)
        self.scan_library_btn.setObjectName(u"scan_library_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scan_library_btn.sizePolicy().hasHeightForWidth())
        self.scan_library_btn.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setBold(True)
        self.scan_library_btn.setFont(font2)
        self.scan_library_btn.setStyleSheet(u"background-color:#f5f4f4; color:#dd7560;border-radius:3px;")

        self.library_button_layout.addWidget(self.scan_library_btn)

        self.update_library_btn = QPushButton(self.left_action_header)
        self.update_library_btn.setObjectName(u"update_library_btn")
        sizePolicy2.setHeightForWidth(self.update_library_btn.sizePolicy().hasHeightForWidth())
        self.update_library_btn.setSizePolicy(sizePolicy2)
        self.update_library_btn.setFont(font2)
        self.update_library_btn.setStyleSheet(u"background-color:#f5f4f4; color:#dd7560;border-radius:3px;")

        self.library_button_layout.addWidget(self.update_library_btn)

        self.new_volumes_btn = QPushButton(self.left_action_header)
        self.new_volumes_btn.setObjectName(u"new_volumes_btn")
        sizePolicy2.setHeightForWidth(self.new_volumes_btn.sizePolicy().hasHeightForWidth())
        self.new_volumes_btn.setSizePolicy(sizePolicy2)
        self.new_volumes_btn.setFont(font2)
        self.new_volumes_btn.setStyleSheet(u"background-color:#f5f4f4; color:#dd7560;border-radius:3px;")

        self.library_button_layout.addWidget(self.new_volumes_btn)


        self.horizontalLayout_2.addLayout(self.library_button_layout)

        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.left_action_header)

        self.series_grid = QGridLayout()
        self.series_grid.setObjectName(u"series_grid")
        self.widget = QWidget(self.right_section_wrapper)
        self.widget.setObjectName(u"widget")

        self.series_grid.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.right_section_wrapper)
        self.widget_2.setObjectName(u"widget_2")

        self.series_grid.addWidget(self.widget_2, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.right_section_wrapper)
        self.widget_3.setObjectName(u"widget_3")

        self.series_grid.addWidget(self.widget_3, 0, 2, 1, 1)

        self.widget_4 = QWidget(self.right_section_wrapper)
        self.widget_4.setObjectName(u"widget_4")

        self.series_grid.addWidget(self.widget_4, 1, 0, 1, 1)

        self.widget_5 = QWidget(self.right_section_wrapper)
        self.widget_5.setObjectName(u"widget_5")

        self.series_grid.addWidget(self.widget_5, 1, 1, 1, 1)

        self.widget_6 = QWidget(self.right_section_wrapper)
        self.widget_6.setObjectName(u"widget_6")

        self.series_grid.addWidget(self.widget_6, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.series_grid)


        self.main_window_layout.addWidget(self.right_section_wrapper)


        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"Manga Manager 1.0", None))
        self.logo_label.setText(QCoreApplication.translate("main_window", u"Manga Manager", None))
        self.libraries_list_header.setText(QCoreApplication.translate("main_window", u"Libraries", None))

        __sortingEnabled = self.libraries_list.isSortingEnabled()
        self.libraries_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.libraries_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("main_window", u"\u25cb Ongoing", None));
        ___qlistwidgetitem1 = self.libraries_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("main_window", u"\u25cb Completed", None));
        ___qlistwidgetitem2 = self.libraries_list.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("main_window", u"\u25cb Short Series", None));
        ___qlistwidgetitem3 = self.libraries_list.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("main_window", u"\u25cb Favorites", None));
        self.libraries_list.setSortingEnabled(__sortingEnabled)

        self.add_library_icon.setText(QCoreApplication.translate("main_window", u"+", None))
        self.add_library_btn.setText(QCoreApplication.translate("main_window", u"Add Library", None))
        self.settings_icon.setText(QCoreApplication.translate("main_window", u"+", None))
        self.settings_btn.setText(QCoreApplication.translate("main_window", u"Settings", None))
        self.library_name_label.setText(QCoreApplication.translate("main_window", u"< Library Name >", None))
        self.scan_library_btn.setText(QCoreApplication.translate("main_window", u"Scan Library", None))
        self.update_library_btn.setText(QCoreApplication.translate("main_window", u"Update Library", None))
        self.new_volumes_btn.setText(QCoreApplication.translate("main_window", u"New Volumes", None))
    # retranslateUi

