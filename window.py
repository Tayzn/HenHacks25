from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QListWidget, QLineEdit, 
    QListWidgetItem, QSystemTrayIcon, QMenu
)
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QTimer, QTime, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("test.ui", self)

        # Resize window
        self.resize(800, 600)
        self.move_to_bottom_right()  # Move window to bottom-right

        # Find UI elements
        self.time_label = self.findChild(QLabel, "timeLabel")
        
        self.task_input = self.findChild(QLineEdit, "taskInput")
        self.add_task_button = self.findChild(QPushButton, "addTaskButton")
        self.task_list = self.findChild(QListWidget, "taskList")
        self.clear_checked_button = self.findChild(QPushButton, "clearCheckedButton")
        
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.Type.InBounce)
        
        if self.task_list is None:
            print("Error: taskList not found in UI!")
        if self.time_label is None:
            print("Error: timeLabel not found in UI!")
        if self.add_task_button is None:
            print("Error: addTaskButton not found in UI!")
        if self.task_list is None:
            print("Error: taskList not found in UI!")
        if self.clear_checked_button is None:
            print("Error: clearCheckedButton not found in UI!")

        # Connect buttons
        self.add_task_button.clicked.connect(self.add_task)
        self.clear_checked_button.clicked.connect(self.clear_checked_tasks)

        # Set up a timer to update time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second
        self.update_time()  # Initialize the time display

        # Set up system tray icon
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("Tomato-Whole-Red-1-Clip-Art.png"))  # Set an icon (replace with a real file)
        self.tray_icon.setToolTip("PomKit")

        # Create tray menu
        self.tray_menu = QMenu()

        show_action = QAction("Show", self)
        show_action.triggered.connect(self.show_window)
        self.tray_menu.addAction(show_action)

        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(self.close_app)
        self.tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.activated.connect(self.tray_icon_clicked)

        self.tray_icon.show()  # Show tray icon

    def update_time(self):
        """Update the clock display."""
        current_time = QTime.currentTime().toString("HH:mm:ss")
        self.time_label.setText(current_time)

    def add_task(self):
        """Add a new task to the to-do list with a checkbox."""
        task = self.task_input.text().strip()
        if task:
            item = QListWidgetItem(task)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.task_list.addItem(item)
            self.task_input.clear()

    def clear_checked_tasks(self):
        """Remove checked tasks from the list."""
        for i in range(self.task_list.count() - 1, -1, -1):
            item = self.task_list.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                self.task_list.takeItem(i)

    def closeEvent(self, event):
        """Override the close event to hide the window instead of quitting."""
        event.ignore()
        self.hide()
        self.tray_icon.showMessage("To-Do List", "App minimized to tray", QSystemTrayIcon.MessageIcon.Information, 2000)

    def show_window(self):
        """Restore the window from the tray."""
        self.showNormal()
        self.activateWindow()

    def close_app(self):
        """Quit the application."""
        self.tray_icon.hide()
        QApplication.quit()

    def tray_icon_clicked(self, reason):
        """Show window when the tray icon is clicked."""
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.show_window()
            
    def showEvent(self, event):
        """Animate the window when it is shown."""
        start_rect = self.geometry().adjusted(0, -50, 0, -50)
        self.animation.setStartValue(start_rect)
        self.animation.setEndValue(self.geometry())
        self.animation.start()
        super().showEvent(event)  # Ensure normal show behavior
        
    def move_to_bottom_right(self):
        """Move the window to the bottom-right corner of the screen."""
        screen = QGuiApplication.primaryScreen().availableGeometry()  # Get screen size
        window_size = self.frameGeometry()  # Get window size

        x = screen.width() - window_size.width()  # Calculate X position
        y = screen.height() - window_size.height()  # Calculate Y position

        self.move(x, y)  # Move window
        
        
app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)  # Prevent app from quitting when window is closed

window = MyWindow()
window.show()
app.exec()
