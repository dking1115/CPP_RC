#!/usr/bin/env python3
import serial
import time
from inputs import devices
from inputs import get_gamepad
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.flush()
enabled=1
switches=0
x=0
y=0
while True:
    events = get_gamepad()
    for event in events:
        switches=0
        if "ABS_X" in event.code:
            x=event.state
        if "ABS_Y" in event.code:
            y=event.state
    y=((y/32000)*10000)+10000
    x=((x/32000)*750)+750
    ar=[enabled,int(y/255),int(y%255),int(x/255),int(x%255),5,6,7]
    print(ar)
    u=str(ar)+"\n"
    u=u.encode('utf-8')
    ser.write(u)
    line = ser.readline().decode('utf-8').rstrip()
    if(line!=""):
        print(line)