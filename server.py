import socket
import threading


host = '192.168.8.105'
port = 12343

msg = 'Hello there'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)

while True:
    conn, addr = s.accept()
    print(f'Connected to:{addr}')
    conn.send(msg.encode())
    while True:
        r_msg = conn.recv(1024)

        if(r_msg.decode() != ""):
            print(r_msg.decode())
            if(r_msg.decode() == "break"):
                conn.close()
                break
            
        
    conn.close()
    

    
