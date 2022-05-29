
import sys
import time
import os
from Adafruit_BNO055 import BNO055
#import adafruit_bno055
import datetime

bno = BNO055.BNO055(serial_port='/dev/ttyAMA0', rst=18)
while True:
    try:
        # Read the Euler angles for heading, roll, pitch (all in degrees).
        heading, roll, pitch = bno.read_euler()
        # Read the calibration status, 0=uncalibrated and 3=fully calibrated.
        sys, gyro, accel, mag = bno.get_calibration_status()
        # Print everything out.
        #print('Heading={0:0.2F} Roll={1:0.2F} Pitch={2:0.2F}\tSys_cal={3} Gyro_cal={4} Accel_cal={5} Mag_cal={6}'.format(
        #      heading, roll, pitch, sys, gyro, accel, mag))
        # Other values you can optionally read:
        # Orientation as a quaternion:
        #qx,qy,qz,qw = bno.read_quaterion()
        # Sensor temperature in degrees Celsius:
        temp_c = bno.read_temp()
        # Magnetometer data (in micro-Teslas):
        mx,my,mz = bno.read_magnetometer()
        # Gyroscope data (in degrees per second):
    
        gx,gy,gz = bno.read_gyroscope()
        # Accelerometer data (in meters per second squared):
        rx,ry,rz = bno.read_accelerometer()
        # Linear acceleration data (i.e. acceleration from movement, not gravity--
        # returned in meters per second squared):
        x,y,z = bno.read_linear_acceleration()
        print(x)
    except:
        print("Sensor error")
    # Gravity acceleration data (i.e. acceleration just from gravity--returned
    # in meters per second squared):
    #grx,gry,grz = bno.read_gravity()
    # Sleep for a second until the next reading.
    #xls,xms = split(x,10)
    #yls,yms = split(y,10)
    #zls,zms = split(z,10)
    #hls,hms = split(heading,10)
    #rls,rms = split(roll,10)
    #pls,pms = split(pitch,10)
    #temp= med(temp_c,2)
    #rxls,rxms = split(rx,10)
    #ryls,ryms = split(ry,10)
    #rzls,rzms = split(rz,10)
    #gxls,gxms = split(gx,10)
    #gyls,gyms = split(gy,10)
    #gzls,gzms = split(gz,10)
    #xm=med(x,5)
    #ym=med(y,5)
    #zm=med(z,5)
    #hm=med(heading,1)
    #rm=med(roll,2)
    #pm=med(pitch,2)
    #tm=med(temp,2)
    #rxm=med(rx,5)
    #3rym=med(ry,5)
    #rzm=med(rz,5)
    #gxm=med(gx,5)
    #gym=med(gy,5)
    #gzm=med(gz,5)
    #print(x)