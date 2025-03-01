from PyQt6.QtWidgets import QApplication
from windows.ExampleWindow import ExampleWindow
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
    window = ExampleWindow()
    window.show()
    testDialog = WhitelistDialog(self)
    testDialog.show()
    app.exec()

  def get_app_task(self, task_name):
    return self.appTasks[task_name]
  
  def start_task(self, task_name):
    self.appTasks[task_name].start()

  def stop_task(self, task_name):
    self.appTasks[task_name].quit()

App() # Entry
