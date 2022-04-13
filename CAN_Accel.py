import logging
import sys
import time
import os
import can
from statistics import median
from Adafruit_BNO055 import BNO055

f = open("Log.txt", "w")
f.write(str(time.time()))
f.close()

def split(inp,gain):
    out=inp*gain
    ms= int(out) >> 6
    ls= int(out) & ((1 << 6) -1)
    ms= median([0,ms,255])
    ls= median([0,ls,255])
    return ls,ms

def med(inp , gain):
    out = gain*abs(median([0,int(inp),255]))
    return out

can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')# socketcan_native

# Create and configure the BNO sensor connection.  Make sure only ONE of the
# below 'bno = ...' lines is uncommented:
# Raspberry Pi configuration with serial UART and RST connected to GPIO 18:
bno = BNO055.BNO055(serial_port='/dev/ttyUSB0', rst=18)
# BeagleBone Black configuration with default I2C connection (SCL=P9_19, SDA=P9_20),
# and RST connected to pin P9_12:
#bno = BNO055.BNO055(rst='P9_12')


# Enable verbose debug logging if -v is passed as a parameter.
if len(sys.argv) == 2 and sys.argv[1].lower() == '-v':
    logging.basicConfig(level=logging.DEBUG)

# Initialize the BNO055 and stop if something went wrong.
if not bno.begin():
    raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')

# Print system status and self test result.
status, self_test, error = bno.get_system_status()
print('System status: {0}'.format(status))
print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))
# Print out an error if system status is in error mode.
if status == 0x01:
    print('System error: {0}'.format(error))
    print('See datasheet section 4.3.59 for the meaning.')

# Print BNO055 software revision and other diagnostic data.
sw, bl, accel, mag, gyro = bno.get_revision()
print('Software version:   {0}'.format(sw))
print('Bootloader version: {0}'.format(bl))
print('Accelerometer ID:   0x{0:02X}'.format(accel))
print('Magnetometer ID:    0x{0:02X}'.format(mag))
print('Gyroscope ID:       0x{0:02X}\n'.format(gyro))

print('Reading BNO055 data, press Ctrl-C to quit...')
while True:
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
    try:
        gx,gy,gz = bno.read_gyroscope()
        # Accelerometer data (in meters per second squared):
        rx,ry,rz = bno.read_accelerometer()
        # Linear acceleration data (i.e. acceleration from movement, not gravity--
        # returned in meters per second squared):
        x,y,z = bno.read_linear_acceleration()
    except:
        print("Sensor error")
    # Gravity acceleration data (i.e. acceleration just from gravity--returned
    # in meters per second squared):
    grx,gry,grz = bno.read_gravity()
    # Sleep for a second until the next reading.
    xls,xms = split(x,10)
    yls,yms = split(y,10)
    zls,zms = split(z,10)
    hls,hms = split(heading,10)
    rls,rms = split(roll,10)
    pls,pms = split(pitch,10)
    temp= med(temp_c,2)
    rxls,rxms = split(rx,10)
    ryls,ryms = split(ry,10)
    rzls,rzms = split(rz,10)
    gxls,gxms = split(gx,10)
    gyls,gyms = split(gy,10)
    gzls,gzms = split(gz,10)
    
    try:
        acc = can.Message(arbitration_id=0x123, data=[ xls, xms, yls, yms, zls, zms, 0, 0], extended_id=True)
        gyr = can.Message(arbitration_id=0x124, data=[ gxls , gxms , gyls , gyms , gzls, gzms, 0, 0], extended_id=True)
        racc= can.Message(arbitration_id=0x125, data=[rxls,rxms,ryls,ryms,rzls,rzms,0,0] , extended_id=True)
        ori = can.Message(arbitration_id=0x126, data=[hls,hms,rls,rms,pls,pms,temp,0],extended_id=True)
        
        can0.send(acc)
        can0.send(gyr)
        can0.send(racc)
        can0.send(ori)
        
        
    except:
        print("Can Error")
    print(xls)    
    print(xms)
    time.sleep(.01)

    try:
        f = open("Log.txt", "a")
        f.write(str(time.time())
        f.close()
    except:
        print("Write Error")

os.system('sudo ifconfig can0 down')