# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LogDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_LogDialog(object):
    def setupUi(self, LogDialog):
        if not LogDialog.objectName():
            LogDialog.setObjectName(u"LogDialog")
        LogDialog.resize(865, 516)
        self.verticalLayout_2 = QVBoxLayout(LogDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(LogDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.status_label = QLabel(self.widget_2)
        self.status_label.setObjectName(u"status_label")
        font = QFont()
        font.setPointSize(14)
        self.status_label.setFont(font)

        self.verticalLayout_3.addWidget(self.status_label)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget = QWidget(LogDialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.log_browser = QTextBrowser(self.widget)
        self.log_browser.setObjectName(u"log_browser")

        self.verticalLayout.addWidget(self.log_browser)


        self.verticalLayout_2.addWidget(self.widget)


        self.retranslateUi(LogDialog)

        QMetaObject.connectSlotsByName(LogDialog)
    # setupUi

    def retranslateUi(self, LogDialog):
        LogDialog.setWindowTitle(QCoreApplication.translate("LogDialog", u"MegaExtractor Log", None))
        self.status_label.setText(QCoreApplication.translate("LogDialog", u"Status: ", None))
        self.label.setText(QCoreApplication.translate("LogDialog", u"Log:", None))
    # retranslateUi



# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QToolButton, QVBoxLayout,
    QWidget)
import Resources_rc

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(476, 398)
        self.verticalLayout_3 = QVBoxLayout(SettingsDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_2 = QGroupBox(SettingsDialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.monitor_dir_edit = QLineEdit(self.groupBox_2)
        self.monitor_dir_edit.setObjectName(u"monitor_dir_edit")
        self.monitor_dir_edit.setReadOnly(True)

        self.gridLayout.addWidget(self.monitor_dir_edit, 0, 1, 1, 1)

        self.monitor_dir_button = QToolButton(self.groupBox_2)
        self.monitor_dir_button.setObjectName(u"monitor_dir_button")
        icon = QIcon()
        icon.addFile(u":/resources/img/icons/folder-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.monitor_dir_button.setIcon(icon)
        self.monitor_dir_button.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.monitor_dir_button, 0, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.output_dir_edit = QLineEdit(self.groupBox_2)
        self.output_dir_edit.setObjectName(u"output_dir_edit")
        self.output_dir_edit.setReadOnly(True)

        self.gridLayout.addWidget(self.output_dir_edit, 1, 1, 1, 1)

        self.output_dir_button = QToolButton(self.groupBox_2)
        self.output_dir_button.setObjectName(u"output_dir_button")
        self.output_dir_button.setIcon(icon)
        self.output_dir_button.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.output_dir_button, 1, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.widget_3 = QWidget(SettingsDialog)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.groupBox_4 = QGroupBox(self.widget_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QSize(150, 150))
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.password_list = QListWidget(self.groupBox_4)
        self.password_list.setObjectName(u"password_list")

        self.horizontalLayout_2.addWidget(self.password_list)

        self.widget_5 = QWidget(self.groupBox_4)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
        self.widget_5.setMinimumSize(QSize(100, 0))
        self.verticalLayout = QVBoxLayout(self.widget_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.add_password_button = QPushButton(self.widget_5)
        self.add_password_button.setObjectName(u"add_password_button")

        self.verticalLayout.addWidget(self.add_password_button)

        self.delete_password_button = QPushButton(self.widget_5)
        self.delete_password_button.setObjectName(u"delete_password_button")

        self.verticalLayout.addWidget(self.delete_password_button)

        self.verticalSpacer = QSpacerItem(20, 105, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.move_up_button = QPushButton(self.widget_5)
        self.move_up_button.setObjectName(u"move_up_button")

        self.verticalLayout.addWidget(self.move_up_button)

        self.move_down_button = QPushButton(self.widget_5)
        self.move_down_button.setObjectName(u"move_down_button")

        self.verticalLayout.addWidget(self.move_down_button)


        self.horizontalLayout_2.addWidget(self.widget_5)


        self.horizontalLayout_3.addWidget(self.groupBox_4)

        self.groupBox = QGroupBox(self.widget_3)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, 0)
        self.widget_4 = QWidget(self.groupBox)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 9, -1)
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.frequency_spinner = QSpinBox(self.widget_4)
        self.frequency_spinner.setObjectName(u"frequency_spinner")
        self.frequency_spinner.setMinimum(5)
        self.frequency_spinner.setMaximum(3000)
        self.frequency_spinner.setSingleStep(5)

        self.horizontalLayout.addWidget(self.frequency_spinner)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_7 = QWidget(self.groupBox)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_2 = QGridLayout(self.widget_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, -1, -1, -1)
        self.delete_checkbox = QCheckBox(self.widget_7)
        self.delete_checkbox.setObjectName(u"delete_checkbox")

        self.gridLayout_2.addWidget(self.delete_checkbox, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.groupBox)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_3 = QGridLayout(self.widget_8)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, -1, -1, -1)
        self.notification_checkbox = QCheckBox(self.widget_8)
        self.notification_checkbox.setObjectName(u"notification_checkbox")

        self.gridLayout_3.addWidget(self.notification_checkbox, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_8)

        self.verticalSpacer_2 = QSpacerItem(20, 63, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.widget_6 = QWidget(self.groupBox)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy2)
        self.widget_6.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 9, 0)
        self.horizontalSpacer_2 = QSpacerItem(54, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.save_button = QPushButton(self.widget_6)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout_4.addWidget(self.save_button)


        self.verticalLayout_2.addWidget(self.widget_6)


        self.horizontalLayout_3.addWidget(self.groupBox)


        self.verticalLayout_3.addWidget(self.widget_3)


        self.retranslateUi(SettingsDialog)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Mega Extractor Settings", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SettingsDialog", u"Directory Settings", None))
        self.label.setText(QCoreApplication.translate("SettingsDialog", u"Directory to Monitor:", None))
        self.monitor_dir_button.setText(QCoreApplication.translate("SettingsDialog", u"...", None))
        self.label_2.setText(QCoreApplication.translate("SettingsDialog", u"Output Directory:", None))
        self.output_dir_button.setText(QCoreApplication.translate("SettingsDialog", u"Output Directoryr:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("SettingsDialog", u"Password List", None))
        self.add_password_button.setText(QCoreApplication.translate("SettingsDialog", u"Add", None))
        self.delete_password_button.setText(QCoreApplication.translate("SettingsDialog", u"Delete", None))
        self.move_up_button.setText(QCoreApplication.translate("SettingsDialog", u"Move Up", None))
        self.move_down_button.setText(QCoreApplication.translate("SettingsDialog", u"Move Down", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingsDialog", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("SettingsDialog", u"Check Frequency:", None))
        self.frequency_spinner.setSuffix(QCoreApplication.translate("SettingsDialog", u"s", None))
        self.frequency_spinner.setPrefix("")
        self.delete_checkbox.setText(QCoreApplication.translate("SettingsDialog", u"Delete Archives", None))
        self.notification_checkbox.setText(QCoreApplication.translate("SettingsDialog", u"Show Notification", None))
        self.save_button.setText(QCoreApplication.translate("SettingsDialog", u"Save", None))
    # retranslateUi



