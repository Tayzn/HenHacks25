from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QTimer, QTime

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("test.ui", self)
        
        # Set up a timer to update time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every 1000 ms (1 second)

        # Initialize the time display
        self.update_time()
        
    def update_time(self):
        current_time = QTime.currentTime().toString("HH:mm:ss")
        self.timeLabel.setText(current_time)
        
app = QApplication([])
window = MyWindow()
window.show()
app.exec()

