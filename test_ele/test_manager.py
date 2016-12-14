#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ball_launcher import ballLauncher


def ball_launcher():
    bl = ballLauncher.BallLauncher()
    print bl.current_elevation_angle
    bl.set_elevation_angle(80)
    print bl.current_elevation_angle
    bl.set_elevation_angle(91)
    bl.set_direction_angle(-1)
    bl.set_direction_angle(181)


if __name__ == "__main__":
    ball_launcher()