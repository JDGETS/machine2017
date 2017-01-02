#!/usr/bin/env python

import roslib
import roslib.load_manifest('smach_tutorials')
import rospy
import smach
import smach_ros
import time

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


    def execute(self, userdata):
        """
        Ouvrir pince
        Monter Scissor ift
        :param userdata:
        :return:
        """
        rospy.loginfo('Executing state E1')
        time.sleep(2)
        return 'outcome1'

class E2(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome2'])
        self.counter = 0

    def execute(self, userdata):
        """
        Avance le robot
        Arret ouverture pince
        Arret monte scissorlift
        :param userdata:
        :return:
        """
        rospy.loginfo('Executing state E2')
        time.sleep(2)
        return 'outcome2'

class E3(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome3'])
        self.counter = 0

    def execute(self, userdata):
        """
        Ferme pince
        :param userdata:
        :return:
        """
        rospy.loginfo('Executing state E3')
        time.sleep(2)
        return 'outcome3'

class E4(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome4'])
        self.counter = 0

    def execute(self, userdata):
        """
        Active Electroaimant
        Descendre scissor lift
        :param userdata:
        :return:
        """
        rospy.loginfo('Executing state E4')
        time.sleep(2)
        return 'outcome4'

class E5(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome5'])
        self.counter = 0

    def execute(self, userdata):
        """
        Active electroaimant
        Active moteur moissoneuse
        Arret forward robot
        :param userdata:
        :return:
        """
        rospy.loginfo('Executing state E5')
        time.sleep(2)
        return 'outcome5'

class E6(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome6'])
        self.counter = 0

    def execute(self, userdata):
        """
        Arret moteur moissoneuse
        :param userdata:
        :return:
        """
        rospy.loginfo('Executing state E6')
        time.sleep(2)
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