#! /usr/bin/env python

import rospy

import actionlib

import action_server.msg

import time

class GrimpeSequenceAction(object):
    _feedback = action_server.msg.monte_poteauActionFeedback()
    _result = action_server.msg.monte_poteauActionResult()

    def __init__(self, name):
        self._dispatcher = {1 : self.step1,
		    2 : self.step2,
			3 : self.step3,
			4 : self.step4,
			5 : self.step5,
			6 : self.step6
			}
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, action_server.msg.monte_poteauAction, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()

    def execute_cb(self, goal):
        r = rospy.Rate(1)
        rospy.loginfo("Executing goal")
        self._dispatcher[goal.transition]()
        
        self._as.set_suceeded(self._result)

    def step1():
        rospy.loginfo("Running step1")
        time.sleep(1)
        

    def step2():
        rospy.loginfo("Running step2")
        time.sleep(1)

    def step3():
        rospy.loginfo("Running step3")
        time.sleep(1)

    def step4():
        rospy.loginfo("Running step4")
        time.sleep(1)

    def step5():
        rospy.loginfo("Running step5")
        time.sleep(1)

    def step6():
        rospy.loginfo("Running step6")
        time.sleep(1)

if __name__ == '__main__':
    rospy.init_node('GrimpeSequenceActionServer')
    server = GrimpeSequenceAction(rospy.get_name())
    rospy.spin()

