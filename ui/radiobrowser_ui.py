# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'radiobrowser.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLineEdit, QPushButton, QSizePolicy, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_RadioBrowser(object):
    def setupUi(self, RadioBrowser):
        if not RadioBrowser.objectName():
            RadioBrowser.setObjectName(u"RadioBrowser")
        RadioBrowser.resize(500, 300)
        icon = QIcon()
        icon.addFile(u"../assets/tomato.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        RadioBrowser.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(RadioBrowser)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioBrowserInput = QLineEdit(RadioBrowser)
        self.radioBrowserInput.setObjectName(u"radioBrowserInput")

        self.horizontalLayout.addWidget(self.radioBrowserInput)

        self.radioBrowserSearch = QPushButton(RadioBrowser)
        self.radioBrowserSearch.setObjectName(u"radioBrowserSearch")

        self.horizontalLayout.addWidget(self.radioBrowserSearch)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.radioBrowserTree = QTreeWidget(RadioBrowser)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.radioBrowserTree.setHeaderItem(__qtreewidgetitem)
        self.radioBrowserTree.setObjectName(u"radioBrowserTree")

        self.verticalLayout.addWidget(self.radioBrowserTree)

        self.radioBrowserSubmit = QPushButton(RadioBrowser)
        self.radioBrowserSubmit.setObjectName(u"radioBrowserSubmit")

        self.verticalLayout.addWidget(self.radioBrowserSubmit)


        self.retranslateUi(RadioBrowser)

        QMetaObject.connectSlotsByName(RadioBrowser)
    # setupUi

    def retranslateUi(self, RadioBrowser):
        RadioBrowser.setWindowTitle(QCoreApplication.translate("RadioBrowser", u"Radio Browser", None))
        self.radioBrowserInput.setPlaceholderText(QCoreApplication.translate("RadioBrowser", u"Enter text...", None))
        self.radioBrowserSearch.setText(QCoreApplication.translate("RadioBrowser", u"Search", None))
        self.radioBrowserSubmit.setText(QCoreApplication.translate("RadioBrowser", u"Submit", None))
    # retranslateUi

