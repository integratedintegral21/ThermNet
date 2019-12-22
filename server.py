import socket
import threading  

connections = list()

msg = 'Hello there'

def accept_connections(sck):
    connection, address = sck.accept()
    connection.settimeout(2)
    print(f'Connected to:{address}')
    connections.append((connection,address))
    connection.send(msg.encode())


host = '192.168.8.105' ##your ip address
port = 12343


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)

while True:
    accept_connections(s)
    try:
        while True:
            r_msg = connections[0][0].recv(1024)
            if(r_msg.decode() != ""):
                f_msg = float(r_msg.decode())
                print(round(f_msg,1))
                if(r_msg.decode() == "break"):
                    connections[0][0].close()
                    break
    except socket.timeout as timeout:
        print(f'Connection with {connections[0][1]} timed out')
        connections[0][0].close()
        connections.pop(0)
    except socket.error as error:
        print(error.errno)
            
    for i in connections:    
        connections[i][0].close()
    

    
