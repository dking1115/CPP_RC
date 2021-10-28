import serial

ser = serial.Serial('/dev/ttyUSB0',250000)
i=0
while True:
    i += 1
    if i>100:
        i=-100
    read_serial=ser.readline()
    s = ser.readline()
    print (s)
    print (read_serial)
    ser.write(i)
