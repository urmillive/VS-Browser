import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back Button
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Forward Button
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Reload Button
        realod_btn = QAction('Reload', self)
        realod_btn.triggered.connect(self.browser.reload)
        navbar.addAction(realod_btn)

        # home Button
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # StackOverflow Button
        stackoverflow = QAction('StackOverflow', self)
        stackoverflow.triggered.connect(self.stackoverflow)
        navbar.addAction(stackoverflow)

        # url Bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_my_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def stackoverflow(self):
        self.browser.setUrl(QUrl('https://stackoverflow.com'))

    def navigate_my_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, url):
        self.url_bar.setText(url.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('VS Browser')
window = MainWindow()
app.exec_()
