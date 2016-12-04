__author__ = 'capra'

from inputs import get_gamepad

a = True

while a:
    events = get_gamepad()
    for event in events:
        print event.ev_type, event.code, event.state
