import serial

ser = serial.Serial('/dev/ttyUSB0',250000)
i=0
while True:
    i += 1
    if i>100:
        i=-100
    read_serial=ser.readline()
    s[0] = str(int (ser.readline(),16))
    print s[0]
    print read_serial
    ser.print(i)
