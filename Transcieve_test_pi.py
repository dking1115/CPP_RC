#!/usr/bin/env python3
import serial
import time
i=0
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.flush()
    while True:
        i += 1
        ar=[0,i,2,3,4,5,6,7]
        #print(ar)
        u=str(ar)+"\n"
        u=u.encode('utf-8')
        ser.write(u)
        line = ser.readline().decode('utf-8').rstrip()
        if(line!=""):
            print(line)
        if i>254:
            i=1