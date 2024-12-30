from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class TerminalApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl.fromLocalFile("D:\Files But Not Corrupt\StoreClicker\index.html"))
        self.setCentralWidget(self.browser)
        self.setWindowTitle("Interactive Terminal")
        self.setWindowState(self.windowState() | Qt.WindowFullScreen)

        self.show()

app = QApplication([])
window = TerminalApp()
app.exec_()
