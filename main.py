from PyQt6.QtWidgets import QApplication
from windows.ExampleWindow import ExampleWindow
from modules import polling

pollingThread = polling.PollingThread()

app = QApplication([])
window = ExampleWindow()
window.show()
pollingThread.start()
app.exec()