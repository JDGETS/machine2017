import pigpio

pins = [7, 8, 9, 27, 28]

def handle_change(gpio, level, tick):
    print 'GPIO %d = %d' % (gpio, level, level)

for pin in pins:
    pi.callback(pin, pigpio.EITHER_EDGE, handle_change)

raw_input('')
