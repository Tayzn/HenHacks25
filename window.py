from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QListWidget, QListWidgetItem
from PyQt6.QtCore import QTimer, QTime
from PyQt6.QtCore import Qt


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
        
        self.clear_checked_button = self.findChild(QPushButton, "clearCheckedButton")
        
        if self.task_list is None:
            print("Error: taskList not found in UI!")
        
        self.add_task_button.clicked.connect(self.add_task)
        self.clear_checked_button.clicked.connect(self.clear_checked_tasks)

        # Initialize the time display
        self.update_time()
        
    def update_time(self):
        current_time = QTime.currentTime().toString("HH:mm:ss")
        self.timeLabel.setText(current_time)
        
    def add_task(self):
        """Add a new task to the to-do list with a checkbox."""
        task = self.task_input.text().strip()
        if task:  # Ensure it's not empty
            item = QListWidgetItem(task)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)  # Enable checkbox
            item.setCheckState(Qt.CheckState.Unchecked)  # Default: unchecked
            self.task_list.addItem(item)
            self.task_input.clear()  # Clear input after adding
            
    def clear_checked_tasks(self):
        """Remove checked tasks from the list."""
        for i in range(self.task_list.count() - 1, -1, -1):  # Loop in reverse
            item = self.task_list.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                self.task_list.takeItem(i)  # Remove checked item
        
app = QApplication([])
window = MyWindow()
window.show()
app.exec()

