from inputs import devices
from inputs import get_gamepad

for device in devices:
    print(device)
while 1:
    events = get_gamepad()
    for event in events:
        if "ABS_X" in event.code:
            x=event.state
            print(x)
         if "ABS_Y" in event.code:
            y=event.state
            print(y)



