import socket
import keyboard
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QTextEdit
from PyQt5.QtCore import QCoreApplication, QThread
import threading
import time
import sys
import pickle


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'opablet'
        self.left = 500
        self.top = 500
        self.width = 500
        self.height = 500
        self.button = QPushButton(self)
        self.text = QTextEdit(self)
        self.thread1 = threading.Thread(target=self.connect)

        self.buttonUpload = QPushButton(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.button.setToolTip('кнопка загрузки')
        self.button.setGeometry(175, 250, 175, 50)
        self.button.setText("Download data")
        self.button.clicked.connect(self.test)

        self.text.setGeometry(50, 10, 400, 250)

        self.buttonUpload.setToolTip('кнопка установки')
        self.buttonUpload.setGeometry(175, 400, 175, 50)
        self.buttonUpload.setText("Upload data")
        self.buttonUpload.clicked.connect(self.Upload)
        self.show()

    def connect(self):
        global result
        global cl
        result = []
        cl = socket.socket()
        cl.connect(("localhost", 12008))
        r = "tablesubject"
        cl.send(pickle.dumps(r))
        while True:
            data = cl.recv(1024)
            if data:
                result = pickle.loads(data)
                break

        if data:
            for items in result:
                self.text.append(str(items))

    def test(self):
        self.thread1.start()

    def Upload(self):
        changedData = self.text.toPlainText()

        cl.send(pickle.dumps(changedData))


if __name__ == "__main__":
    a = QtWidgets.QApplication(sys.argv)
    app = App()
    app.show()
    a.exec_()
