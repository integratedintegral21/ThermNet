import socket
import threading
import sys

host, port = '192.168.8.105', 12345
threads = list()

def handleClient(conn,addr):
    while True:
        data = conn.recv(1024)
        print(f"Message from:{address}")
        print(data.decode())
    print(f"Connection with: {address} closed")
    conn.close()

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
    threads.append(threading.Thread(target=handleClient,args=(connection,address,)))
    threads[len(threads) - 1].start()