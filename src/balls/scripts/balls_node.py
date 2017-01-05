#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool
from pwm_driver.msg import DutyCycle

rospy.init_node('balls_node')

moissoneuse_channel = rospy.get_param('/pins/moissoneuse_channel', 6)
elevator_channel = rospy.get_param('/pins/elevator_channel', 4)

grabbing_state = False
pub = rospy.Publisher('/duty_cycle', DutyCycle, queue_size=10)

def handle_grab(msg):
    global grabbing_state
    grabbing_state = msg.data

    if grabbing_state:
        print 'grabbing'
        pub.publish(DutyCycle(moissoneuse_channel, 50))
        pub.publish(DutyCycle(elevator_channel, 100))
    else:
        print 'stop grabbing'
        pub.publish(DutyCycle(moissoneuse_channel, 0))
        pub.publish(DutyCycle(elevator_channel, 0))


rospy.Subscriber('/balls/grab', Bool, handle_grab)

rospy.spin()
