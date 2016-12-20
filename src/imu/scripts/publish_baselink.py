#!/usr/bin/env python

import rospy
import tf
from geometry_msgs.msg import Quaternion, PoseStamped, Pose

rospy.init_node('publish_baselink')

br = tf.TransformBroadcaster()

def pose_cb(msg):
    global q
    t = msg.header.stamp
    qw = msg.pose.orientation
    q = [qw.x, qw.y, qw.z, qw.w]
    br.sendTransform((0, 0, 0), q, t, 'laser', 'base_link')


rospy.Subscriber('/imu_pose', PoseStamped, pose_cb)

rospy.spin()
