#!/usr/bin/env python

import rospy
import tf
import math
from std_msgs.msg import Float32

rospy.init_node('launcher_tf')

angle_base = 0
angle_up = 0

rate = rospy.Rate(40)
br = tf.TransformBroadcaster()

def handle_angle_base(msg):
    global angle_base
    angle_base = msg.data


def handle_angle_up(msg):
    global angle_up
    angle_up = msg.data


rospy.Subscriber('/angle_base', Float32, handle_angle_base)
rospy.Subscriber('/angle_up', Float32, handle_angle_up)

while not rospy.is_shutdown():
    angle = tf.transformations.quaternion_from_euler(0, 0, angle_base)

    br.sendTransform((0, 0, 0),
                     angle,
                     rospy.Time.now(),
                     "launcher_base",
                     "launcher")

    angle = tf.transformations.quaternion_from_euler(0, angle_up, 0)
    br.sendTransform((-0.05, 0, 0),
                     angle,
                     rospy.Time.now(),
                     "launcher_elevation",
                     "launcher_base")

    rate.sleep()
