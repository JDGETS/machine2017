#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BallLauncher:
    def __init__(self):
        self.current_elevation_angle = 0
        self.current_direction_angle = 0
        self.current_left_speed = 0
        self.current_right_speed = 0
        self.min_speed = 0
        self.max_speed = 100
        self.min_theta = 0
        self.max_theta = 180
        self.min_phi = 0
        self.max_phi = 80

    def set_elevation_angle(self, angle):
        """
        Sets the elevation angle to a realistic value
        :param angle: in degrees
        :return: returns true if success, else false
        """
        if self.current_elevation_angle == angle:
            print "The angle desired is the same as the current angle"
            return True
        if angle < self.min_phi:
            print "Angle desired is not within boundaries. Boundaries are: "
            print "Min angle: ", self.min_phi
            print "Max angle: ", self.max_phi
            return False
        if angle > self.max_phi:
            print "Angle desired is not within boundaries. Boundaries are: "
            print "Min angle: ", self.min_phi
            print "Max angle: ", self.max_phi
            return False

        self.current_elevation_angle = angle
        return True

    def set_lauch_speed(self, speed):
        """
        Sets the speed to a realistic value
        :param speed: in rpm
        :return: returns true if success, else false
        """
        if self.current_left_speed == speed and self.current_right_speed == speed:
            print "The speed desired is the same as the current speed"
            return True
        if speed < self.min_speed:
            print "Speed desired is not within boundaries. Boundaries are: "
            print "Min speed: ", self.min_speed
            print "Max speed: ", self.max_speed
            return False
        if speed > self.max_speed:
            print "Speed desired is not within boundaries. Boundaries are: "
            print "Min speed: ", self.min_speed
            print "Max speed: ", self.max_speed
            return False

        self.current_left_speed = speed
        self.current_right_speed = speed

        return True

    def set_direction_angle(self, angle):
        """
        Sets the direction angle to a realistic value
        :param angle: in degrees
        :return: returns true if success, else false
        """
        if self.current_direction_angle == angle:
            print "The angle desired is the same as the current angle"
            return True
        if angle < self.min_theta:
            print "Angle desired is not within boundaries. Boundaries are: "
            print "Min angle: ", self.min_theta
            print "Max angle: ", self.max_theta
            return False
        if angle > self.max_theta:
            print "Angle desired is not within boundaries. Boundaries are: "
            print "Min angle: ", self.min_theta
            print "Max angle: ", self.max_theta
            return False

        self.current_elevation_angle = angle
        return True
