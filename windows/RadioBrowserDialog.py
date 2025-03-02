import vlc
from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)
from pyradios import RadioBrowser


class RadioBrowserDialog(QDialog):
    def __init__(self, app):
        super().__init__()
        self.app = app

        # Load the .ui file for the second window
        uic.loadUi("././ui/radiobrowser.ui", self)

        # Access the input field and submit button
        self.text_input = self.findChild(QLineEdit, "radioBrowserInput")
        self.search_button = self.findChild(QPushButton, "radioBrowserSearch")
        self.submit_button = self.findChild(QPushButton, "radioBrowserSubmit")
        self.tree_widget = self.findChild(QTreeWidget, "radioBrowserTree")

        self.search_button.clicked.connect(self.search)
        self.submit_button.clicked.connect(self.submit)

        self.tree_widget.setHeaderLabels(["Name", "Tags"])

        self.rb = RadioBrowser()

    def search(self):
        # print("SEARCH", self.text_input.text())
        self.stations = self.rb.search(name=self.text_input.text())

        for station in self.stations:
            # Create the root item (top-level item) and set text for multiple columns

            root_item = QTreeWidgetItem(self.tree_widget)
            root_item.setText(0, station["name"][:48])  # Column 1
            root_item.setText(1, station["tags"])  # Column 2

        self.tree_widget.resizeColumnToContents(0)

    def submit(self):
        self.accept()

        station = self.get_selected_station()
        self.app.get_window("MainWindow").update_radio_station(station)

    def get_selected_station(self):
        selected = self.tree_widget.selectedIndexes()
        if len(selected) == 0:
            return

        index = selected[0].row()

        return self.stations[index]
