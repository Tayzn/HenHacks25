from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QPushButton, QTextEdit, QListWidget, QListWidgetItem
from PyQt6.QtCore import Qt
import pywinctl as pywin
import psutil

UI_FILE = "././ui/whitelist.ui"

class WhitelistDialog(QDialog):
    def __init__(self, app):
        super().__init__()
        self.app = app

        uic.loadUi(UI_FILE, self)  # Load the .ui file

        self.button = self.findChild(QPushButton, "appWhitelistSubmit")  # Find a widget by its object name
        self.listWidget: QListWidget = self.findChild(QListWidget, "appWhitelistList")

        self.button.clicked.connect(self.on_button_click)

    def showEvent(self, a0):
        self.load_apps()
        current_whitelist = self.app.get_app_task("WindowTracker").whitelistedApps
        for idx in range(self.listWidget.count()):
            item = self.listWidget.item(idx)
            text = item.text()
            text = text.split(" - ")[0]
            if text in current_whitelist:
                item.setCheckState(Qt.CheckState.Checked)

        return super().showEvent(a0)

    def load_apps(self):
        self.listWidget.clear()
        existing = set()
        for window in pywin.getAllWindows():
            pid = window.getPID()
            name = psutil.Process(pid).name()
            if name in existing: continue
            existing.add(name)

            display = name
            if window.title:
                display = f"{name} - {window.title}"

            new_item = QListWidgetItem(display)
            new_item.setCheckState(Qt.CheckState.Unchecked)

            self.listWidget.addItem(new_item)


    def on_button_click(self):
        checked_apps = []
        for idx in range(self.listWidget.count()):
            item = self.listWidget.item(idx)
            if item.checkState() == Qt.CheckState.Checked:
                text = item.text()
                text = text.split(" - ")[0]
                checked_apps.append(text)
        self.app.get_app_task("WindowTracker").update_whitelist(checked_apps)
        self.hide()

    def text_changed(self):
        print(self.textWindow.toPlainText())