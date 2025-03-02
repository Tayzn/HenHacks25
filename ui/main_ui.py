# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QStatusBar, QTimeEdit,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1119, 710)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leftGroup = QGroupBox(self.centralwidget)
        self.leftGroup.setObjectName(u"leftGroup")
        self.verticalLayout_5 = QVBoxLayout(self.leftGroup)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.statusGroup = QGroupBox(self.leftGroup)
        self.statusGroup.setObjectName(u"statusGroup")
        self.verticalLayout = QVBoxLayout(self.statusGroup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.timeLabel = QLabel(self.statusGroup)
        self.timeLabel.setObjectName(u"timeLabel")

        self.verticalLayout.addWidget(self.timeLabel)


        self.verticalLayout_5.addWidget(self.statusGroup)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.appsGroup = QGroupBox(self.leftGroup)
        self.appsGroup.setObjectName(u"appsGroup")
        self.verticalLayout_2 = QVBoxLayout(self.appsGroup)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.appsGroup)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.appWhitelistButton = QPushButton(self.appsGroup)
        self.appWhitelistButton.setObjectName(u"appWhitelistButton")

        self.verticalLayout_2.addWidget(self.appWhitelistButton)

        self.mainWindowAppWhitelist = QListWidget(self.appsGroup)
        self.mainWindowAppWhitelist.setObjectName(u"mainWindowAppWhitelist")
        self.mainWindowAppWhitelist.setSelectionMode(QAbstractItemView.NoSelection)

        self.verticalLayout_2.addWidget(self.mainWindowAppWhitelist)


        self.verticalLayout_5.addWidget(self.appsGroup)

        self.label = QLabel(self.leftGroup)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.label_5 = QLabel(self.leftGroup)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        self.pomodoroTimer = QLineEdit(self.leftGroup)
        self.pomodoroTimer.setObjectName(u"pomodoroTimer")

        self.verticalLayout_5.addWidget(self.pomodoroTimer)

        self.startPomodoroButton = QPushButton(self.leftGroup)
        self.startPomodoroButton.setObjectName(u"startPomodoroButton")

        self.verticalLayout_5.addWidget(self.startPomodoroButton)

        self.pausePomodoroButton = QPushButton(self.leftGroup)
        self.pausePomodoroButton.setObjectName(u"pausePomodoroButton")

        self.verticalLayout_5.addWidget(self.pausePomodoroButton)

        self.resetPomodoroButton = QPushButton(self.leftGroup)
        self.resetPomodoroButton.setObjectName(u"resetPomodoroButton")

        self.verticalLayout_5.addWidget(self.resetPomodoroButton)

        self.musicGroup = QGroupBox(self.leftGroup)
        self.musicGroup.setObjectName(u"musicGroup")
        self.horizontalLayout = QHBoxLayout(self.musicGroup)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.musicPlayPauseBtn = QToolButton(self.musicGroup)
        self.musicPlayPauseBtn.setObjectName(u"musicPlayPauseBtn")

        self.horizontalLayout.addWidget(self.musicPlayPauseBtn)

        self.musicBrowseRadioBtn = QPushButton(self.musicGroup)
        self.musicBrowseRadioBtn.setObjectName(u"musicBrowseRadioBtn")

        self.horizontalLayout.addWidget(self.musicBrowseRadioBtn)

        self.musicLabel = QLabel(self.musicGroup)
        self.musicLabel.setObjectName(u"musicLabel")

        self.horizontalLayout.addWidget(self.musicLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.musicVolumeLabel = QLabel(self.musicGroup)
        self.musicVolumeLabel.setObjectName(u"musicVolumeLabel")

        self.horizontalLayout.addWidget(self.musicVolumeLabel)

        self.musicVolumeSlider = QSlider(self.musicGroup)
        self.musicVolumeSlider.setObjectName(u"musicVolumeSlider")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.musicVolumeSlider.sizePolicy().hasHeightForWidth())
        self.musicVolumeSlider.setSizePolicy(sizePolicy)
        self.musicVolumeSlider.setMaximum(100)
        self.musicVolumeSlider.setOrientation(Qt.Horizontal)
        self.musicVolumeSlider.setTickPosition(QSlider.TicksBelow)

        self.horizontalLayout.addWidget(self.musicVolumeSlider)


        self.verticalLayout_5.addWidget(self.musicGroup)


        self.horizontalLayout_2.addWidget(self.leftGroup)

        self.rightGroup = QGroupBox(self.centralwidget)
        self.rightGroup.setObjectName(u"rightGroup")
        self.verticalLayout_4 = QVBoxLayout(self.rightGroup)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.focusMode = QPushButton(self.rightGroup)
        self.focusMode.setObjectName(u"focusMode")

        self.verticalLayout_4.addWidget(self.focusMode)

        self.label_2 = QLabel(self.rightGroup)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.reminderList = QListWidget(self.rightGroup)
        self.reminderList.setObjectName(u"reminderList")

        self.verticalLayout_4.addWidget(self.reminderList)

        self.reminderInput = QLineEdit(self.rightGroup)
        self.reminderInput.setObjectName(u"reminderInput")

        self.verticalLayout_4.addWidget(self.reminderInput)

        self.reminderTimeEdit = QTimeEdit(self.rightGroup)
        self.reminderTimeEdit.setObjectName(u"reminderTimeEdit")

        self.verticalLayout_4.addWidget(self.reminderTimeEdit)

        self.addReminderButton = QPushButton(self.rightGroup)
        self.addReminderButton.setObjectName(u"addReminderButton")

        self.verticalLayout_4.addWidget(self.addReminderButton)

        self.label_4 = QLabel(self.rightGroup)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.taskList = QListWidget(self.rightGroup)
        self.taskList.setObjectName(u"taskList")

        self.verticalLayout_4.addWidget(self.taskList)

        self.taskInput = QLineEdit(self.rightGroup)
        self.taskInput.setObjectName(u"taskInput")

        self.verticalLayout_4.addWidget(self.taskInput)

        self.addTaskButton = QPushButton(self.rightGroup)
        self.addTaskButton.setObjectName(u"addTaskButton")

        self.verticalLayout_4.addWidget(self.addTaskButton)

        self.clearCheckedButton = QPushButton(self.rightGroup)
        self.clearCheckedButton.setObjectName(u"clearCheckedButton")

        self.verticalLayout_4.addWidget(self.clearCheckedButton)


        self.horizontalLayout_2.addWidget(self.rightGroup)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1119, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.leftGroup.setTitle("")
        self.statusGroup.setTitle("")
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.appsGroup.setTitle("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"App Wishlist", None))
        self.appWhitelistButton.setText(QCoreApplication.translate("MainWindow", u"Configure App Whitelist", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"App Usage", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Pomodoro Timer", None))
        self.pomodoroTimer.setText("")
        self.startPomodoroButton.setText(QCoreApplication.translate("MainWindow", u"Start Pomodoro", None))
        self.pausePomodoroButton.setText(QCoreApplication.translate("MainWindow", u"Pause Pomodoro", None))
        self.resetPomodoroButton.setText(QCoreApplication.translate("MainWindow", u"Reset Pomodoro", None))
        self.musicGroup.setTitle(QCoreApplication.translate("MainWindow", u"Music Controls", None))
        self.musicPlayPauseBtn.setText(QCoreApplication.translate("MainWindow", u"\u25b6\ufe0f", None))
        self.musicBrowseRadioBtn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.musicLabel.setText("")
        self.musicVolumeLabel.setText(QCoreApplication.translate("MainWindow", u"Volume: 100%", None))
        self.rightGroup.setTitle("")
        self.focusMode.setText(QCoreApplication.translate("MainWindow", u"Focus Mode", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Reminders", None))
        self.addReminderButton.setText(QCoreApplication.translate("MainWindow", u"Add Reminder", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"To-Do List", None))
        self.addTaskButton.setText(QCoreApplication.translate("MainWindow", u"Add Task", None))
        self.clearCheckedButton.setText(QCoreApplication.translate("MainWindow", u"Clear Checked Items", None))
    # retranslateUi

