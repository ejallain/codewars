# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 10:38:44 2017

@author: eria
"""


def bouncingBall(h, bounce, window):
    if h < 0 or bounce < 0 or bounce >= 1 or window >= h:
        return -1
    else:
        num_ball_sightings = 1
        bounce_height = h * bounce
        while bounce_height > window:
            num_ball_sightings += 2
            bounce_height = bounce_height * bounce
    return(num_ball_sightings)
            