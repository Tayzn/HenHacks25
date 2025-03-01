from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QListWidget
from PyQt6.QtCore import QTimer, QTime

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("test.ui", self)
        
        # Set up a timer to update time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every 1000 ms (1 second)
        
        self.task_input = self.findChild(QLineEdit, "taskInput")
        self.add_task_button = self.findChild(QPushButton, "addTaskButton")
        self.task_list = self.findChild(QListWidget, "taskList")
        
        if self.task_list is None:
            print("Error: taskList not found in UI!")
        
        self.add_task_button.clicked.connect(self.add_task)

        # Initialize the time display
        self.update_time()
        
    def update_time(self):
        current_time = QTime.currentTime().toString("HH:mm:ss")
        self.timeLabel.setText(current_time)
        
    def add_task(self):
        task = self.task_input.text().strip()
        if task:  # Add only if task is not empty
            self.task_list.addItem(task)
            self.task_input.clear()  # Clear input after adding
        
app = QApplication([])
window = MyWindow()
window.show()
app.exec()

