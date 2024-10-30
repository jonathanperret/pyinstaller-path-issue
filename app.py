from PySide6 import QtWidgets
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide6.QtWidgets import QMessageBox

import sys
import os

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.do_request()
        
        print(f"PATH is: {os.environ['PATH']}")

        self.setWindowTitle("Hello World")
        l = QtWidgets.QLabel("My simple app.")
        l.setMargin(10)
        self.setCentralWidget(l)
        self.show()

    def do_request(self):
        self._network_manager = QNetworkAccessManager()

        self._network_request = QNetworkRequest("https://api.github.com/repos/AllYarnsAreBeautiful/ayab-desktop/releases/latest")

        self._network_reply = self._network_manager.get(
            self._network_request
        )
        self._network_reply.finished.connect(self.request_finished)

    def request_finished(self):
        print(f"response status: {self._network_reply.attribute(QNetworkRequest.Attribute.HttpStatusCodeAttribute)}")
        import win32api, win32process
        for h in win32process.EnumProcessModules(win32process.GetCurrentProcess()):
            dll = win32api.GetModuleFileName(h)
            if "libssl-3-x64" in dll:
                print(f"loaded from: {dll}")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec()
