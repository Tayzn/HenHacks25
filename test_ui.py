# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1119, 858)
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
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.timeLabel = QTextEdit(self.groupBox_2)
        self.timeLabel.setObjectName(u"timeLabel")

        self.verticalLayout_5.addWidget(self.timeLabel)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.appUsage = QTextEdit(self.groupBox_2)
        self.appUsage.setObjectName(u"appUsage")

        self.verticalLayout_5.addWidget(self.appUsage)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.music = QTextEdit(self.groupBox_2)
        self.music.setObjectName(u"music")

        self.verticalLayout_5.addWidget(self.music)

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


        self.horizontalLayout_7.addWidget(self.groupBox)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")

        self.horizontalLayout_7.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_7)

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
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Timer (displays current time)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"App Usage", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Music Controls", None))
        self.music.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.focusMode.setText(QCoreApplication.translate("MainWindow", u"Focus Mode", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"To-Do List", None))
        self.addTaskButton.setText(QCoreApplication.translate("MainWindow", u"Add Task", None))
    # retranslateUi

