import os
import sys
from apscheduler.schedulers.background import BackgroundScheduler
from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QListWidget, QLineEdit, 
    QListWidgetItem, QSystemTrayIcon, QMenu, QTimeEdit, QMessageBox
)
from PyQt6.QtGui import QGuiApplication, QAction, QIcon
from PyQt6.QtCore import QTimer, QTime, Qt, QPropertyAnimation, QEasingCurve
from datetime import datetime, timedelta

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("test.ui", self)

        # Resize and position window
        self.resize(800, 600)
        self.move_to_bottom_right()
        self.load_stylesheet("style.qss")

        # UI Elements
        self.time_label = self.findChild(QLabel, "timeLabel")
        self.task_input = self.findChild(QLineEdit, "taskInput")
        self.add_task_button = self.findChild(QPushButton, "addTaskButton")
        self.task_list = self.findChild(QListWidget, "taskList")
        self.clear_checked_button = self.findChild(QPushButton, "clearCheckedButton")
        
        self.reminder_input = self.findChild(QLineEdit, "reminderInput")
        self.reminder_list = self.findChild(QListWidget, "reminderList")
        self.add_reminder_button = self.findChild(QPushButton, "addReminderButton")
        self.reminder_time_edit = self.findChild(QTimeEdit, "reminderTimeEdit")
        self.reminder_time_edit.setDisplayFormat("HH:mm")
        
        # Pomodoro Timer UI
        self.pomodoro_timer = self.findChild(QLineEdit, "pomodoroTimer")
        self.start_pomodoro_button = self.findChild(QPushButton, "startPomodoroButton")
        self.pause_pomodoro_button = self.findChild(QPushButton, "pausePomodoroButton")
        self.reset_pomodoro_button = self.findChild(QPushButton, "resetPomodoroButton")
        
        # Connect Buttons
        self.add_task_button.clicked.connect(self.add_task)
        self.clear_checked_button.clicked.connect(self.clear_checked_tasks)
        self.add_reminder_button.clicked.connect(self.add_reminder)
        self.start_pomodoro_button.clicked.connect(self.start_pomodoro)
        self.pause_pomodoro_button.clicked.connect(self.pause_pomodoro)
        self.reset_pomodoro_button.clicked.connect(self.reset_pomodoro)
        
        self.time_for_break= True;
        

        # Timers
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
        self.reminder_timer = QTimer(self)
        self.reminder_timer.timeout.connect(self.check_reminders)
        self.reminder_timer.start(60000)

        # System Tray Setup
        self.tray_icon = QSystemTrayIcon(QIcon("Tomato-Whole-Red-1-Clip-Art.png"), self)
        self.tray_icon.setToolTip("PomKit")
        tray_menu = QMenu()
        tray_menu.addAction(QAction("Show", self, triggered=self.show_window))
        tray_menu.addAction(QAction("Quit", self, triggered=self.close_app))
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.activated.connect(self.tray_icon_clicked)
        self.tray_icon.show()
        
        # Pomodoro Variables
        self.pomodoro_time = 10 #DON"T FORGET TO CHANGE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.break_time = 5 * 60
        self.current_time = self.pomodoro_time
        self.pomodoro_running = False
        
        # Animation
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.Type.InBounce)
        
        # Scheduler for Pomodoro
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        
        self.reminders = []
        self.update_time()

    def start_pomodoro(self):
        """Start the Pomodoro Timer and ensure display updates every second."""
        if not self.pomodoro_running:
            self.pomodoro_running = True
            self.current_time = self.pomodoro_time

            # Disconnect any previous connections to avoid multiple triggers
            try:
                self.timer.timeout.disconnect(self.update_pomodoro_display)
            except TypeError:
                pass  # Ignore if there was nothing to disconnect

            self.timer.timeout.connect(self.update_pomodoro_display)
            self.timer.start(1000)  # Update every second
            self.update_pomodoro_display()  # Ensure UI updates immediately
    
    def pause_pomodoro(self):
        self.pomodoro_running = False
        self.timer.stop()

    def reset_pomodoro(self):
        """Reset the Pomodoro Timer."""
        self.pomodoro_running = False
        self.timer.stop()
        self.current_time = self.pomodoro_time
        self.update_pomodoro_display()

    def update_pomodoro_display(self):
        """Update the Pomodoro Timer Display every second."""
        if self.pomodoro_running and self.current_time > 0:
            minutes, seconds = divmod(self.current_time, 60)
            self.pomodoro_timer.setText(f"{minutes:02}:{seconds:02}")
            self.current_time -= 1  # Decrease time by 1 second
        else:
            self.timer.stop()  # Stop the timer when countdown reaches zero
            if self.time_for_break:
                self.show_pomodoro_notification_break()
            else:
                self.show_pomodoro_notification_work()

    def schedule_pomodoro_end(self, duration):
        """Schedule an event when the Pomodoro session ends."""
        current_datetime = datetime.now()  # Get current date & time
        end_datetime = current_datetime + timedelta(seconds=duration)  # Add duration
        self.scheduler.add_job(self.show_pomodoro_notification_break, "date", run_date=end_datetime)

    def show_pomodoro_notification_break(self):
        """Notify user about break time and wait before restarting."""
        QMessageBox.information(self, "Pomodoro Completed!", "⏳ Time's up! Take a break!")
        self.current_time = self.break_time
        self.pomodoro_running = False
        self.time_for_break = False  # Next session will be work

        # Wait before starting the break countdown
        QTimer.singleShot(1000, self.start_pomodoro)
        
    def show_pomodoro_notification_work(self):
        """Notify user to get back to work and wait before restarting."""
        QMessageBox.information(self, "Break Over!", "⏳ Time to get back to work!")
        self.current_time = self.pomodoro_time
        self.pomodoro_running = False
        self.time_for_break = True  # Next session will be break

        # Wait before starting the work countdown
        QTimer.singleShot(1000, self.start_pomodoro)

    def update_time(self):
        self.time_label.setText("Current time: " + QTime.currentTime().toString("HH:mm:ss"))

    def add_task(self):
        task = self.task_input.text().strip()
        if task:
            item = QListWidgetItem(task)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.task_list.addItem(item)
            self.task_input.clear()

    def add_reminder(self):
        reminder_text = self.reminder_input.text().strip()
        reminder_time = self.reminder_time_edit.time().toString("HH:mm")
        if reminder_text:
            self.reminders.append((reminder_time, reminder_text))
            self.reminder_list.addItem(f"{reminder_time} - {reminder_text}")
            self.reminder_input.clear()

    def check_reminders(self):
        current_time = QTime.currentTime().toString("HH:mm")
        for reminder_time, reminder_text in self.reminders:
            if reminder_time == current_time:
                self.show_reminder_dialog(reminder_text)
                self.reminders.remove((reminder_time, reminder_text))

    def show_reminder_dialog(self, message):
        QMessageBox.information(self, "Reminder Alert", f"Reminder: {message}")

    def clear_checked_tasks(self):
        for i in range(self.task_list.count() - 1, -1, -1):
            item = self.task_list.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                self.task_list.takeItem(i)

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.tray_icon.showMessage("To-Do List", "App minimized to tray", QSystemTrayIcon.MessageIcon.Information, 2000)

    def show_window(self):
        self.showNormal()
        self.activateWindow()

    def close_app(self):
        self.tray_icon.hide()
        QApplication.quit()

    def tray_icon_clicked(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.show_window()
            
    def move_to_bottom_right(self):
        """Move the window to the bottom-right corner of the screen."""
        screen = QGuiApplication.primaryScreen().availableGeometry()  # Get available screen size
        window_size = self.frameGeometry()  # Get window size

        x = screen.right() - window_size.width()  # Adjust X position
        y = screen.bottom() - window_size.height()  # Adjust Y position

        self.move(x, y)  # Move window
        
    def load_stylesheet(self, filename):
        """Load an external QSS stylesheet and apply it."""
        if os.path.exists(filename):
            with open(filename, "r") as file:
                self.setStyleSheet(file.read())
        else:
            print(f"Error: Stylesheet '{filename}' not found!")

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)
window = MyWindow()
window.show()
app.exec()
