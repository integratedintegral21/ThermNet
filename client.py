import socket
import time
import w1thermsensor

sensor = w1thermsensor.W1ThermSensor()

HEADERSIZE = 10
     
host = '192.168.8.105'
port = 12343 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

r_msg = s.recv(1024)
print(r_msg.decode())
for i in range(5):
    s_msg = str(sensor.get_temperature())
    s.send(s_msg)
    time.sleep(1)
    
s.send("break")


