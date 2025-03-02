import psutil
import pywinctl as pywin
from PyQt6 import uic
from PyQt6.QtCore import QFileInfo, Qt, QTime
from PyQt6.QtWidgets import QDialog, QLineEdit, QPushButton, QTimeEdit

UI_FILE = "././ui/reminder.ui"


class ReminderDialog(QDialog):
    def __init__(self, app):
        super().__init__()
        self.app = app

        uic.loadUi(UI_FILE, self)  # Load the .ui file

        self.button = self.findChild(
            QPushButton, "reminderSubmit"
        )  # Find a widget by its object name
        self.time = self.findChild(QTimeEdit, "reminderTime")
        self.input = self.findChild(QLineEdit, "reminderInput")

        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        time = self.time.time()
        text = self.input.text()

        if text:
            self.time.setTime(QTime.fromString("12:00 am", "hh:mm a"))
            self.input.setText("")

            self.app.get_window("MainWindow").add_reminder(text, time)
            self.accept()
