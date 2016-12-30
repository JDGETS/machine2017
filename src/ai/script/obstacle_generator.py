#!/usr/bin/env python

import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
import numpy as np
from std_msgs.msg import Header

rospy.init_node('obstacle_generator')

pub = rospy.Publisher('/fake_walls', PointCloud2, queue_size=10)
rate = rospy.Rate(30)
center = np.array((1.524, 0.762, 0))


while not rospy.is_shutdown():
    points = []
    header = Header()
    header.frame_id = 'world'
    header.stamp = rospy.Time.now()

    for x in np.arange(-0.4826, 0.4826, 0.01):
        points.append(center + np.array([0, x, 0]))

    msg = pc2.create_cloud_xyz32(header, points)

    pub.publish(msg)

    rate.sleep()
