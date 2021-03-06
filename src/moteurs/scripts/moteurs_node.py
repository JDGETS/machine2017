#!/usr/bin/env python

import rospy
from pwm_driver.msg import DutyCycle
from geometry_msgs.msg import Twist
from std_msgs.msg import String

rospy.init_node('moteurs')

# PWM channels
left_forward = rospy.get_param('/pins/motors_left_forward', 0)
left_backward = rospy.get_param('/pins/motors_left_backward', 1)
right_forward = rospy.get_param('/pins/motors_right_forward', 2)
right_backward = rospy.get_param('/pins/motors_right_backward', 3)
robot_width = float(rospy.get_param('~robot_width', 0.3))
max_speed = float(rospy.get_param('~max_speed', 0.9))

pub = rospy.Publisher('/duty_cycle', DutyCycle, queue_size=10)

def clamp(x, a, b):
    return max(min(x, b), a)

def handle_speed(forward, backward, speed):
    if speed == 0:
        pub.publish(DutyCycle(backward, 0))
        pub.publish(DutyCycle(forward, 0))

    elif speed > 0:
        pub.publish(DutyCycle(backward, 0))
        pub.publish(DutyCycle(forward, speed))
    else:
        pub.publish(DutyCycle(backward, abs(speed)))
        pub.publish(DutyCycle(forward, 0))


def handle_cmd_vel(msg):
    speed = msg.linear.x
    angular = msg.angular.z

    left_speed = (speed - angular * robot_width * 0.5)
    right_speed = (speed + angular * robot_width * 0.5)

    right_speed *= 1.3

    left_speed /= max_speed
    right_speed /= max_speed

    left_speed = clamp(left_speed, -1, 1) * 100
    right_speed = clamp(right_speed, -1, 1) * 100


    handle_speed(left_forward, left_backward, left_speed)
    handle_speed(right_forward, right_backward, right_speed)


rospy.Subscriber('/cmd_vel', Twist, handle_cmd_vel)

rospy.spin()
