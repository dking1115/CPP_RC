import os
import can

os.system('sudo ip link set can0 type can bitrate 250000')
os.system('sudo ifconfig can0 up')

can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')# socketcan_native

#msg = can.Message(arbitration_id=0x123, data=[0, 1, 2, 3, 4, 5, 6, 7], extended_id=False)
while True:
    msg= can0.recv(10.0)
    if msg is None:
        print('Timeout occurred, no message.')
        os.system('sudo ifconfig can0 down')
        exit()
    #print (msg)
    txt=str(msg)
    txt=txt.split()
    #print(txt[3])
    ID=txt[3]
    Bitone=txt[6]
    Bittwo=txt[7]
    Bitthree=txt[8]
    Bitfour=txt[9]
    Bitfive=txt[10]
    Bitsix=txt[11]
    Bitseven=txt[12]
    Biteight=txt[13]
    if(ID=="0cfdd633"):
        print(Bitone)
    #print(txt)
    



