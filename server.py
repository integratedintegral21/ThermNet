import socket
import threading
import sys

host, port = '192.168.8.105', 12345
clients = list()

class Client(threading.Thread):

    conn = 0
    addr = 0

    def handleClient(self,conn,addr):
        while True:
            data = conn.recv(1024)
            print(f"Message from:{address}")
            print(data.decode())
        print(f"Connection with: {address} closed")
        conn.close()

    def __init__(self,conn,addr):
        self.conn = conn
        self.addr = addr
        super().__init__(target=self.handleClient,args=(self.conn,self.addr,))
        self.start()
    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host,port))
except socket.error:
    print("Binding failed")
    sys.exit()

print("Socket bounded")
s.listen(10)

while True:
    connection, address = s.accept()
    print(f"Connected with {address}")
    new_client = Client(connection,address)
    clients.append(new_client)