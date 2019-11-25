import socket
import socketserver

HOST, PORT = '192.168.8.105', 12345

class TCPHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip().decode()
            print("Received: ", self.data, "from: "+ format(self.client_address[0]) +"")

class MyTCP(socketserver.TCPServer):
     
     def __init__(self,address,handler):
         super().__init__(address,handler)
         self.timeout = 3
                


server = MyTCP((HOST, PORT),TCPHandler)
server.serve_forever()