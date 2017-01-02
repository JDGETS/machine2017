#!/usr/bin/env python

import rospy
from std_msgs.msg import Byte

import pigpio

pub = rospy.Publisher('/ball_count', Byte, queue_size=10)

msg1 = Byte(98)

rate = rospy.Rate(30)

pi = pigpio.pi()
"""
Sensors are inversed
"""
lift_bas = 7
lift_haut = 8
lanceur = 9

c1_state = 1
c2_state = 1
count = 0

while not rospy.is_shutdown():
    if pi.read(lift_bas) == 0:
        c1_state = 0
    elif c1_state == 0 and pi.read(lift_bas) == 1:
        count += 1
        c1_state = 1

    if pi.read(lift_haut) == 0:
        c2_state = 0
    elif c2_state == 0 and pi.read(lift_haut) == 1:
        count -= 1
        current_state = 1

    pub.publish(count)
    rate.sleep()

pi.stop()
