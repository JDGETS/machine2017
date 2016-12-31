#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

rospy.init_node('invert_scan')

pub = rospy.Publisher('/scan', LaserScan, queue_size=10)

def handle_scan(msg):
    msg.ranges = msg.ranges[::-1]
    pub.publish(msg)

rospy.Subscriber('/scan_raw', LaserScan, handle_scan)

rospy.spin()
