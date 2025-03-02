import vlc
from PyQt6 import uic
from PyQt6.QtWidgets import (
    QLabel,
    QListWidget,
    QMainWindow,
    QPushButton,
    QSlider,
    QToolButton,
)

UI_FILE = "././ui/main.ui"


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app

        uic.loadUi(UI_FILE, self)  # Load the .ui file

        self.button = self.findChild(QPushButton, "appWhitelistButton")
        self.whitelistPreview = self.findChild(QListWidget, "mainWindowAppWhitelist")

        self.musicBrowseBtn = self.findChild(QPushButton, "musicBrowseRadioBtn")
        self.musicPlayPauseBtn = self.findChild(QToolButton, "musicPlayPauseBtn")
        self.musicVolumeSlider = self.findChild(QSlider, "musicVolumeSlider")
        self.musicTitleLabel = self.findChild(QLabel, "musicLabel")
        self.musicVolumeLabel = self.findChild(QLabel, "musicVolumeLabel")

        self.musicBrowseBtn.clicked.connect(self.on_music_browse)
        self.musicPlayPauseBtn.clicked.connect(self.on_music_playpause)
        self.musicVolumeSlider.valueChanged.connect(self.on_music_volume_change)

        self.musicVolumeLabel.setText(f"Volume: {self.musicVolumeSlider.value()}%")

        self.button.clicked.connect(self.on_button_click)

        self.init_player()
        self.station_url = ""

    def on_button_click(self):
        self.app.show_window("WhitelistDialog")

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

    # def play_pause(self):
    # self.vlc_player.pause()
    # print("Toggle play/pause")
