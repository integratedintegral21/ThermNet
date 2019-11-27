import socket
import time
import w1thermsensor
import sys

HOST, PORT = '192.168.8.105', 12345
msg = 'Hello from the other side!'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    therm = w1thermsensor.W1ThermSensor()
except w1thermsensor.errors.SensorNotReadyError:
    print("w1 thermsensor initialization failed")
except  w1thermsensor.errors.NoSensorFoundError:
    print("w1 thermsensor not found")



try:
    s.connect((HOST,PORT))
    s.sendall(msg.encode())
    while True:
        msg = round(therm.get_temperature(),1)
        s.send(str(msg))
        time.sleep(1)

finally:
    s.close()
