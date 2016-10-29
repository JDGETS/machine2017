#!/usr/bin/env python

import rospy
from pin_test.srv import *
import pigpio

pi = pigpio.pi()

pi.set_mode(17, pigpio.OUTPUT)

rospy.init_node('toggle_led')

def handle_led_state(req):
	if req.open:
		pi.write(17, 1)
	else:
		pi.write(17, 0)

	return LedStateResponse()

rospy.Service('/set_led_state', LedState, handle_led_state)

rospy.spin()
