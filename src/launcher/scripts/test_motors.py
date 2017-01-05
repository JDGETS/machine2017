#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from pwm_driver.msg import PulseWidth, DutyCycle
import sys

rospy.init_node('test_motors')

angle_up = rospy.Publisher('/launcher/angle_up', Float32, queue_size=10)
pwm = rospy.Publisher('/pulse_width', PulseWidth, queue_size=10)

init_value = 750
speed = 990 - init_value
# 890 - 990, 5

rate = rospy.Rate(10)

while not rospy.is_shutdown():
    angle_up.publish(Float32(0.0))
    
    rate.sleep()
