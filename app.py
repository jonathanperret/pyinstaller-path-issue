from PySide6 import QtWidgets
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide6.QtWidgets import QMessageBox

import sys

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.do_request()

        self.setWindowTitle("Hello World")
        l = QtWidgets.QLabel("My simple app.")
        l.setMargin(10)
        self.setCentralWidget(l)
        self.show()

    def do_request(self):
        self._network_manager = QNetworkAccessManager()
        self._network_manager.setAutoDeleteReplies(True)

        self._network_request = QNetworkRequest("https://api.github.com/repos/AllYarnsAreBeautiful/ayab-desktop/releases/latest")

        self._network_reply = self._network_manager.get(
            self._network_request
        )
        self._network_reply.finished.connect(self.request_finished)

    def request_finished(self):
        data = self._network_reply.readAll()
        QMessageBox.information(self, "response", str(data)[:100], QMessageBox.StandardButton.Ok)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec()
