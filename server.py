import socket
import threading
import sys

host, port = '192.168.8.100', 12345 #client's socket
clients = list()

class Client(threading.Thread):

    conn = None
    addr = None

    def __init__(self,conn,addr):
        self.conn = conn
        self.addr = addr
        self.conn.settimeout(3)
        super().__init__(target=self.handleClient)
        self.start()

    def handleClient(self):
        try:
            while True:
                data = self.conn.recv(1024)
                print(f"Message from:{address}")
                print(data.decode())
        except socket.timeout:
            print("Connection with ", address, " timed out")
            clients.remove(self)
            self.conn.close()
        print("Connection with ", address , " closed")
        self.conn.close()
    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host,port))
except socket.error:
    print("Binding failed")
    sys.exit(0)

print("Socket bounded")
s.listen(10)

while True:
    try:
        connection, address = s.accept()
        print(f"Connected with {address}")
        new_client = Client(connection,address)
        clients.append(new_client)
    except Exception:
        sys.exit(0)
