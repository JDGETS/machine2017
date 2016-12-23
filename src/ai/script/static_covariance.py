#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped

rospy.init_node('static_covariance')

pub = rospy.Publisher('/pose_cov', PoseWithCovarianceStamped, queue_size=10)

def pose_cb(msg):
    # (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)
    msg.pose.covariance = [
        0.004, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.004, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0121847027
    ]
    pub.publish(msg)

rospy.Subscriber('/pose', PoseWithCovarianceStamped, pose_cb)

rospy.spin()
