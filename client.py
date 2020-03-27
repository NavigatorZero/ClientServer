import socket
import keyboard
import UserInterface
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QTextEdit
from PyQt5.QtCore import QCoreApplication, QThread
import threading
import simple_threadpool
import time
import sys


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'opablet'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.button = QPushButton("кнопка блять", self)
        self.text = QTextEdit(self)
        self.initUI()

        self.BDTEXT = []

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.button.setToolTip('кнопка блять')
        self.button.resize(100, 70)
        self.button.clicked.connect(self.test)
        self.text.resize(120, 50)
        self.text.setText("text")
        self.show()

    def connect(self):
        global result
        result = []
        cl = socket.socket()
        cl.connect(("0.0.0.0", 12006))
        r = "table_dolgi"
        cl.send(r.encode())
        while True:
            data = cl.recv(1024)
            if data:
                print(data)
                result.append(data)

    def test(self):
        thread1 = threading.Thread(target=self.connect)
        thread1.start()
        print(result)
        self.text.setText(result)


if __name__ == "__main__":
    a = QtWidgets.QApplication(sys.argv)
    app = App()
    app.show()
    a.exec_()
