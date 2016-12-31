#!/usr/bin/env python

import pigpio

import time

# PWM, value defaults to 0, min to 0, max to 255
# [GPIO, PWM <, value <, min <, max > > >]

if __name__ == '__main__':
    # pi.set_PWM_dutycycle()
    pi = pigpio.pi()
    value = 0
    while (1):
        pi.set_PWM_dutycycle(21, value)
        time.sleep(5)
        value += 10
        if value > 255:
            value = 255
            pi.set_PWM_dutycycle(21, value)
            time.sleep(10)
            value = 0
 
    pi.stop()
     
        
