from PyQt5.QtCore import QObject, pyqtSlot, QUrl, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel





class TerminalApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create QWebEngineView
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl.fromLocalFile("D:/Files But Not Corrupt/Ultimatus/index.html"))
        self.setCentralWidget(self.browser)
        self.setWindowTitle("Interactive Terminal")
        

        
      

        self.show()


# Run the application
app = QApplication([])
window = TerminalApp()
app.exec_()
