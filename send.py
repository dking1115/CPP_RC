import os
import can
import time

can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')# socketcan_native

while True:
    
    for x in range(32768):
        msx= x >> 8
        lsx= x & ((1 << 8) - 1)
        msg = can.Message(arbitration_id=0x123, data=[0, 1, 2, 3, 4, 5, msx, lsx], extended_id=True)
        can0.send(msg)
        time.sleep (.01)




os.system('sudo ifconfig can0 down')