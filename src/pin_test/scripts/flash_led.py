#!/usr/bin/env python

import rospy
from pin_test.srv import LedState

rospy.init_node('flash_led')

set_state = rospy.ServiceProxy('/set_led_state', LedState)
state = False

while not rospy.is_shutdown():
	set_state(state)
	state = not state
	rospy.sleep(1)
