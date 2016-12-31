#!/usr/bin/env python

import pigpio

# PWM, value defaults to 0, min to 0, max to 255
# [GPIO, PWM <, value <, min <, max > > >]

if __name__ == '__main__':
    # pi.set_PWM_dutycycle()
    pi = pigpio.pi()
    pi.set_PWM_dutycycle(21, 25)
    while (1):
        pass
