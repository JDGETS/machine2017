#!/usr/bin/env python

import rospy
from pwm_driver.msg import PulseWidth
from std_msgs.msg import Float32, Byte, Bool, Empty
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

trigger_channel = rospy.get_param('/pins/launcher_trigger_channel', 5)

pub = rospy.Publisher('/pulse_width', PulseWidth, queue_size=10)

pub.publish(PulseWidth(motor_left_channel, 750))
pub.publish(PulseWidth(motor_right_channel, 750))

# True if trigger is open
# False if trigger is closed
trigger_state = False

rospy.sleep(3)

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
    angle = int(2.7314 * angle + 1675)

    pub.publish(PulseWidth(angle_base_channel, angle))


def handle_angle_up(msg):
    pente = -10.422
    offset = 2159.2
    angle = pente * msg.data + offset

    pub.publish(PulseWidth(angle_up_channel, angle))


def handle_trigger(msg):
    global trigger_state
    trigger_state = msg.data

    if trigger_state:
        pub.publish(PulseWidth(trigger_channel, 550))
    else:
        pub.publish(PulseWidth(trigger_channel, 2300))


def handle_launch(msg):
    handle_trigger(Bool(True))
    rospy.sleep(1)
    handle_trigger(Bool(False))


rospy.Subscriber('/launcher/speed', Float32, handle_speed)
rospy.Subscriber('/launcher/angle_base', Float32, handle_angle_base)
rospy.Subscriber('/launcher/angle_up', Float32, handle_angle_up)
rospy.Subscriber('/launcher/trigger', Bool, handle_trigger)

rospy.Subscriber('/launcher/launch', Empty, handle_launch)

rospy.spin()
