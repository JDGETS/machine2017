#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

global pub

def callback(data):
	twist = Twist()
	twist.linear.x = 4*data.axes[1]
	twist.angular.z = 4*data.axes[0]
	pub.publish(twist)

pub = rospy.Publisher('turtle1/cmd_vel', Twist)
rospy.Subscriber("joy", Joy, callback)
rospy.init_node("Joy2Turtle")
rospy.spin()


