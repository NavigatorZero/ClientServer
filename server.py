import socket

import Database
import json
import pickle
import numpy as np


class StdClass:
    pass


print("hello")
PORT = 12008
HOST = 'localhost'
serv = socket.socket()
serv.bind((HOST, PORT))
serv.listen()
conn, addr = serv.accept()
print('Connect', addr)
db = Database.Database()
while True:
    data = conn.recv(4096)

    if data:
        try:
            data = data.decode('utf-8')
            if data == "tablesubject":
                table = db.getTable(data)
                conn.sendall(table)
        except:
            pass

            try:
                newTable = pickle.loads(data)
                db.updateTable(newTable)
            except:
                pass
