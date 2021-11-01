#!/usr/bin/env python3
import serial
import time
from inputs import devices
from inputs import get_gamepad
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
ser.flush()
enabled=1
switches=0
x=0
y=0
T=0
while True:
    events = get_gamepad()
    for event in events:
        switches=0
        #print(event.ev_type, event.code, event.state)
        if "ABS_RX" in event.code:
            x=event.state
            x=((x/32768)*750)+750

        if "ABS_RZ" in event.code:
            T=event.state
            T=((T/1024)*255)
            #print(event.ev_type, event.code, event.state)
            
        if "ABS_RY" in event.code:
            y=event.state
            #print(y)
            y=((y/32768)*10000)+10000
            #print(y)
        if "BTN_EAST" in event.code:
            switches=1
        #This deactivates the seat switch
        if "BTN_WEST" in event.code:
            switches=2
        #This sets neutral mode
        if "BTN_SOUTH" in event.code:
            switches=3
        #This sets drive mode
    #print(x)
    
    ar=[enabled,int(y/255),int(y%255),int(x/255),int(x%255),switches,T,7]
    print(ar)
    u=str(ar)+"\n"
    u=u.encode('utf-8')
    ser.write(u)
    line = ser.readline()
    if(line!=""):
        print(line)