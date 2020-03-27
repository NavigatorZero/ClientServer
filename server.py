import socket

import Database

print("hello")
PORT = 12006
HOST = '0.0.0.0'
serv = socket.socket()
serv.bind((HOST, PORT))
serv.listen()
conn, addr = serv.accept()
print('Connect', addr)
test = Database.Database()
while True:
    data = conn.recv(1024)
    # table_dolgi
    if data:
        print(data)
        table = test.getTable(data.decode())
        for tuples in table:

            for item in tuples:
                print(item)
                print(type(item))
                if type(item) is str:
                    print(item)
                    conn.send(item.encode())
        conn.send(data)
        conn.sendall(data)