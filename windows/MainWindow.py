import os
import sys
from datetime import datetime, timedelta

import vlc
from apscheduler.schedulers.background import BackgroundScheduler
from PyQt6 import uic
from PyQt6.QtCore import QEasingCurve, QPropertyAnimation, Qt, QTime, QTimer, QUrl
from PyQt6.QtGui import QAction, QGuiApplication, QIcon
from PyQt6.QtMultimedia import QAudioOutput, QMediaDevices, QMediaPlayer
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMenu,
    QMessageBox,
    QPushButton,
    QSlider,
    QSystemTrayIcon,
    QTimeEdit,
)

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
        self.musicPlayPauseBtn = self.findChild(QPushButton, "musicPlayPauseBtn")
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
        self.pomodoro_timer_label = self.findChild(QLabel, "pomodoroTimer")
        self.start_pomodoro_button = self.findChild(QPushButton, "startPomodoroButton")
        self.pause_pomodoro_button = self.findChild(QPushButton, "pausePomodoroButton")
        self.reset_pomodoro_button = self.findChild(QPushButton, "resetPomodoroButton")

        # Connect Buttons
        self.add_task_button.clicked.connect(self.add_task)
        self.clear_checked_button.clicked.connect(self.clear_checked_tasks)
        self.add_reminder_button.clicked.connect(self.add_reminder)
        self.start_pomodoro_button.clicked.connect(self.start_pause_pomodoro)
        self.reset_pomodoro_button.clicked.connect(self.reset_pomodoro)
        self.whitelistButton.clicked.connect(self.show_whitelist_dialog)
        self.musicBrowseBtn.clicked.connect(self.on_music_browse)
        self.musicPlayPauseBtn.clicked.connect(self.on_music_playpause)
        self.musicVolumeSlider.valueChanged.connect(self.on_music_volume_change)

        # Timers
        self.pomodoro_timer = QTimer(self)
        self.pomodoro_timer.timeout.connect(self.update_pomodoro_display)
        # self.pomodoro_timer.start(1000)

        self.reminder_timer = QTimer(self)
        self.reminder_timer.timeout.connect(self.check_reminders)
        self.reminder_timer.start(60000)

        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self.update_clock)
        self.clock_timer.start(1000)

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
        self.pomo_work_time = 10  # DON"T FORGET TO CHANGE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.pomo_break_time = 5 * 60
        self.pomo_current_time = self.pomo_work_time
        self.is_pomo_running = False
        self.pomodoro_status = "Work"

        # Animation
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.Type.InBounce)

        # Scheduler for Pomodoro
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()

        self.reminders = []

        self.update_pomodoro_display()

        # Sound effect
        self.audio_output = QAudioOutput()
        self.media_player = QMediaPlayer()
        self.media_player.setAudioOutput(self.audio_output)
        self.media_player.setSource(
            QUrl.fromLocalFile("./assets/bells.wav")
        )  # Path to your sound file
        self.audio_output.setVolume(0.5)  # Adjust volume
        self.media_player.play()

    def show_whitelist_dialog(self):
        self.app.show_window("WhitelistDialog")

    def start_pause_pomodoro(self):
        """Start the Pomodoro Timer and ensure display updates every second."""

        if self.is_pomo_running:
            self.pomodoro_timer.stop()
            self.is_pomo_running = False
        else:
            self.pomodoro_timer.start(1000)  # Update every second
            self.is_pomo_running = True

    def reset_pomodoro(self):
        """Reset the Pomodoro Timer."""
        self.is_pomo_running = False
        self.pomodoro_timer.stop()

        self.pomodoro_status = "Work"
        self.pomo_current_time = self.pomo_work_time

        self.update_pomodoro_display()

    def update_pomodoro_display(self):
        """Update the Pomodoro Timer Display every second."""

        if self.pomo_current_time > 0:
            minutes, seconds = divmod(self.pomo_current_time, 60)
            self.pomodoro_timer_label.setText(
                f"{self.pomodoro_status}: {minutes:02}:{seconds:02}"
            )
            self.pomo_current_time -= 1  # Decrease time by 1 second
        else:
            if self.pomodoro_status == "Work":
                self.show_pomodoro_notification_break()
                self.pomo_current_time = self.pomo_break_time
                self.pomodoro_status = "Rest"
            else:
                self.show_pomodoro_notification_work()
                self.pomo_current_time = self.pomo_work_time
                self.pomodoro_status = "Work"

    def show_pomodoro_notification_break(self):
        """Notify user about break time and wait before restarting."""
        QMessageBox.information(
            self, "Pomodoro Completed!", "⏳ Time's up! Take a break!"
        )
        self.pomo_current_time = self.pomo_break_time
        self.is_pomo_running = False

        # Wait before starting the break countdown
        QTimer.singleShot(1000, self.start_pause_pomodoro)

    def show_pomodoro_notification_work(self):
        """Notify user to get back to work and wait before restarting."""
        QMessageBox.information(self, "Break Over!", "⏳ Time to get back to work!")
        self.pomo_current_time = self.pomo_work_time
        self.is_pomo_running = False

        # Wait before starting the work countdown
        QTimer.singleShot(1000, self.start_pause_pomodoro)

    def update_clock(self):
        self.time_label.setText(QTime.currentTime().toString("hh:mm:ss a"))

    def add_task(self):
        task = self.task_input.text().strip()
        if task:
            item = QListWidgetItem(task)
            item.setFlags(
                item.flags()
                | Qt.ItemFlag.ItemIsUserCheckable
                | Qt.ItemFlag.ItemIsEnabled
            )
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
        QMessageBox.warning(
            self,
            "Getting off track!",
            "You have been in a non-whitelisted app for a while now...",
        )

    def show_notification(self, title, message):
        QMessageBox.information(self, title, message)

    def clear_checked_tasks(self):
        for i in range(self.task_list.count() - 1, -1, -1):
            item = self.task_list.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                self.task_list.takeItem(i)

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.tray_icon.showMessage(
            "To-Do List",
            "App minimized to tray",
            QSystemTrayIcon.MessageIcon.Information,
            2000,
        )

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
        screen = (
            QGuiApplication.primaryScreen().availableGeometry()
        )  # Get available screen size
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
