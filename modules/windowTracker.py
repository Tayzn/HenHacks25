from PyQt6.QtCore import QThread

MAX_ALLOWED_TIME = 10 # seconds allowed on a non-whitelisted app

class AppTimerTask(QThread):
  def __init__(self, parent = None):
    super().__init__(parent)
    self.timeout = MAX_ALLOWED_TIME

  def run(self):
    while True:
      self.sleep(1)
      self.timeout -= 1
      if self.timeout == 0:
        print("You have spent too much time on an unwhitelisted app!")
        break
    self.quit()

class WindowTracker():
  def __init__(self, app, whitelist=[]):
    self.app = app
    self.whitelistedApps = whitelist
    self.currentTimeoutTask: AppTimerTask = None

  def window_changed(self, appName):
    if self.currentTimeoutTask:
      self.currentTimeoutTask.quit()
      self.currentTimeoutTask = None
      print('quit previous')

    if appName not in self.whitelistedApps:
      self.currentTimeoutTask = AppTimerTask()
      self.currentTimeoutTask.start()
      print("Changed to non-whitelisted app!")



