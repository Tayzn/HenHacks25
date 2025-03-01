from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QPushButton, QTextEdit

UI_FILE = "././ui/example.ui"

class ExampleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_FILE, self)  # Load the .ui file

        self.button = self.findChild(QPushButton, "pushButton")  # Find a widget by its object name
        self.textWindow: QTextEdit = self.findChild(QTextEdit, "textEdit")

        self.button.clicked.connect(self.on_button_click)
        self.textWindow.textChanged.connect(self.text_changed)

    def on_button_click(self):
        print(self.textWindow.toPlainText())

    def text_changed(self):
        print(self.textWindow.toPlainText())