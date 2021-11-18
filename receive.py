import os
import can

os.system('sudo ip link set can0 type can bitrate 250000')
os.system('sudo ifconfig can0 up')

can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')# socketcan_native

#msg = can.Message(arbitration_id=0x123, data=[0, 1, 2, 3, 4, 5, 6, 7], extended_id=False)
while True:
    msg= can0.recv(1.0)
    if msg is None:
        print('Timeout occurred, no message.')
        os.system('sudo ifconfig can0 down')
        exit()
    #print (msg)
    txt=str(msg)
    txt=txt.split()
    #print(txt[3])
    ID=txt[3]
    Bitone=txt[7]
    Bittwo=txt[8]
    Bitthree=txt[9]
    Bitfour=txt[10]
    Bitfive=txt[11]
    Bitsix=txt[12]
    Bitseven=txt[13]
    Biteight=txt[14]
    if(ID=="00201905"):
        print(int(Bitfour,16))
    #print(txt)
    



