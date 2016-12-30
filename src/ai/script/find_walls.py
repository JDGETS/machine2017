#!/usr/bin/env python

import rospy
import numpy as np
import cv2
import itertools
import math
from geometry_msgs.msg import PolygonStamped, Polygon, Point32
from nav_msgs.msg import OccupancyGrid
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2
from std_msgs.msg import Header, Float32
import tf

rospy.init_node('find_walls')

terrain = rospy.Publisher('/terrain', PolygonStamped, queue_size=10)

rate = rospy.Rate(30)
terrain_width = 304.8
terrain_height = 152.4
goals_height = [0.889, 1.143, 0.889]

points = None
goals = []

def handle_map(msg):
    global points

    if points != None:
        return

    origin = msg.info.origin.position
    width, height = msg.info.width, msg.info.height
    data = np.array(msg.data)
    data[data == -1] = 0
    data[data > 1] = 255

    data = np.array(data, dtype=np.uint8).reshape((height, width))

    img = cv2.cvtColor(data, cv2.COLOR_GRAY2RGB)
    edges = cv2.Canny(data, 50, 200, apertureSize = 5)

    lines = cv2.HoughLines(edges, 1, np.pi / 180, 40)
    eqs = []
    groups = {}

    _, contours, _ = cv2.findContours(data, 1, 2)

    area = 0
    the_rect = None

    # find the largest rectangle
    for cnt in contours:
        rect = cv2.minAreaRect(cnt)
        w, h = rect[1]

        if w * h > area:
            area = w * h
            the_rect = rect

    # rectangle points
    box = cv2.boxPoints(the_rect)
    _, _, angle = the_rect
    angle = math.radians(angle)

    # farthest points
    top_corners = sorted(box, key=lambda (x,y): math.sqrt((x + origin.x)**2 + (y + origin.y)**2))[-2:]

    # linear interpolation to estimate the goals positions
    a, b  = top_corners

    for r, z in zip([0.25, 0.5, 0.75], goals_height):
        x, y = (a + (b - a) * r) / 100.0
        goals.append((origin.x + x, origin.y + y, z))

    points = [top_corners[0]]

    # figure out bottom corners
    for (x, y) in top_corners:
        points.append((x + math.cos(angle) * - terrain_width, y + math.sin(angle) * - terrain_width))

    points.append(top_corners[1])

    msg = PolygonStamped()
    msg.header.frame_id = 'map'
    msg.header.stamp = rospy.Time.now()

    for (x, y) in points:
        msg.polygon.points.append(Point32(x / 100.0 + origin.x, y / 100.0 + origin.y, 0))

    terrain.publish(msg)

rospy.Subscriber('/map', OccupancyGrid, handle_map)

goals_publisher = rospy.Publisher('/goals', PointCloud2, queue_size=10)
ball_trajectory = rospy.Publisher('/ball_trajectory', PolygonStamped, queue_size=10)

br = tf.TransformBroadcaster()


while not rospy.is_shutdown():
    if len(goals) > 0:
        header = Header()
        header.frame_id = 'map'
        header.stamp = rospy.Time.now()

        msg = pc2.create_cloud_xyz32(header, goals)

        goals_publisher.publish(msg)
        now = rospy.Time.now()

        for i, (x, y, z) in enumerate(goals):
            base_tf = "goal" + str(i) + "_base"
            br.sendTransform((x, y, 0), (0, 0, 0, 1), now, base_tf, "map")
            br.sendTransform((0, 0, z), (0, 0, 0, 1), now, "goal" + str(i) + "_ring", base_tf)

    rate.sleep()
