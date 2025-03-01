from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QPushButton, QListWidget
from .WhitelistDialog import WhitelistDialog

UI_FILE = "././ui/main.ui"

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app

        uic.loadUi(UI_FILE, self)  # Load the .ui file

        self.button = self.findChild(QPushButton, "appWhitelistButton")
        self.whitelistPreview = self.findChild(QListWidget, "mainWindowAppWhitelist")

        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.app.show_window("WhitelistDialog")