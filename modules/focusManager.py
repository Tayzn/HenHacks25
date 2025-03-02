from PyQt6.QtCore import QTimer, QObject

class FocusSession():
  def __init__(self, app):
    self.duration = 0
    self.appTimeline = []
    self.app = app

    self.app.get_window("MainWindow").focusButton.setText("In Focus Mode: " + str(self.duration) + " seconds")

    self.timer = QTimer()
    self.timer.timeout.connect(self.tick_timer)
    self.timer.start(1000)

  def tick_timer(self):
    self.duration += 1
    self.app.get_window("MainWindow").focusButton.setText("In Focus Mode: " + str(self.duration) + " seconds")

  def ping_app_timeline(self, appName, whitelisted):
    self.appTimeline.append({"appName": appName, "time": self.duration, "whitelisted": whitelisted})

  def close(self):
    self.timer.stop()
    self.app.get_window("MainWindow").focusButton.setText("Start Focus Mode")
    self.app.show_window("GraphicDisplay", self.appTimeline)

class FocusManager(QObject):
  def __init__(self, app):
    super().__init__()
    self.focusMode = False
    self.app = app
    self.currentSession = None

  def toggle_focus_mode(self):
    self.focusMode = not self.focusMode
    if self.focusMode:
      self.currentSession = FocusSession(self.app)
    elif self.currentSession:
      self.currentSession.close()
    return self.focusMode

  def ping_app_time(self, appName, whitelisted):
    if not self.currentSession: return
    self.currentSession.ping_app_timeline(appName, whitelisted)

  def is_focus_mode(self):
    return self.focusMode