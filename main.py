from PyQt6.QtWidgets import QApplication
from windows.ExampleWindow import ExampleWindow

app = QApplication([])
window = ExampleWindow()
window.show()
app.exec()