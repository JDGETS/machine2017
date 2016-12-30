#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import pigpio

pi = pigpio.pi()

pi.set_mode(26, pigpio.INPUT)
pi.set_mode(27, pigpio.INPUT)

rospy.init_node('lift_node')

rate = rospy.Rate(50)
direction = 'stop'

def handle_msg(msg):
    global direction
    direction = msg.data

rospy.Subscriber('/lift', String, handle_msg)

def handle_sensor_change(gpio, level, tick):
    global direction
    print 'change ' + str(gpio) + ' ' + str(level)
    direction = 'stop'


pi.callback(26, pigpio.EITHER_EDGE, handle_sensor_change)
pi.callback(27, pigpio.EITHER_EDGE, handle_sensor_change)

old_direction = direction

while not rospy.is_shutdown():
    if old_direction != direction:
        print direction

    old_direction = direction
    rate.sleep()

pi.stop()
