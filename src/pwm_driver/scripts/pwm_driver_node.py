#!/usr/bin/env python
import rospy
import pigpio
from driver import PWM
from pwm_driver.srv import *

pi = pigpio.pi()
pwm = PWM(pi) # defaults to bus 1, address 0x40

rospy.init_node('pwm_driver')

def handle_set_duty_cycle(req):
    print 'request'
    print req.channel
    print req.value
    return SetDutyCycleResponse()


rospy.Service('set_duty_cycle', SetDutyCycle, handle_set_duty_cycle)

rospy.spin()

pwm.cancel()
pi.stop()
