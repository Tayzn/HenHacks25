import os
from PyQt6.QtWidgets import QApplication

from modules import polling, windowTracker
from windows.MainWindow import MainWindow
from windows.RadioBrowserDialog import RadioBrowserDialog
from windows.WhitelistDialog import WhitelistDialog


def load_stylesheet(qObject, filename):
    """Load an external QSS stylesheet and apply it."""
    if os.path.exists(filename):
        with open(filename, "r") as file:
            qObject.setStyleSheet(file.read())
    else:
        print(f"Error: Stylesheet '{filename}' not found!")

class App():
  def __init__(self):
    self.start()

  def start(self):
    app = QApplication([])
    self.pid = app.applicationPid()

    self.appTasks = {
      "WindowTracker": windowTracker.WindowTracker(self),
      "PollingThread": polling.PollingThread(self)
    }
    self.appTasks["PollingThread"].start()

    self.windows = {
      "MainWindow": MainWindow(self),
      "WhitelistDialog": WhitelistDialog(self),
      "RadioBrowserDialog": RadioBrowserDialog(self),
    }
    for window in self.windows.values():
       load_stylesheet(window, "./assets/style.qss")

    self.windows["MainWindow"].show()

    app.exec()

  def get_app_task(self, task_name):
    return self.appTasks[task_name]
  
  def start_task(self, task_name):
    self.appTasks[task_name].start()

  def stop_task(self, task_name):
    self.appTasks[task_name].quit()

  def show_window(self, window_name):
    self.windows[window_name].show()

  def get_window(self, window_name):
    return self.windows[window_name]

App() # Entry
