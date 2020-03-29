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
    # table_dolgi
    if pickle.loads(data) == "tablesubject":
        table = db.getTable(pickle.loads(data))
        data = pickle.dumps(table)
        conn.send(data)
    elif data:

        result = []
        test = pickle.loads(data)
        opa = test.split(', ')
        for i in opa:
            if i[0:3] == 'b"(':
                result.append(int(i[3:]))
                continue

            if i[-2] == ')':
                last = i.replace(')"', "")
                result.append(str(last))
                continue

            result.append(str(i))
        db.updateTable(result)
