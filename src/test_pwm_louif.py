#!/usr/bin/env python

import pigpio

import time

# PWM, value defaults to 0, min to 0, max to 255
# [GPIO, PWM <, value <, min <, max > > >]

if __name__ == '__main__':
    # pi.set_PWM_dutycycle()
    pi = pigpio.pi()
    while (1):
        time.sleep(10)
        pi.set_PWM_dutycycle(21, 0)
        time.sleep(10)
        pi.set_PWM_dutycycle(21, 127)
        time.sleep(10)
        pi.set_PWM_dutycycle(21, 255)     
        
