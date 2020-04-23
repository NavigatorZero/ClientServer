import socket
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QTextEdit, QTableWidget, QLabel
import threading
import sys
import pickle


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'opablet'
        self.left = 500
        self.top = 500
        self.width = 750
        self.height = 750

        self.thread1 = threading.Thread(target=self.connect)

        self.buttonAddRow = QPushButton(self)
        self.buttonRemoveRow = QPushButton(self)
        self.button = QPushButton(self)
        self.buttonUpload = QPushButton(self)

        self.tableWidget = QTableWidget(self)

        self.textTable = QTextEdit(self)

        self.textTableLabel = QLabel(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.button.setToolTip('кнопка загрузки')
        self.button.setGeometry(500, 120, 150, 35)
        self.button.setText("Загрузить таблицу")
        self.button.clicked.connect(self.test)

        self.buttonAddRow.setToolTip('кнопка установки')
        self.buttonAddRow.setGeometry(500, 200, 150, 35)
        self.buttonAddRow.setText("Добавить запись")
        self.buttonAddRow.clicked.connect(self.AddRow)

        self.buttonRemoveRow.setToolTip('кнопка установки')
        self.buttonRemoveRow.setGeometry(500, 158, 150, 35)
        self.buttonRemoveRow.setText("Удалить запись")
        self.buttonRemoveRow.clicked.connect(self.DeleteRow)

        self.buttonUpload.setToolTip('Загрузить данные в бд')
        self.buttonUpload.setGeometry(500, 250, 150, 35)
        self.buttonUpload.setText("Загрузить данные в бд")
        self.buttonUpload.clicked.connect(self.Upload)

        self.tableWidget.setGeometry(QtCore.QRect(25, 31, 450, 250))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.textTableLabel.setText("Введите имя таблицы")
        self.textTableLabel.setGeometry(500, 25, 250, 50)

        self.textTable.setGeometry(500, 75, 200, 35)
        self.show()

    def connect(self):
        global result
        global cl
        result = []
        cl = socket.socket()
        cl.connect(("localhost", 12008))
        r = self.textTable.toPlainText()
        cl.send(r.encode('utf-8'))
        while True:
            data = cl.recv(4098)
            if data:
                result = pickle.loads(data)

                break

        if data:
            if (self.tableWidget.columnCount() > 0 ):
                self.tableWidget.clear()
            self.tableWidget.setRowCount(len(result[0]))
            self.tableWidget.setColumnCount(len(result[1]))
            global rows
            rows = len(result[0])
            global column
            column = len(result[1])
            # очищаем таблицу
            self.tableWidget.clear()
            if result[1]:
                print(result[1])
                self.tableWidget.setHorizontalHeaderLabels(result[1])
            # заполняем таблицу
            row = 0
            for tup in result[0]:
                col = 0
                for item in tup:
                    cellinfo = QtWidgets.QTableWidgetItem(str(item))
                    self.tableWidget.setItem(row, col, cellinfo)
                    col += 1
                row += 1

    def test(self):
        self.thread1.start()

    def AddRow(self):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

    def Upload(self):
        dataToChange = []
        for row in range(self.tableWidget.rowCount()):
            dataToChange.append([])
            for column in range(self.tableWidget.columnCount()):
                index = self.tableWidget.item(row, column)
                dataToChange[row].append(index.text())
        dataToChange.append(self.textTable.toPlainText())
        dataToChange.append(result[1])
        cl.sendall(pickle.dumps(dataToChange))
        # We suppose data are strings

    def DeleteRow(self):
        indices = self.tableWidget.selectionModel().selectedRows()
        for index in sorted(indices):
            self.tableWidget.removeRow(index.row())


if __name__ == "__main__":
    a = QtWidgets.QApplication(sys.argv)
    app = App()
    app.show()
    a.exec_()
