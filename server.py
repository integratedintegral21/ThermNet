import socket
import threading  

def accept_connections(sck):
    connection, address = sck.accept()
    connection.settimeout(5)
    print(f'Connected to:{address}')
    return connection, address


host = '192.168.8.105'
port = 12343

msg = 'Hello there'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)

while True:
    
    conn, addr = accept_connections(s)

    try:
        while True:
            r_msg = conn.recv(1024)
            if(r_msg.decode() != ""):
                f_msg = float(r_msg.decode())
                print(round(f_msg,1))
                if(r_msg.decode() == "break"):
                    conn.close()
                    break
    except socket.timeout as timeout:
        print(f'Connection with {addr} timed out')
        conn.close()
            
        
    conn.close()
    

    
