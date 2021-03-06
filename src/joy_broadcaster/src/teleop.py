#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool, Empty
from sensor_msgs.msg import Joy
import rospkg
import subprocess
from topic_tools.srv import MuxSelect

FORWARD = 1
BACKWARDS = 2
SPINNING = 3
STOPPED = 4

'''
buttons = [
A,
B,
X,
Y,
LB,
RB,
Back,
Start,
Logitech,
Analog Left Click,
Analog Right Click
]

axes = [
Analog Left X,
Analog Left Y,
LT (1: released, -1: fully pressed),
Analog Right X,
Analog Right Y,
RT (1: released, -1: fully pressed),
Arrow x,
Arrow y
]
'''

buttons = {"left": "axes:0:+",
           "right": "axes:0:-",
           "accelerate": "axes:7:+",
           "deccelerate": "axes:7:-",
           "forward": "buttons:1",
           "backwards": "buttons:0",
           "spin_left": "buttons:4",
           "spin_right": "buttons:5",
           "change_state": "buttons:8",
           "toggle_elevator": "buttons:6",
           "launch_ball": "buttons:2",
           "recup_ball": "buttons:3"}

linear_increment = 0.1
max_linear_vel = 0.85
min_linear_vel = -0.85
default_linear_vel = 0.3

angular_increment = 0.5
max_angular_vel = 1

spin_speed = 3.0

last_joy_message = None
linear_vel = 0.0
angular_vel = 0.0
last_angular_acceleration = 0
rotating = False
state = STOPPED

# states = [booting, sur le terrain, autonomous, manuel]
robot_state = 0

scan_mux = rospy.ServiceProxy('/scan_mux_select', MuxSelect)
cmd_vel_mux = rospy.ServiceProxy('/cmd_vel_select', MuxSelect)
elevator_pub = rospy.Publisher('/balls/grab', Bool, queue_size=10)

launch_ball = rospy.Publisher('/launcher/launch', Empty, queue_size=10)
recup_ball = rospy.Publisher('/launcher/recup', Empty, queue_size=10)
ai_start = rospy.Publisher('/ai/start', Empty, queue_size=10)

elevator = False

def activate_scan():
    scan_mux('/scan_raw')

def disable_autonomous():
    cmd_vel_mux('/cmd_vel_man')

def process_input(msg):
    global FORWARD, BACKWARDS, SPINNING, STOPPED

    forward = get_button_value(msg, "forward") > 0
    backwards = get_button_value(msg, "backwards") > 0
    left = get_button_value(msg, "left") > 0
    right = get_button_value(msg, "right") > 0
    #rospy.loginfo(msg)

    if forward or backwards:
        if forward:
            change_state(FORWARD)
        elif backwards:
            change_state(BACKWARDS)
            #Inverser la direction si on recule
            tmpleft = left
            left = right
            right = tmpleft

        if get_button_value(msg, "accelerate") > 0:
            increment_linear_vel()
        elif get_button_value(msg, "deccelerate") > 0:
            decrement_linear_vel()

        if backwards and linear_vel > 0 or forward and linear_vel < 0:
            reset_linear_vel()

        if left:
            start_rotation(True)
        elif right:
            start_rotation(False)
        else:
            stop_rotation()
    else:
        spin_left = get_button_value(msg, "spin_left") > 0
        spin_right = get_button_value(msg, "spin_right") > 0
        if spin_left or spin_right:
            change_state(SPINNING)
            start_rotation(spin_left, True)
        else:
            change_state(STOPPED)

    global robot_state

    if get_button_value(msg, "change_state") > 0:
        print robot_state

        if robot_state < 3:
            robot_state += 1

        if robot_state == 1:
            activate_scan()
            pass

        if robot_state == 2:
            ai_start.publish(Empty())
            pass

        if robot_state == 3:
            disable_autonomous()
            pass


    global elevator
    if get_button_value(msg, "toggle_elevator") > 0:
        elevator = not elevator

        elevator_pub.publish(Bool(elevator))

    if get_button_value(msg, "recup_ball") > 0:
        recup_ball.publish(Empty())

    if get_button_value(msg, "launch_ball") > 0:
        launch_ball.publish(Empty())

def change_state(new_state):
    global linear_vel, default_linear_vel, state
    if state != new_state:
        if new_state == FORWARD:
            linear_vel = default_linear_vel
        elif new_state == BACKWARDS:
            linear_vel = -default_linear_vel
        else:
            linear_vel = 0
            stop_rotation()
        state = new_state


def increment_linear_vel():
    global linear_vel, linear_increment, max_linear_vel
    if linear_vel + linear_increment > max_linear_vel:
        linear_vel = max_linear_vel
    else:
        linear_vel = linear_vel + linear_increment
    if abs(linear_vel) < linear_increment:
        linear_vel = 0.0


def decrement_linear_vel():
    global linear_vel, linear_increment, min_linear_vel
    if linear_vel - linear_increment < min_linear_vel:
        linear_vel = min_linear_vel
    else:
        linear_vel = linear_vel - linear_increment
    if abs(linear_vel) < linear_increment:
        linear_vel = 0.0


def start_rotation(left, spin=False):
    global angular_increment, angular_vel, rotating, spin_speed

    if spin:
        angular_vel = (1.0 if left else -1.0) * spin_speed
    else:
        if left and angular_vel <= 0.0:
            angular_vel = angular_increment
        elif not left and angular_vel >= 0.0:
            angular_vel = -angular_increment

    rotating = True


def stop_rotation():
    global angular_vel, rotating
    angular_vel = 0.0
    rotating = False


def accelerate_rotation():
    global angular_vel, angular_increment, max_angular_vel, last_angular_acceleration, rotating

    diff = rospy.get_time() - last_angular_acceleration
    absvel = abs(angular_vel)

    if diff > 0.1 and rotating and max_angular_vel - absvel > 0.01:
        angular_vel += angular_increment * (absvel / angular_vel)
        last_angular_acceleration = rospy.get_time()


def reset_linear_vel():
    global linear_vel
    linear_vel = 0.0


def has_new_input(msg):
    global last_joy_message
    if last_joy_message:
        for i in range(len(msg.buttons)):
            if msg.buttons[i] != last_joy_message.buttons[i]:
                return True
        for i in range(len(msg.axes)):
            if msg.axes[i] != last_joy_message.axes[i]:
                return True
    else:
        return True

    return False


def get_button_value(msg, name):
    global buttons
    split = buttons[name].split(":")
    val = getattr(msg, split[0])[int(split[1])]
    if len(split) == 2:
        return val
    else:
        if split[2] == "+" and val > 0:
            return 1
        elif split[2] == "-" and val < 0:
            return 1
        else:
            return 0


def joy_callback(msg):
    global last_joy_message
    #rospy.loginfo("joy callback: " + str(msg))
    #if has_new_input(msg):
    process_input(msg)
    last_joy_message = msg


def cmd_vel_timer(event):
    global linear_vel, angular_vel, cmd_vel_publisher, state, FORWARD, BACKWARDS

    if state == FORWARD or state == BACKWARDS:
        accelerate_rotation()

    msg = Twist()
    msg.linear.x = linear_vel
    msg.angular.z = angular_vel

    cmd_vel_publisher.publish(msg)


rospy.init_node('teleop')

rospy.Subscriber("/joy", Joy, joy_callback)
cmd_vel_publisher = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
rospy.Timer(rospy.Duration.from_sec(15.0/1000), cmd_vel_timer)


rospy.spin()
