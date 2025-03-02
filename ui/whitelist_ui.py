# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'whitelist.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_appWhitelist(object):
    def setupUi(self, appWhitelist):
        if not appWhitelist.objectName():
            appWhitelist.setObjectName(u"appWhitelist")
        appWhitelist.resize(438, 339)
        icon = QIcon()
        icon.addFile(u"../assets/tomato.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        appWhitelist.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(appWhitelist)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.appWhitelistList = QListWidget(appWhitelist)
        self.appWhitelistList.setObjectName(u"appWhitelistList")

        self.verticalLayout.addWidget(self.appWhitelistList)

        self.appWhitelistSubmit = QPushButton(appWhitelist)
        self.appWhitelistSubmit.setObjectName(u"appWhitelistSubmit")

        self.verticalLayout.addWidget(self.appWhitelistSubmit)


        self.retranslateUi(appWhitelist)

        QMetaObject.connectSlotsByName(appWhitelist)
    # setupUi

    def retranslateUi(self, appWhitelist):
        appWhitelist.setWindowTitle(QCoreApplication.translate("appWhitelist", u"App Whitelist", None))
        self.appWhitelistSubmit.setText(QCoreApplication.translate("appWhitelist", u"Submit", None))
    # retranslateUi

