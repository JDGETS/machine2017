#!/usr/bin/env python
import rospy
import pigpio
from driver import PWM
from pwm_driver.srv import *

rospy.init_node('pwm_driver')

pi = pigpio.pi()
pwm = PWM(pi) # defaults to bus 1, address 0x40

pwm.set_frequency(50)

def handle_set_duty_cycle(req):
    pwm.set_duty_cycle(req.channel, req.value)
    return SetDutyCycleResponse()

rospy.Service('set_duty_cycle', SetDutyCycle, handle_set_duty_cycle)

rospy.spin()

pwm.cancel()
pi.stop()
