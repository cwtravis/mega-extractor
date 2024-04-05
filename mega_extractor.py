import json
import os
import sys
import datetime
import time

# PySide6 Imports
from PySide6.QtWidgets import QApplication, QMessageBox, QDialog, QMenu, QSystemTrayIcon, QInputDialog
from PySide6.QtCore import Qt, QSettings, QFile, QTextStream, QStandardPaths, QTimer
from PySide6.QtGui import QPixmap, QIcon, QDesktopServices, QAction

import Resources_rc
from UI_Components import Ui_SettingsDialog

class SettingsDialog(QDialog):

    def __init__(self, icon, settings, parent=None):
        super().__init__(parent)
        self.settings = {}
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
        self.ui.save_button.clicked.connect(self.saveButtonClicked)
        self.ui.monitor_dir_button.clicked.connect(self.monitorDirButtonClicked)
        self.ui.output_dir_button.clicked.connect(self.outputDirButtonClicked)
        self.ui.add_password_button.clicked.connect(self.addPasswordButtonClicked)
        self.ui.delete_password_button.clicked.connect(self.deletePasswordButtonClicked)
        self.ui.frequency_spinner.setValue(int(settings.get("CheckFrequency", 0)))
        self.ui.monitor_dir_edit.setText(settings.get("MonitorDirectory", ""))
        self.ui.output_dir_edit.setText(settings.get("OutputDirectory", ""))
        self.ui.notification_checkbox.setChecked(settings.get("ShowNotifications", "1")=="1")
        self.ui.notification_checkbox.setChecked(settings.get("DeleteArchives", "0")=="1")
        if "passwords" in settings.keys():
            for password in settings["passwords"]:
                self.ui.password_list.addItem(password)

        self.setWindowIcon(icon)

    def addPasswordButtonClicked(self):
        password, ok = QInputDialog.getText(self, "Add Password","Password:")
        if ok:
            self.ui.password_list.addItem(password)

    def deletePasswordButtonClicked(self):
        indexes = self.ui.password_list.selectedIndexes()
        if len(indexes) <= 0: return
        index = indexes[0]
        self.ui.password_list.takeItem(index.row())
    
    def monitorDirButtonClicked(self):
        pass

    def outputDirButtonClicked(self):
        pass

    def saveButtonClicked(self):
        self.accept()
    
    def cancel_button_clicked(self):
        self.reject()

def settingsClicked(icon, settings):
    print("Settings Clicked")
    dialog = SettingsDialog(icon, settings)
    result = dialog.exec()
    print(f"Settings Result: {result}")

# Start the PySide6 App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    version_file = QFile(":version.json")
    version_file.open(QFile.ReadOnly)
    text_stream = QTextStream(version_file)
    version_file_text = text_stream.readAll()
    version_dict = json.loads(version_file_text)
    org_name = version_dict["company_name"]
    app_name = version_dict["product_name"]
    version = version_dict["version"]
    app.setOrganizationName(org_name)
    app.setApplicationName(app_name)
    app.setApplicationVersion(version)
    app.setQuitOnLastWindowClosed(False)
    
    # Config Directory
    config_dir = QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)
    documents = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
    if(not os.path.isdir(config_dir)):
        os.makedirs(config_dir)
    ini_path = os.path.join(config_dir, f"settings.ini").replace("\\", "/")
    print(ini_path)
    if os.path.isfile(ini_path):
        pass
    settings = QSettings(ini_path, QSettings.IniFormat)

    # Create the icon
    window_icon = QIcon(":resources/img/icons/excavator.png")
    settings_icon  = QIcon(":resources/img/icons/settings.svg")
    quit_icon  = QIcon(":resources/img/icons/log-out.svg")

    # Create the tray
    tray = QSystemTrayIcon()
    tray.setIcon(window_icon)
    tray.setVisible(True)

    # Create the menu
    menu = QMenu()
    settings_action = QAction("Settings")
    settings_action.setIcon(settings_icon)
    menu.addAction(settings_action)
    menu.addSeparator()

    settings_action.triggered.connect(lambda: settingsClicked(window_icon, {}))

    # Add a Quit option to the menu.
    quit = QAction("Quit")
    quit.setIcon(quit_icon)
    quit.triggered.connect(app.quit)
    menu.addAction(quit)

    # Add the menu to the tray
    tray.setContextMenu(menu)

    sys.exit(app.exec())