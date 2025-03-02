import psutil
from PyQt6.QtCore import QThread, QObject, QFileInfo
from PyQt6.QtWidgets import QMessageBox, QFileIconProvider, QListWidgetItem

MAX_ALLOWED_TIME = 5 # seconds allowed on a non-whitelisted app

class AppTimerWorker(QObject):
  def run(self, task):
    while task.running:
      task.sleep(1)
      task.timeout -= 1

      if task.timeout == 3:
        task.pingSignal.emit(task.appName)

      if task.timeout == 0:
        task.signal.emit(0)
        break

class AppTimerTask(QThread):
  def __init__(self, signal, pingSignal, appName, parent = None):
    super().__init__(parent)
    self.timeout = MAX_ALLOWED_TIME
    self.running = True
    self.worker = AppTimerWorker()
    self.signal = signal
    self.pingSignal = pingSignal
    self.appName = appName

  def run(self):
    self.worker.run(self)

class WindowTracker(QObject):
  def __init__(self, app, whitelist=set()):
    self.app = app
    self.whitelistedApps = whitelist
    whitelist.add(psutil.Process(app.pid).name())
    self.currentTimeoutTask: AppTimerTask = None

  def window_changed(self, appName, signal, pingSignal):
    if self.currentTimeoutTask:
      self.currentTimeoutTask.running = False
      self.currentTimeoutTask.wait()
      self.currentTimeoutTask = None

    if appName not in self.whitelistedApps:
      self.currentTimeoutTask = AppTimerTask(signal, pingSignal, appName)
      self.currentTimeoutTask.start()
      print("Changed to non-whitelisted app!", appName)
    else:
      print("Changed to whitelisted app")

  def update_whitelist(self, whitelist):
    self.whitelistedApps = set(whitelist)
    this_process = psutil.Process(self.app.pid).name()
    self.whitelistedApps.add(this_process)

    currentWindow = self.app.get_app_task("PollingThread").get_active_window_name()
    self.window_changed(currentWindow, self.app.get_app_task("PollingThread").signal, self.app.get_app_task("PollingThread").ping_signal)
    
    mainWindowPreview = self.app.get_window("MainWindow").whitelistPreview
    mainWindowPreview.clear()

    provider = QFileIconProvider()
    existing = set()

    for proc in psutil.process_iter():
      name = proc.name()
      if name in existing: continue
      existing.add(name)
      if name in self.whitelistedApps and name != this_process:
        new_item = QListWidgetItem(provider.icon(QFileInfo(proc.exe())), name)
        mainWindowPreview.addItem(new_item)
    






