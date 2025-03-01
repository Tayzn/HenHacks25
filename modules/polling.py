import time
import pywinctl as pywin
from PyQt6.QtCore import QThread

import psutil
def get_name_from_pid(pid):
    return psutil.Process(pid).name()

class PollingThread(QThread):
    def __init__(self, app, parent = None):
        super().__init__(parent)
        self.app = app
        self.storedActiveWindowName = ""

    def run(self):
        while True:
            currentWindow = pywin.getActiveWindow()
            currentAppName = get_name_from_pid(currentWindow.getPID())

            if currentAppName != self.storedActiveWindowName:
                self.storedActiveWindowName = currentAppName
                self.app.get_app_task("WindowTracker").window_changed(currentAppName)

            time.sleep(0.3)