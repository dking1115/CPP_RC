from inputs import devices
from inputs import get_gamepad

for device in devices:
    print(device)
while 1:
    events = get_gamepad()
    for event in events:
        print(event.ev_type)
        if "ABS_X" in event.ev_type:
            x=event.state
            print(x)


