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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1119, 710)
        icon = QIcon()
        icon.addFile(u"../assets/tomato.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.timeLabel = QLabel(self.frame)
        self.timeLabel.setObjectName(u"timeLabel")
        font = QFont()
        font.setBold(True)
        self.timeLabel.setFont(font)
        self.timeLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.timeLabel)

        self.leftGroup = QGroupBox(self.frame)
        self.leftGroup.setObjectName(u"leftGroup")
        self.gridLayout = QGridLayout(self.leftGroup)
        self.gridLayout.setObjectName(u"gridLayout")
        self.appsGroup = QGroupBox(self.leftGroup)
        self.appsGroup.setObjectName(u"appsGroup")
        self.verticalLayout_2 = QVBoxLayout(self.appsGroup)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.appWhitelistButton = QPushButton(self.appsGroup)
        self.appWhitelistButton.setObjectName(u"appWhitelistButton")

        self.verticalLayout_2.addWidget(self.appWhitelistButton)

        self.mainWindowAppWhitelist = QListWidget(self.appsGroup)
        self.mainWindowAppWhitelist.setObjectName(u"mainWindowAppWhitelist")
        self.mainWindowAppWhitelist.setSelectionMode(QAbstractItemView.NoSelection)

        self.verticalLayout_2.addWidget(self.mainWindowAppWhitelist)


        self.gridLayout.addWidget(self.appsGroup, 2, 0, 1, 1)

        self.musicGroup = QGroupBox(self.leftGroup)
        self.musicGroup.setObjectName(u"musicGroup")
        self.horizontalLayout_3 = QHBoxLayout(self.musicGroup)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.musicBrowseRadioBtn = QPushButton(self.musicGroup)
        self.musicBrowseRadioBtn.setObjectName(u"musicBrowseRadioBtn")

        self.horizontalLayout_3.addWidget(self.musicBrowseRadioBtn)

        self.musicLabel = QLabel(self.musicGroup)
        self.musicLabel.setObjectName(u"musicLabel")

        self.horizontalLayout_3.addWidget(self.musicLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.musicVolumeLabel = QLabel(self.musicGroup)
        self.musicVolumeLabel.setObjectName(u"musicVolumeLabel")

        self.horizontalLayout_3.addWidget(self.musicVolumeLabel)

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

        self.horizontalLayout_3.addWidget(self.musicVolumeSlider)

        self.musicPlayPauseBtn = QPushButton(self.musicGroup)
        self.musicPlayPauseBtn.setObjectName(u"musicPlayPauseBtn")

        self.horizontalLayout_3.addWidget(self.musicPlayPauseBtn)


        self.gridLayout.addWidget(self.musicGroup, 10, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 8, 0, 1, 1)

        self.groupBox = QGroupBox(self.leftGroup)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.addReminderButton = QPushButton(self.groupBox)
        self.addReminderButton.setObjectName(u"addReminderButton")

        self.verticalLayout_3.addWidget(self.addReminderButton)

        self.reminderList = QListWidget(self.groupBox)
        self.reminderList.setObjectName(u"reminderList")

        self.verticalLayout_3.addWidget(self.reminderList)


        self.gridLayout.addWidget(self.groupBox, 4, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.leftGroup)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pomodoroTimer = QLabel(self.groupBox_2)
        self.pomodoroTimer.setObjectName(u"pomodoroTimer")

        self.horizontalLayout_6.addWidget(self.pomodoroTimer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.startPomodoroButton = QPushButton(self.groupBox_2)
        self.startPomodoroButton.setObjectName(u"startPomodoroButton")

        self.horizontalLayout_6.addWidget(self.startPomodoroButton)

        self.resetPomodoroButton = QPushButton(self.groupBox_2)
        self.resetPomodoroButton.setObjectName(u"resetPomodoroButton")

        self.horizontalLayout_6.addWidget(self.resetPomodoroButton)


        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.focusMode = QPushButton(self.leftGroup)
        self.focusMode.setObjectName(u"focusMode")

        self.gridLayout.addWidget(self.focusMode, 9, 0, 1, 1)


        self.verticalLayout.addWidget(self.leftGroup)


        self.horizontalLayout_2.addWidget(self.frame)

        self.rightGroup = QGroupBox(self.centralwidget)
        self.rightGroup.setObjectName(u"rightGroup")
        self.verticalLayout_4 = QVBoxLayout(self.rightGroup)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
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

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FocusMato", None))
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.leftGroup.setTitle("")
        self.appsGroup.setTitle(QCoreApplication.translate("MainWindow", u"App Whitelist", None))
        self.appWhitelistButton.setText(QCoreApplication.translate("MainWindow", u"Configure App Whitelist", None))
        self.musicGroup.setTitle(QCoreApplication.translate("MainWindow", u"Music Controls", None))
        self.musicBrowseRadioBtn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.musicLabel.setText("")
        self.musicVolumeLabel.setText(QCoreApplication.translate("MainWindow", u"Volume: 100%", None))
        self.musicPlayPauseBtn.setText(QCoreApplication.translate("MainWindow", u"\u25b6\ufe0f", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Reminders", None))
        self.addReminderButton.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Pomodoro", None))
        self.pomodoroTimer.setText(QCoreApplication.translate("MainWindow", u"WORK 00:00", None))
        self.startPomodoroButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.resetPomodoroButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.focusMode.setText(QCoreApplication.translate("MainWindow", u"Start Focus Mode", None))
        self.rightGroup.setTitle("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"To-Do List", None))
        self.addTaskButton.setText(QCoreApplication.translate("MainWindow", u"Add Task", None))
        self.clearCheckedButton.setText(QCoreApplication.translate("MainWindow", u"Clear Checked Items", None))
    # retranslateUi

