#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import *

rospy.init_node('autonomous')

server = actionlib.SimpleActionClient('/move_base', MoveBaseAction)

goal = MoveBaseGoal()
goal.target_pose.pose.position.x = 1
goal.target_pose.pose.position.y = 0.2

goal.target_pose.pose.orientation.w = 1
goal.target_pose.header.frame_id = 'world'
goal.target_pose.header.stamp = rospy.Time.now()

print 'waiting for server'
server.wait_for_server()

print 'send_goal'
server.send_goal(goal)

print 'wait...'
server.wait_for_result()

print 'result'
print server.get_result()

rospy.spin()
