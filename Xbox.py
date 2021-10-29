from inputs import devices
from inputs import get_gamepad

for device in devices:
    print(device)
while 1:
    events = get_gamepad()
    for event in events:
        print(event.code)
        if "ABS_X" in event.code:
            x=event.state
            print(x)


