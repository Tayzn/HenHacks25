# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reminder.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTimeEdit,
    QVBoxLayout, QWidget)

class Ui_ReminderDialog(object):
    def setupUi(self, ReminderDialog):
        if not ReminderDialog.objectName():
            ReminderDialog.setObjectName(u"ReminderDialog")
        ReminderDialog.resize(350, 75)
        icon = QIcon()
        icon.addFile(u"../assets/tomato.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        ReminderDialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(ReminderDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.reminderTime = QTimeEdit(ReminderDialog)
        self.reminderTime.setObjectName(u"reminderTime")

        self.horizontalLayout.addWidget(self.reminderTime)

        self.reminderInput = QLineEdit(ReminderDialog)
        self.reminderInput.setObjectName(u"reminderInput")

        self.horizontalLayout.addWidget(self.reminderInput)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.reminderSubmit = QPushButton(ReminderDialog)
        self.reminderSubmit.setObjectName(u"reminderSubmit")

        self.verticalLayout.addWidget(self.reminderSubmit)


        self.retranslateUi(ReminderDialog)

        QMetaObject.connectSlotsByName(ReminderDialog)
    # setupUi

    def retranslateUi(self, ReminderDialog):
        ReminderDialog.setWindowTitle(QCoreApplication.translate("ReminderDialog", u"New Reminder", None))
        self.reminderTime.setDisplayFormat(QCoreApplication.translate("ReminderDialog", u"hh:mm a", None))
        self.reminderInput.setPlaceholderText(QCoreApplication.translate("ReminderDialog", u"Enter text...", None))
        self.reminderSubmit.setText(QCoreApplication.translate("ReminderDialog", u"Submit", None))
    # retranslateUi

