#!/usr/bin/env python

import rospy
from std_msgs.msg import Byte, Float32
import tf
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
from geometry_msgs.msg import PolygonStamped, Polygon, Point32
from nav_msgs.msg import Path
import projectile_solver as launcher
import numpy as np
import math
from pwm_driver.msg import DutyCycle

rospy.init_node('place_launcher')

listener = tf.TransformListener()

ball_trajectory = rospy.Publisher('/ball_trajectory', PolygonStamped, queue_size=10)
angle_base = rospy.Publisher('/launcher/angle_base', Float32, queue_size=10)
angle_up = rospy.Publisher('/launcher/angle_up', Float32, queue_size=10)


def handle_msg(msg):
    goal_tf = "goal%d_ring" % msg.data
    now = rospy.Time.now()

    try:
        listener.waitForTransform("base_link", goal_tf, now, rospy.Duration(1.5))
        (goal_pos, _) = listener.lookupTransform("map", goal_tf, now)
        (robot_trans, rot) = listener.lookupTransform("base_link", goal_tf, now)
        rot = tf.transformations.euler_from_quaternion(rot)

        a = math.atan2(robot_trans[1], robot_trans[0])


        angle_base.publish(Float32(a))

        (launcher_pos, _) = listener.lookupTransform("map", "launcher_base", now)

        v0, phi, t = launcher.findvelocityandangle(launcher_pos[0], launcher_pos[1], launcher_pos[2], Point32(*goal_pos))

        angle_up.publish(Float32(-phi))

        msg = PolygonStamped()
        msg.header.frame_id = 'map'
        msg.header.stamp = now

        now = rospy.Time.now()
        listener.waitForTransform("map", "launcher_tip", now, rospy.Duration(1.5))
        (launcher_pos, rot) = listener.lookupTransform("map", "launcher_tip", now)
        (_, phi, a) = tf.transformations.euler_from_quaternion(rot)

        x0 = np.array(launcher_pos)
        f0 = np.array([math.cos(a),
                       math.sin(a),
                       math.sin(-phi)]) * v0

        for t in np.arange(0, 2, 0.01):
            xt = f0 * t + launcher_pos
            xt[2] -= 0.5 * t * t * 9.81

            msg.polygon.points.append(Point32(*xt))

        ball_trajectory.publish(msg)

    except Exception as e:
        rospy.logerr(e)
        pass


rospy.Subscriber('/place_launcher', Byte, handle_msg)

rospy.spin()
