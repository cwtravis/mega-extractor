import json
import os
import sys
import datetime
import time
from enum import Enum

# PySide6 Imports
from PySide6.QtWidgets import QApplication, QMessageBox, QDialog, QMenu, QSystemTrayIcon, QInputDialog, QFileDialog
from PySide6.QtCore import Qt, QSettings, QFile, QTextStream, QStandardPaths, QTimer, Signal, QObject, QRunnable
from PySide6.QtGui import QPixmap, QIcon, QDesktopServices, QAction

import Resources_rc
from UI_Components import Ui_SettingsDialog, Ui_LogDialog

#Log Levels
class LogLevel(Enum):
    INFO = 0
    ERROR = 10
    DEBUG = 20
    
    @staticmethod
    def get(value):
        for level in LogLevel:
            if(value == level.value):
                return level
        return LogLevel.INFO
    
class MegaExtractor(QApplication):
    def __init__(self, args):
        super(MegaExtractor, self).__init__(args)

        # Gather App Info from version.json resource
        version_file = QFile(":version.json")
        version_file.open(QFile.ReadOnly)
        text_stream = QTextStream(version_file)
        version_file_text = text_stream.readAll()
        version_dict = json.loads(version_file_text)
        self.org_name = version_dict["company_name"]
        self.app_name = version_dict["product_name"]
        self.version = version_dict["version"]
        self.setOrganizationName(self.org_name)
        self.setApplicationName(self.app_name)
        self.setApplicationVersion(self.version)
        
        # Config Directory
        self.config_dir = QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)
        self.documents = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        if(not os.path.isdir(self.config_dir)):
            os.makedirs(self.config_dir)
        self.ini_path = os.path.join(self.config_dir, f"settings.ini").replace("\\", "/")
        print(self.ini_path)
        if os.path.isfile(self.ini_path):
            pass
        self.settings = QSettings(self.ini_path, QSettings.IniFormat)
        log_level_str = self.settings.value("MegaExtractor/LogLevel", "Unknown")
        if log_level_str.lower() == "info":
            self.log_level = LogLevel.INFO
        elif log_level_str.lower() == "error":
            self.log_level = LogLevel.ERROR
        elif log_level_str.lower() == "debug":
            self.log_level = LogLevel.DEBUG
        else:
            # No Level Set, write INFO
            self.settings.setValue("MegaExtractor/LogLevel", "INFO")
            self.log_level = LogLevel.INFO

        # Create the icon
        self.window_icon = QIcon(":resources/img/icons/excavator.png")
        self.settings_icon  = QIcon(":resources/img/icons/settings.svg")
        self.log_icon = QIcon(":resources/img/icons/file-text.svg")
        self.quit_icon  = QIcon(":resources/img/icons/log-out.svg")

        # Create the tray
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(self.window_icon)
        
        # Create the menu
        self.menu = QMenu()
        self.settings_action = QAction("Settings")
        self.settings_action.setIcon(self.settings_icon)
        self.menu.addAction(self.settings_action)
        self.menu.addSeparator()
        self.log_action = QAction("Status")
        self.log_action.setIcon(self.log_icon)
        self.menu.addAction(self.log_action)
        self.menu.addSeparator()
        
        # Add a Quit option to the menu.
        self.quit_action = QAction("Quit")
        self.quit_action.setIcon(self.quit_icon)
        self.menu.addAction(self.quit_action)

        # Signals
        self.settings_action.triggered.connect(self.settingsClicked)
        self.log_action.triggered.connect(self.statusClicked)
        self.quit_action.triggered.connect(self.quit)
        
        # Add the menu to the tray
        self.tray.setContextMenu(self.menu)

        #Start the app
        self.log_dialog = LogDialog(self.window_icon)
        self.setQuitOnLastWindowClosed(False)
        self.tray.setVisible(True)
        self.log("Starting MegaExtractor")
        self.log(f"LogLevel set to [{self.log_level}]")
        self.seven_zip_path = "C:/Program Files/7-Zip/7z.exe"
        if not os.path.exists(self.seven_zip_path):
            QMessageBox.critical(self.log_dialog, "MegaExtractor", f"No 7-Zip install found: \n{self.seven_zip_path}\nInstall 7-zip for MegaExtractor to function. \nExiting.")
            sys.exit(1)
        self.log(f"7-Zip Path Located: [{self.seven_zip_path}]")

    def settingsClicked(self):
        print("Settings Clicked")
        dialog = SettingsDialog(self.window_icon, self.settings)
        result = dialog.exec()
        if result == QDialog.Accepted:
            #Settings Saved
            self.settings = dialog.settings
            self.settings.sync()
            self.monitor_dir = self.settings.value("MegaExtractor/MonitorDirectory")
            self.output_dir = self.settings.value("MegaExtractor/OutputDirectory")
        else:
            # Save Cancelled
            pass
    
    def setStatus(self, status: str):
        self.log_dialog.status(status)

    def statusClicked(self):
        self.log_dialog.show()

    def log(self, msg, level=LogLevel.INFO):
        if(not msg or level.value > self.log_level.value):
            return
        self.log_dialog.log(msg, level)

class Extractor(QRunnable):
    class Signals(QObject):
        log = Signal(str, LogLevel)

    def __init__(self):
        super(Extractor, self).__init__()
        self.signals = self.Signals()

    def run(self):
        pass

class LogDialog(QDialog):
    class Signals(QObject):
        log = Signal(str, LogLevel)
        status = Signal(str)

    def __init__(self, icon, initial_text="", parent=None):
        super().__init__(parent)
        self.setWindowIcon(icon)
        self.ui = Ui_LogDialog()
        self.ui.setupUi(self)
        self.ui.log_browser.append(initial_text)

    def status(self, status):
        self.ui.status_label.setText(f"Status: {status}")
    
    def log(self, msg, level=LogLevel.INFO):
        if(level == LogLevel.ERROR):
            style = "color: #cc0000;"
        elif(level == LogLevel.DEBUG):
            style = "color: #006600;"
            print(msg)
        else:
            style = "color: #000000;"
        now = datetime.datetime.now()
        timestamp = now.strftime("%H:%M:%S")
        msg = f'<span style="{style}">{timestamp} - {msg}</span>'
        self.ui.log_browser.append(msg)

class SettingsDialog(QDialog):
    def __init__(self, icon: QIcon, settings: QSettings, parent=None):
        super().__init__(parent)
        self.setWindowIcon(icon)
        self.settings = settings
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
        self.ui.save_button.clicked.connect(self.saveButtonClicked)
        self.ui.monitor_dir_button.clicked.connect(self.monitorDirButtonClicked)
        self.ui.output_dir_button.clicked.connect(self.outputDirButtonClicked)
        self.ui.add_password_button.clicked.connect(self.addPasswordButtonClicked)
        self.ui.delete_password_button.clicked.connect(self.deletePasswordButtonClicked)
        self.ui.move_up_button.clicked.connect(self.moveUpButtonClicked)
        self.ui.move_down_button.clicked.connect(self.moveDownButtonClicked)
        self.ui.frequency_spinner.setValue(int(self.settings.value("MegaExtractor/CheckFrequency", "5")))
        self.ui.monitor_dir_edit.setText(self.settings.value("MegaExtractor/MonitorDirectory", ""))
        self.ui.output_dir_edit.setText(self.settings.value("MegaExtractor/OutputDirectory", ""))
        self.ui.notification_checkbox.setChecked(self.settings.value("MegaExtractor/ShowNotifications", "1")=="1")
        self.ui.delete_checkbox.setChecked(self.settings.value("MegaExtractor/DeleteArchives", "0")=="1")
        #read password list as QSettings Array
        count = self.settings.beginReadArray("Passwords")
        for i in range(count):
            self.settings.setArrayIndex(i)
            self.ui.password_list.addItem(self.settings.value("Value"))
        settings.endArray()

    def addPasswordButtonClicked(self):
        password, ok = QInputDialog.getText(self, "Add Password","Password:")
        if ok:
            self.ui.password_list.addItem(password)

    def deletePasswordButtonClicked(self):
        indexes = self.ui.password_list.selectedIndexes()
        if len(indexes) <= 0: return
        index = indexes[0]
        self.ui.password_list.takeItem(index.row())
    
    def moveUpButtonClicked(self):
        indexes = self.ui.password_list.selectedIndexes()
        if len(indexes) <= 0:
            # No Row selected 
            return
        row_a = indexes[0].row()
        if row_a <= 0: 
            # selected row is already at the top
            return 
        self.swapPasswords(row_a, row_a-1)
        self.ui.password_list.setCurrentRow(row_a-1)

    def moveDownButtonClicked(self):
        indexes = self.ui.password_list.selectedIndexes()
        if len(indexes) <= 0: 
            # No row selected
            return
        row_a = indexes[0].row()
        if row_a >= self.ui.password_list.count()-1: 
            # selected row is already at the bottom
            return 
        self.swapPasswords(row_a, row_a+1)
        self.ui.password_list.setCurrentRow(row_a+1)
    
    def swapPasswords(self, row_a, row_b):
        item_a = self.ui.password_list.item(row_a)
        item_b = self.ui.password_list.item(row_b)
        if item_a is None or item_b is None: return
        data_a = item_a.text()
        data_b = item_b.text()
        item_a.setText(data_b)
        item_b.setText(data_a)

    def monitorDirButtonClicked(self):
        default_dir = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        result = QFileDialog.getExistingDirectory(self, 
            "Choose directory to monitor.", 
            default_dir,
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        if not os.path.exists(result):
            QMessageBox.warning(self, "MegaExtractor", "Selected monitor directory doesn't exist. Try again.")
        else:
            self.ui.monitor_dir_edit.setText(result)

    def outputDirButtonClicked(self):
        default_dir = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        result = QFileDialog.getExistingDirectory(self, 
            "Choose Output Directory", 
            default_dir,
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        if not os.path.exists(result):
            QMessageBox.warning(self, "MegaExtractor", "Selected output directory doesn't exist. Try again.")
        else:
            self.ui.output_dir_edit.setText(result)

    def saveButtonClicked(self):
        monitor_dir = self.ui.monitor_dir_edit.text()
        output_dir = self.ui.output_dir_edit.text()
        frequency = self.ui.frequency_spinner.value()
        notifications = "0"
        if self.ui.notification_checkbox.isChecked():
            notifications = "1"
        delete = "0"
        if self.ui.delete_checkbox.isChecked():
            delete = "1"
        passwords = []
        for i in range(self.ui.password_list.count()):
            passwords.append(self.ui.password_list.item(i).text())
        self.settings.setValue("MegaExtractor/CheckFrequency", frequency)
        self.settings.setValue("MegaExtractor/MonitorDirectory", monitor_dir)
        self.settings.setValue("MegaExtractor/OutputDirectory", output_dir)
        self.settings.setValue("MegaExtractor/ShowNotifications", notifications)
        self.settings.setValue("MegaExtractor/DeleteArchives", delete)
        self.settings.beginWriteArray("Passwords")
        for i in range(len(passwords)):
            self.settings.setArrayIndex(i)
            self.settings.setValue("Value", passwords[i])
        self.settings.endArray()
        self.accept()
    
    def cancel_button_clicked(self):
        self.reject()

# Start the PySide6 App
if __name__ == "__main__":
    app = MegaExtractor(sys.argv)
    sys.exit(app.exec())