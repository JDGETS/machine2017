#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32

rospy.init_node('koi')

def handle_msg(msg):
    print msg

rospy.Subscriber('/launcher/angle_up', Float32, handle_msg)

rospy.spin()
