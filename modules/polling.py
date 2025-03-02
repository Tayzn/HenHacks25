import time
import psutil
import pywinctl as pywin
from PyQt6.QtCore import QThread, pyqtSignal

def get_name_from_pid(pid):
    return psutil.Process(pid).name()

class PollingThread(QThread):
    signal = pyqtSignal(int)
    ping_signal = pyqtSignal(str)

    def __init__(self, app, parent = None):
        super().__init__(parent)
        self.app = app
        self.storedActiveWindowName = ""

    def run(self):
        while True:
            currentWindow = pywin.getActiveWindow()
            if not currentWindow: continue
            currentAppName = get_name_from_pid(currentWindow.getPID())

            if currentAppName != self.storedActiveWindowName:
                self.storedActiveWindowName = currentAppName
                self.app.get_app_task("WindowTracker").window_changed(currentAppName, self.signal, self.ping_signal)
                
            time.sleep(0.2)

    def get_active_window_name(self):
        return self.storedActiveWindowName