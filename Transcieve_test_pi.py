#!/usr/bin/env python3
import serial
import time
i=0
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.flush()
    while True:
        i += 1
        ar={0,i,2,3,4,5,6,7}
        #print(ar)
        u=str(ar)+"\n"
        u=u.encode('ASCII')
        ser.write(u)
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        if i>100:
            i=0