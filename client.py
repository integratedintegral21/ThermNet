import socket
import time
import w1thermsensor
import sys
import threading
import errno

msg = "---"

def tempThread(sensor):
    while True:
        global msg
        try:
            msg = "temperature: " + str(round(sensor.get_temperature(),1))   
        except w1thermsensor.errors.SensorNotReadyError:
            print("therm sensor disconnected")
            msg = 'disconnected'
            time.sleep(1)

HOST, PORT = '192.168.8.105', 12345
welcome_msg = 'Hello from the other side!'
 
try:
    therm = w1thermsensor.W1ThermSensor()
    test = therm.get_temperature()
    t_thread = threading.Thread(target=tempThread, args=(therm,))
    t_thread.start()
except w1thermsensor.errors.SensorNotReadyError:
    print("w1 thermsensor initialization failed")
except  w1thermsensor.errors.NoSensorFoundError:
    print("w1 bus failed")


while True:
    print("Connecting...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    s.sendall(welcome_msg.encode())
    print("Connected to " + HOST)
    while True:
        try:
            s.send(str(msg))
            time.sleep(1)
        except socket.error as err:
            if err.errno == errno.ECONNRESET:
                print("Disconnected")
                break
            else:
                raise
    s.close()
