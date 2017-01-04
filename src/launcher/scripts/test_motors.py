#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from pwm_driver.msg import PulseWidth

rospy.init_node('test_motors')

angle_up = rospy.Publisher('/launcher/angle_up', Float32, queue_size=10)
pwm = rospy.Publisher('/pulse_width', Pulsewidth, queue_size=10)
init_value = 750
speed = 890 - init_value
# 890 - 990, 5

angle_up.pub(Float32(55.0))

rospy.sleep(2)

pwm.publish(PulseWidth(13, init_value))
pwm.publish(PulseWidth(14, init_value))

rospy.sleep(3)

print init_value + speed
pwm.publish(PulseWidth(13, init_value + speed))
pwm.publish(PulseWidth(14, init_value + speed))

rospy.sleep(3)

pwm.publish(PulseWidth(5, 200))

rospy.sleep(1)

pwm.publish(PulseWidth(13, init_value))
pwm.publish(PulseWidth(14, init_value))

pwm.publish(PulseWidth(5, 800))
