#!/usr/bin/env python

import rospy
from pwm_driver.msg import PulseWidth
from std_msgs.msg import Float32, Byte
import pigpio
import time

lift_bas = 7
lift_haut = 8
lanceur = 9

rospy.init_node('launcher_node')

motor_left_channel = rospy.get_param('/pins/launcher_motor_left_channel', 13)
motor_right_channel = rospy.get_param('/pins/launcher_motor_right_channel', 14)

angle_base_channel = rospy.get_param('/pins/launcher_base_channel', 10)
angle_up_channel = rospy.get_param('/pins/launcher_up_channel', 11)

pub = rospy.Publisher('/pulse_width', PulseWidth, queue_size=10)

pub.publish(PulseWidth(motor_left_channel, 750))
pub.publish(PulseWidth(motor_right_channel, 750))

rospy.sleep(3)

COUNT = 0

def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def handle_speed(msg):
    speed = msg.data
    micro = 750

    if speed > 0:
        micro = int(speed * 5.0 + 885)

    pub.publish(PulseWidth(motor_left_channel, micro))
    pub.publish(PulseWidth(motor_right_channel, micro))


def handle_angle_base(msg):
    angle = msg.data
    # todo: correction angle avec mapping
    global COUNT
    pi = pigpio()

    if pi.read(lanceur) == 1:
        time.sleep(1)
        angle = 0

    angle = getAngleFromTF()

    pub.publish(PulseWidth(angle_base_channel, angle))

def getAngleFromTF():
    # TODO, get value from tf compare
    return 0

def handle_angle_up(msg):
    angle = msg.data
    angle = -10.422 * angle + 2159.2

    pub.publish(PulseWidth(angle_base_channel, angle))

def update_count(msg):
    global COUNT
    COUNT = msg.data


rospy.Subscriber('/launcher/speed', Float32, handle_speed)
rospy.Subscriber('/launcher/angle_base', Float32, handle_angle_base)
rospy.Subscriber('/launcher/angle_up', Float32, handle_angle_up)
rospy.Subscriber('/ball_count', Byte, update_count)

rospy.spin()
