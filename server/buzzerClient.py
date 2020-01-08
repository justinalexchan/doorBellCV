import RPi.GPIO as GPIO
from time import sleep
import socket

port = 0 #change port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', port))
s.listen()

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
buzzer = 17
GPIO.setup(buzzer,GPIO.OUT)
p = GPIO.PWM(17, 190)

clientsocket, address = s.accept()
print("connected: " + str(address))

while True:
    
    msg = clientsocket.recv(1024)
    print(msg)
    if str(msg) == "b'1'":
        p.start(90)
        sleep(1)
        msg = ''
    else:
        msg = ''
        p.stop()

    
    
