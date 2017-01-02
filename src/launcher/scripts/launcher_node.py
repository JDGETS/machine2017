#!/usr/bin/env python

import rospy
from pwm_driver.msg import PulseWidth
from std_msgs.msg import Float32

rospy.init_node('launcher_node')

motor_left_channel = rospy.get_param('/pins/launcher_motor_left_channel', 13)
motor_right_channel = rospy.get_param('/pins/launcher_motor_right_channel', 14)

angle_base_channel = rospy.get_param('/pins/launcher_base_channel', 10)
angle_up_channel = rospy.get_param('/pins/launcher_up_channel', 11)

pub = rospy.Publisher('/pulse_width', PulseWidth, queue_size=10)

pub.publish(PulseWidth(motor_left_channel, 750))
pub.publish(PulseWidth(motor_right_channel, 750))

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
    # todo
    pass

def handle_angle_up(msg):
    angle = msg.data
    angle = -10.422 * angle + 2159.2

    pub.publish(PulseWidth(angle_base_channel, angle))


rospy.Subscriber('/launcher/speed', Float32, handle_speed)
rospy.Subscriber('/launcher/angle_base', Float32, handle_angle_base)
rospy.Subscriber('/launcher/angle_up', Float32, handle_angle_up)

rospy.spin()
