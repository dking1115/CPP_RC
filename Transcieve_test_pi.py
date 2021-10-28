#!/usr/bin/env python3
import serial
import time
i=0
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.flush()
    while True:
        i += 1
        ser.write(str(i) + "\n")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)
        if i>100:
            i=0