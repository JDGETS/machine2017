#!/usr/bin/env python
import rospy
import pigpio
from driver import PWM
from pwm_driver.msg import *

rospy.init_node('pwm_driver')

pi = pigpio.pi()
pwm = PWM(pi) # defaults to bus 1, address 0x40

pwm.set_frequency(50)

def handle_msg(msg):
    pwm.set_duty_cycle(msg.channel, msg.value)

rospy.Subscriber('/duty_cycle', DutyCycle, handle_msg)

rospy.spin()

pwm.cancel()
pi.stop()
