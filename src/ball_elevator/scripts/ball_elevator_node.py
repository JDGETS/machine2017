#!/usr/bin/env python

import rospy
from std_msgs.msg import Byte, String
from pwm_driver.msg import PulseWidth

import pigpio

lift_bas = 7
lift_haut = 8
lanceur = 9

COUNT = 0

rate = rospy.Rate(30)

def update_count(msg):
    global COUNT
    COUNT = msg.data

def get_angle_from_TF():
    # TODO, get value from tf compare
    return 0


if __name__ == '__main__':
    pi = pigpio()
    motor_elevator_channel = rospy.get_param('/pins/elevator_channel', ???)  # See Google sheet for pin mapping
    kicker_elevator_channel = rospy.get_param('/pins/elevator_kicker_channel', ???)
    pub_elevator = rospy.Publisher('/ball_elevator', String, queue_size=10)
    pub_servo_kickball = rospy.Publisher('/kick_it', String, queue_size=10)
    pub_elevator.publish(PulseWidth(motor_elevator_channel, ???))

    rospy.Subscriber('/ball_count', Byte, update_count)
    while not rospy.is_shutdown():
        """
        Motor always on
        DeActivate motor when:
        C2 and C3 and AngleVert != fulldown and AngleHori != PositionINit
        """
        global COUNT
        if pi.read(lift_haut) and pi.read(lanceur):# and ...:
            if COUNT == 1:
                # TODO: Publish on servo to push ball in launcher
                pub_servo_kickball.publish(PulseWidth(kicker_elevator_channel, ???))
            pub_elevator.publish(PulseWidth(motor_elevator_channel, ???))