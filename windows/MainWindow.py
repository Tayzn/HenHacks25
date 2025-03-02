import vlc
import os
import sys
from apscheduler.schedulers.background import BackgroundScheduler
from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QListWidget, QLineEdit, 
    QListWidgetItem, QSystemTrayIcon, QMenu, QTimeEdit, QMessageBox, QGroupBox,
    QSlider, QToolButton
)
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput, QMediaDevices
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QGuiApplication, QAction, QIcon
from PyQt6.QtCore import QTimer, QTime, Qt, QPropertyAnimation, QEasingCurve
from datetime import datetime, timedelta

UI_FILE = "././ui/main.ui"

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        
        # Testing audio
        uic.loadUi(UI_FILE, self)

        audio_outputs = QMediaDevices.audioOutputs()
        if not audio_outputs:
            print("No audio output devices detected!")
        else:
            print("Available audio devices:")
            for device in audio_outputs:
                print(device.description())

        # Resize and position window
        self.resize(800, 600)
        self.move_to_bottom_right()

        self.init_player()
        self.station_url = ""

        # UI Elements
        self.time_label = self.findChild(QLabel, "timeLabel")
        self.task_input = self.findChild(QLineEdit, "taskInput")
        self.add_task_button = self.findChild(QPushButton, "addTaskButton")
        self.task_list = self.findChild(QListWidget, "taskList")
        self.clear_checked_button = self.findChild(QPushButton, "clearCheckedButton")
        self.whitelistButton = self.findChild(QPushButton, "appWhitelistButton")
        self.whitelistPreview = self.findChild(QListWidget, "mainWindowAppWhitelist")
        self.musicBrowseBtn = self.findChild(QPushButton, "musicBrowseRadioBtn")
        self.musicPlayPauseBtn = self.findChild(QToolButton, "musicPlayPauseBtn")
        self.musicVolumeSlider = self.findChild(QSlider, "musicVolumeSlider")
        self.musicTitleLabel = self.findChild(QLabel, "musicLabel")
        self.musicVolumeLabel = self.findChild(QLabel, "musicVolumeLabel")
        
        self.musicVolumeLabel.setText(f"Volume: {self.musicVolumeSlider.value()}%")
        
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
        
        self.pomodoro_timer_instance = QTimer(self)
        self.pomodoro_timer_instance.timeout.connect(self.update_pomodoro_display)
        
        # Connect Buttons
        self.add_task_button.clicked.connect(self.add_task)
        self.clear_checked_button.clicked.connect(self.clear_checked_tasks)
        self.add_reminder_button.clicked.connect(self.add_reminder)
        self.start_pomodoro_button.clicked.connect(self.start_pomodoro)
        self.pause_pomodoro_button.clicked.connect(self.pause_pomodoro)
        self.reset_pomodoro_button.clicked.connect(self.reset_pomodoro)
        self.whitelistButton.clicked.connect(self.show_whitelist_dialog)
        self.musicBrowseBtn.clicked.connect(self.on_music_browse)
        self.musicPlayPauseBtn.clicked.connect(self.on_music_playpause)
        self.musicVolumeSlider.valueChanged.connect(self.on_music_volume_change)
        
        self.time_for_break= True
        

        # Timers
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
        self.reminder_timer = QTimer(self)
        self.reminder_timer.timeout.connect(self.check_reminders)
        self.reminder_timer.start(60000)

        # System Tray Setup
        self.tray_icon = QSystemTrayIcon(QIcon("./assets/tomato.png"), self)
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
        
        #Sound effect
        self.audio_output = QAudioOutput()
        self.media_player = QMediaPlayer()
        self.media_player.setAudioOutput(self.audio_output)
        self.media_player.setSource(QUrl.fromLocalFile("./assets/bells.wav"))  # Path to your sound file
        self.audio_output.setVolume(0.5)  # Adjust volume
        self.media_player.play()

    def show_whitelist_dialog(self):
        self.app.show_window("WhitelistDialog")

    def start_pomodoro(self):
        """Start the Pomodoro Timer and ensure display updates every second."""
        if not self.pomodoro_running:
            self.pomodoro_running = True
            self.pomodoro_timer_instance.start(1000)  # Update every second
            self.update_pomodoro_display()  # Ensure UI updates immediately

    def pause_pomodoro(self):
        """Pause only the Pomodoro Timer without affecting the system clock."""
        self.pomodoro_running = False
        self.pomodoro_timer_instance.stop()  # Stop only the pomodoro timer

    def reset_pomodoro(self):
        """Reset the Pomodoro Timer."""
        self.pomodoro_running = False
        self.pomodoro_timer_instance.stop()
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

    def show_unfocused_alert(self):
        QMessageBox.warning(self, "Getting off track!", "You have been in a non-whitelisted app for a while now...")

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
        


    # Music controls
    def on_music_browse(self):
        self.app.show_window("RadioBrowserDialog")

    def update_radio_station(self, radio_info):
        self.musicTitleLabel.setText(radio_info["name"])
        self.station_url = radio_info["url"]

    def on_music_playpause(self):
        if self.vlc_player.is_playing():
            self.vlc_player.stop()
            self.musicPlayPauseBtn.setText("▶️")

    # Music controls
    def on_music_browse(self):
        self.app.show_window("RadioBrowserDialog")

    def update_radio_station(self, radio_info):
        self.musicTitleLabel.setText(radio_info["name"])
        self.station_url = radio_info["url"]

    def on_music_playpause(self):
        if self.vlc_player.is_playing():
            self.vlc_player.stop()
            self.musicPlayPauseBtn.setText("▶️")
        else:
            self.play_track(self.station_url)
            self.musicPlayPauseBtn.setText("⏹️")

    def on_music_volume_change(self, level):
        self.musicVolumeLabel.setText(f"Volume: {level}%")
        self.vlc_player.audio_set_volume(level)

    def init_player(self):
        self.vlc_instance = vlc.Instance(
            "--no-xlib"
        )  # Ensure no X server dependency on Linux
        self.vlc_player = self.vlc_instance.media_player_new()

        # Set VLC player volume
        self.vlc_player.audio_set_volume(self.musicVolumeSlider.value())

    def play_track(self, url):
        if not url:
            return

        url = url.strip()

        media = self.vlc_instance.media_new(url)
        self.vlc_player.set_media(media)

        if self.vlc_player.play() == -1:
            print("Unable to play")
        else:
            print("Playing media")