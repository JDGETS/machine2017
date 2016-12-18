#!/usr/bin/env python

import rospy
import smbus
import math
from sensor_msgs.msg import Imu
from tf.transformations import quaternion_from_euler
from geometry_msgs.msg import Quaternion, PoseStamped, Pose
from sensor_msgs.msg import Imu
import time

rospy.init_node('mpu6050')

pub = rospy.Publisher('/imu', Imu, queue_size=10)
pub_pose = rospy.Publisher('/imu_pose', PoseStamped, queue_size=10)
rate = rospy.Rate(30)

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
address = 0x68       # This is the address value read via the i2cdetect command

# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)

rx, ry, rz = 0, 0, 0
last_time = time.time()

drift_x = 0
drift_y = 0
drift_z = 0

rospy.loginfo("Measuring average drift of gyroscope")

for _ in range(100):
    drift_x += read_word_2c(0x43) / 131
    drift_y += read_word_2c(0x45) / 131
    drift_z += read_word_2c(0x47) / 131
    time.sleep(0.01)

drift_x /= 100
drift_y /= 100
drift_z /= 100

rospy.loginfo("Ready")
while not rospy.is_shutdown():
    dt = time.time() - last_time

    vx = read_word_2c(0x43) / 131 - drift_x
    vy = read_word_2c(0x45) / 131 - drift_y
    vz = read_word_2c(0x47) / 131 - drift_z
    ax = read_word_2c(0x3b) / 16384.0
    ay = read_word_2c(0x3d) / 16384.0
    az = read_word_2c(0x3f) / 16384.0

    accy = math.degrees(math.atan(-ax / math.sqrt(ay ** 2 + az ** 2)));
    accx = math.degrees(math.atan(ay / math.sqrt(ax ** 2 + az ** 2)));

    alpha = 0.98
    rx = alpha * (vx * dt + rx) + (1.0 - alpha) * accx
    ry = alpha * (vy * dt + ry) + (1.0 - alpha) * accy
    rz += vz * dt

    last_time = time.time()

    msg = Imu()
    msg.header.frame_id = 'odom'
    msg.header.stamp = rospy.Time.now()

    msg.angular_velocity.x = vx
    msg.angular_velocity.y = vy
    msg.angular_velocity.z = vz

    msg.linear_acceleration.x = ax
    msg.linear_acceleration.y = ay
    msg.linear_acceleration.z = az

    pub.publish(msg)

    pose = PoseStamped()
    pose.header = msg.header
    o = pose.pose.orientation
    o.x, o.y, o.z, o.w = quaternion_from_euler(*map(math.radians, [rx, ry, rz]))

    pub_pose.publish(pose)

    rate.sleep()
