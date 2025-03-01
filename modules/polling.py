import time
from PyQt6.QtCore import QThread

class PollingThread(QThread):
    def run(self):
        while True:
            print('polling!')
            time.sleep(1)