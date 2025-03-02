import psutil
from PyQt6.QtCore import QThread, pyqtSignal, QObject, QMetaObject, Qt
from PyQt6.QtWidgets import QMessageBox

MAX_ALLOWED_TIME = 5 # seconds allowed on a non-whitelisted app

class AppTimerWorker(QObject):
  def run(self, task):
    while task.running:
      task.sleep(1)
      task.timeout -= 1
      if task.timeout == 0:
        task.signal.emit(0)
        break

class AppTimerTask(QThread):
  def __init__(self, signal, parent = None):
    super().__init__(parent)
    self.timeout = MAX_ALLOWED_TIME
    self.running = True
    self.worker = AppTimerWorker()
    self.signal = signal

  def run(self):
    self.worker.run(self)

class WindowTracker(QObject):
  def __init__(self, app, whitelist=set()):
    self.app = app
    self.whitelistedApps = whitelist
    whitelist.add(psutil.Process(app.pid).name())
    self.currentTimeoutTask: AppTimerTask = None

  def show_alert(self):
    print('showing alert')
    QMessageBox.warning(self.app.get_window("MainWindow"), "Get back on track!", "You've been using a non-whitelisted app for a while now...")

  def window_changed(self, appName, signal):
    if self.currentTimeoutTask:
      self.currentTimeoutTask.running = False
      self.currentTimeoutTask.wait()
      self.currentTimeoutTask = None

    if appName not in self.whitelistedApps:
      self.currentTimeoutTask = AppTimerTask(signal)
      self.currentTimeoutTask.start()
      print("Changed to non-whitelisted app!", appName)
    else:
      print("Changed to whitelisted app")

  def update_whitelist(self, whitelist):
    self.whitelistedApps = set(whitelist)
    this_process = psutil.Process(self.app.pid).name()
    self.whitelistedApps.add(this_process)

    currentWindow = self.app.get_app_task("PollingThread").get_active_window_name()
    self.window_changed(currentWindow)
    
    mainWindowPreview = self.app.get_window("MainWindow").whitelistPreview
    mainWindowPreview.clear()
    for whitelisted in whitelist:
      if whitelisted == this_process: continue
      mainWindowPreview.addItem(whitelisted)
    






