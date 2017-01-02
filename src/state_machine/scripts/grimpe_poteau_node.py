#!/usr/bin/env python

import roslib
import rospy
import smach
import smach_ros
import time
from std_msgs.msg import String
from sensor_msgs.msg import Joy
"""
Grimpe poteau state machine
States:
 E1
 E2
 E3
 E4
 E5
 E6
"""


# define state
class E1(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1'])
        self.pub_pince = rospy.Publisher('/pince', String, queue_size=10)
        self.pub_scissor = rospy.Publisher('/scissor', String, queue_size=10)
        self.sub_scissor = rospy.Subscriber('/scissor', String, self.callback)
        self.scissor_lift_state = "lower"

    def execute(self, userdata):
        """
        Ouvrir pince
        Monter Scissor lift
        :param userdata:
        :return:
        """
        rospy.loginfo('Executing state E1')
        rate = rospy.Rate(10)  # 10hz
        message_pince = String()
        message_pince.data = "open"
        message_scissor = String()
        message_scissor.data = "rise"
        rospy.loginfo(message_pince)
        rospy.loginfo(message_scissor)
        while not rospy.is_shutdown() and self.scissor_lift_state == 'lower':
            self.pub_pince.publish(message_pince)
            self.pub_scissor.publish(message_scissor)
            rate.sleep()

        return 'outcome1'

    def callback(self, data):
        if data.data == "risen":
            self.scissor_lift_state = "risen"


class E2(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome2'])
        self.pub_scissor = rospy.Publisher('/scissor', String, queue_size=10)
        self.rospy.Subscriber("/joy", Joy, joy_callback)
        self.transition = False

    def execute(self, userdata):
        """
        Avance le robot
        Arret ouverture pince
        Arret monte scissorlift
        :param userdata:
        :return:
        """
        rospy.loginfo('Executing state E2')
        rate = rospy.Rate(10)  # 10hz
        message_scissor = String()
        message_scissor.data = "stop"
        rospy.loginfo(message_scissor)

        while not rospy.is_shutdown():
            self.pub_scissor.publish(message_scissor)
            rate.sleep()

        if self.transition == True:
            return 'outcome2'


class E3(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome3'])
        self.pub_pince = rospy.Publisher('/pince', String, queue_size=10)
        self.transition = False

    def execute(self, userdata):
        """
        Ferme pince
        :param userdata:
        :return:
        """
        rospy.loginfo('Executing state E3')
        rate = rospy.Rate(10)  # 10hz
        message_pince = String()
        message_pince.data = "close"
        rospy.loginfo(message_pince)
        self.pub_pince.publish(message_pince)
        rate.sleep()
        if self.transition == True:
            return 'outcome3'


class E4(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome4'])
        self.pub_magnet = rospy.Publisher('/magnet', String, queue_size=10)
        self.pub_scissor = rospy.Publisher('/scissor', String, queue_size=10)
        self.transition = False

    def execute(self, userdata):
        """
        Active Electroaimant
        Descendre scissor lift
        :param userdata:
        :return:
        """
        rospy.loginfo('Executing state E4')
        rate = rospy.Rate(10)  # 10hz
        message_magnet = String()
        message_magnet.data = "activate"
        message_scissor = String()
        message_scissor.data = "lower"
        rospy.loginfo(message_magnet)
        rospy.loginfo(message_scissor)
        self.pub_magnet.publish(message_magnet)
        self.pub_scissor.publish(message_scissor)

        rate.sleep()
        if self.transition == True:
            return 'outcome4'

class E5(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome5'])
        self.pub_magnet = rospy.Publisher('/magnet', String, queue_size=10)
        self.pub_intake = rospy.Publisher('/intake', String, queue_size=10)
        self.transition = False

    def execute(self, userdata):
        """
        Active electroaimant
        Active moteur moissoneuse
        Arret forward robot
        :param userdata:
        :return:
        """
        rospy.loginfo('Executing state E5')
        rate = rospy.Rate(10)  # 10hz
        message_magnet = String()
        message_magnet.data = "activate"
        message_intake = String()
        message_intake.data = "run"
        rospy.loginfo(message_magnet)
        rospy.loginfo(message_intake)
        self.pub_magnet.publish(message_magnet)
        self.pub_intake.publish(message_intake)

        rate.sleep()
        if self.transition == True:
            return 'outcome5'


class E6(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome6'])
        self.pub_intake = rospy.Publisher('/intake', String, queue_size=10)
        self.transition = False

    def execute(self, userdata):
        """
        Arret moteur moissoneuse
        :param userdata:
        :return:
        """
        rospy.loginfo('Executing state E6')
        rate = rospy.Rate(10)  # 10hz
        message_intake = String()
        message_intake.data = "run"
        rospy.loginfo(message_intake)
        self.pub_intake.publish(message_intake)

        rate.sleep()

        if self.transition == True:
            return 'outcome6'


def main():
    rospy.init_node('grimpe_poteau_state_machine')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['outcome6'])

    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('E1', E1(),
                               transitions={'outcome1': 'E2'})
        smach.StateMachine.add('E2', E2(),
                               transitions={'outcome2': 'E3'})
        smach.StateMachine.add('E3', E3(),
                               transitions={'outcome3': 'E4'})
        smach.StateMachine.add('E4', E4(),
                               transitions={'outcome4': 'E5'})
        smach.StateMachine.add('E5', E5(),
                               transitions={'outcome5': 'E6'})
        smach.StateMachine.add('E6', E6(),
                               transitions={'outcome6': 'outcome6'})
    # Execute SMACH plan
    outcome = sm.execute()


if __name__ == '__main__':
    main()