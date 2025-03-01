from PyQt6.QtWidgets import QApplication
from windows.MainWindow import MainWindow
from windows.WhitelistDialog import WhitelistDialog
from modules import polling, windowTracker

class App():
  def __init__(self):
    self.appTasks = {
      "WindowTracker": windowTracker.WindowTracker(self),
      "PollingThread": polling.PollingThread(self)
    }

    self.start()

  def start(self):
    self.appTasks["PollingThread"].start()

    app = QApplication([])
    
    self.windows = {
      "MainWindow": MainWindow(self),
      "WhitelistDialog": WhitelistDialog(self)
    }

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
