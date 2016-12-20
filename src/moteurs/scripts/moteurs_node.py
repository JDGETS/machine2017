#!/usr/bin/env python

import rospy
from pwm_driver.srv import SetDutyCycle
from geometry_msgs.msg import Twist

rospy.init_node('moteurs')

# PWM channels
left_forward = rospy.get_param('~left_forward', 0)
left_backward = rospy.get_param('~left_backward', 1)
right_forward = rospy.get_param('~right_forward', 2)
right_backward = rospy.get_param('~right_backward', 3)

channels = [left_forward, left_backward, right_forward, right_backward]

set_duty_cycle = rospy.ServiceProxy('set_duty_cycle', SetDutyCycle)


def callback(data):
    twist = Twist()
    twist.linear.x = 4*data.axes[1]
    twist.angular.z = 4*data.axes[0]
    pub.publish(twist)

def handle_speed(forward, backward, speed):
    if speed > 0:
        set_duty_cycle(backward, 0)
        set_duty_cycle(forward, 100)
    else:
        set_duty_cycle(backward, 100)
        set_duty_cycle(forward, 0)


def handle_cmd_vel(msg):
    speed = msg.linear.x
    angular = msg.angular.z

    left_speed = 0
    right_speed = 0

    if abs(speed) > 0:
        if speed > 0:
            left_speed = 1
            right_speed = 1
        else:
            left_speed = -1
            right_speed = -1
    else:
        for channel in channels:
            set_duty_cycle(channel, 0)
        return

    handle_speed(left_forward_channel, left_backward_channel, left_speed)
    handle_speed(right_forward_channel, right_backward_channel, right_speed)


rospy.Subscriber('/cmd_vel', Twist, handle_cmd_vel)

rospy.spin()
