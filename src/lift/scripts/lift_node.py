#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import pigpio
from pwm_driver.msg import DutyCycle

pi = pigpio.pi()

rospy.init_node('lift_node')

pub = rospy.Publisher('/pwm1/duty_cycle', DutyCycle, queue_size=10)

lift_up_sensor_pin = int(rospy.get_param('/pins/lift_up_sensor_pin'))
lift_down_sensor_pin = int(rospy.get_param('/pins/lift_down_sensor_pin'))
lift_up_channel = int(rospy.get_param('/pins/lift_up_channel'))
lift_down_channel = int(rospy.get_param('/pins/lift_down_channel'))

rate = rospy.Rate(50)
position = 'down'
direction = 'stop'

def activate_motor():
    if direction == 'stop':
        print 'motor stop'
        pub.publish(DutyCycle(lift_up_channel, 0))
        pub.publish(DutyCycle(lift_down_channel, 0))

    elif direction == 'up':
        print 'motor up'
        pub.publish(DutyCycle(lift_up_channel, 100))
        pub.publish(DutyCycle(lift_down_channel, 0))

    elif direction == 'down':
        print 'motor down'
        pub.publish(DutyCycle(lift_up_channel, 0))
        pub.publish(DutyCycle(lift_down_channel, 100))


def handle_msg(msg):
    global direction

    if position != msg.data:
        direction = msg.data


rospy.Subscriber('/lift', String, handle_msg)

def handle_sensor_change(gpio, level, tick):
    global direction
    direction = 'stop'


pi.callback(lift_up_sensor_pin, pigpio.EITHER_EDGE, handle_sensor_change)
pi.callback(lift_down_sensor_pin, pigpio.EITHER_EDGE, handle_sensor_change)

old_direction = direction

while not rospy.is_shutdown():
    if old_direction != direction:
        position = old_direction
        activate_motor()
        print 'position = ' + position

    old_direction = direction
    rate.sleep()

pi.stop()
