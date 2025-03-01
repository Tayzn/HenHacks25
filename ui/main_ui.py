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
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1119, 710)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_10 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")

        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.timeLabel = QLabel(self.groupBox_2)
        self.timeLabel.setObjectName(u"timeLabel")

        self.verticalLayout_5.addWidget(self.timeLabel)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.appWhitelistButton = QPushButton(self.groupBox_2)
        self.appWhitelistButton.setObjectName(u"appWhitelistButton")

        self.verticalLayout_5.addWidget(self.appWhitelistButton)

        self.mainWindowAppWhitelist = QListWidget(self.groupBox_2)
        self.mainWindowAppWhitelist.setObjectName(u"mainWindowAppWhitelist")
        self.mainWindowAppWhitelist.setSelectionMode(QAbstractItemView.NoSelection)

        self.verticalLayout_5.addWidget(self.mainWindowAppWhitelist)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        self.pomodoroTimer = QLineEdit(self.groupBox_2)
        self.pomodoroTimer.setObjectName(u"pomodoroTimer")

        self.verticalLayout_5.addWidget(self.pomodoroTimer)

        self.startPomodoroButton = QPushButton(self.groupBox_2)
        self.startPomodoroButton.setObjectName(u"startPomodoroButton")

        self.verticalLayout_5.addWidget(self.startPomodoroButton)

        self.pausePomodoroButton = QPushButton(self.groupBox_2)
        self.pausePomodoroButton.setObjectName(u"pausePomodoroButton")

        self.verticalLayout_5.addWidget(self.pausePomodoroButton)

        self.resetPomodoroButton = QPushButton(self.groupBox_2)
        self.resetPomodoroButton.setObjectName(u"resetPomodoroButton")

        self.verticalLayout_5.addWidget(self.resetPomodoroButton)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.volumeControl = QSlider(self.groupBox_2)
        self.volumeControl.setObjectName(u"volumeControl")
        self.volumeControl.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.volumeControl)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.horizontalLayout_8.addLayout(self.verticalLayout)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.focusMode = QPushButton(self.groupBox)
        self.focusMode.setObjectName(u"focusMode")

        self.verticalLayout_4.addWidget(self.focusMode)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.reminderList = QListWidget(self.groupBox)
        self.reminderList.setObjectName(u"reminderList")

        self.verticalLayout_4.addWidget(self.reminderList)

        self.reminderInput = QLineEdit(self.groupBox)
        self.reminderInput.setObjectName(u"reminderInput")

        self.verticalLayout_4.addWidget(self.reminderInput)

        self.reminderTimeEdit = QTimeEdit(self.groupBox)
        self.reminderTimeEdit.setObjectName(u"reminderTimeEdit")

        self.verticalLayout_4.addWidget(self.reminderTimeEdit)

        self.addReminderButton = QPushButton(self.groupBox)
        self.addReminderButton.setObjectName(u"addReminderButton")

        self.verticalLayout_4.addWidget(self.addReminderButton)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.taskList = QListWidget(self.groupBox)
        self.taskList.setObjectName(u"taskList")

        self.verticalLayout_4.addWidget(self.taskList)

        self.taskInput = QLineEdit(self.groupBox)
        self.taskInput.setObjectName(u"taskInput")

        self.verticalLayout_4.addWidget(self.taskInput)

        self.addTaskButton = QPushButton(self.groupBox)
        self.addTaskButton.setObjectName(u"addTaskButton")

        self.verticalLayout_4.addWidget(self.addTaskButton)

        self.clearCheckedButton = QPushButton(self.groupBox)
        self.clearCheckedButton.setObjectName(u"clearCheckedButton")

        self.verticalLayout_4.addWidget(self.clearCheckedButton)


        self.horizontalLayout_7.addWidget(self.groupBox)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")

        self.horizontalLayout_7.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_7)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1119, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle("")
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"Timer (displays current time)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"App Usage", None))
        self.appWhitelistButton.setText(QCoreApplication.translate("MainWindow", u"Configure App Whitelist", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Pomodoro Timer", None))
        self.pomodoroTimer.setText("")
        self.startPomodoroButton.setText(QCoreApplication.translate("MainWindow", u"Start Pomodoro", None))
        self.pausePomodoroButton.setText(QCoreApplication.translate("MainWindow", u"Pause Pomodoro", None))
        self.resetPomodoroButton.setText(QCoreApplication.translate("MainWindow", u"Reset Pomodoro", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Music Controls", None))
        self.groupBox.setTitle("")
        self.focusMode.setText(QCoreApplication.translate("MainWindow", u"Focus Mode", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Reminders", None))
        self.addReminderButton.setText(QCoreApplication.translate("MainWindow", u"Add Reminder", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"To-Do List", None))
        self.addTaskButton.setText(QCoreApplication.translate("MainWindow", u"Add Task", None))
        self.clearCheckedButton.setText(QCoreApplication.translate("MainWindow", u"Clear Checked Items", None))
    # retranslateUi

