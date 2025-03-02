
class FocusManager():
  def __init__(self, app):
    self.focusMode = False
    self.app = app

  def toggle_focus_mode(self):
    self.focusMode = not self.focusMode

  def is_focus_mode(self):
    return self.focusMode