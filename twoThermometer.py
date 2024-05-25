# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:57:15 2024

@author: MTN-SIMREG
"""
import numpy as np
from vpython import *

red_cyl = cylinder(radius = .1, color = color.red, length = 3, pos = vector(0,-3,0), axis = vector(0,1,0))
red_sphere = sphere(radius = .2, color = color.red, pos = vector(0, -3, 0), axis = vector(0,1,0))
glass_sphereRd = sphere(radius = .25, pos = vector(0, -3, 0), axis = vector(0,1,0), opacity = .4)
glass_cyl_Rd = cylinder(radius = .2, length = 4, pos = vector(0,-3,0), axis = vector(0,1,0), opacity = .4)

green_cyl = cylinder(radius = .1, color = color.green, length = 3, pos = vector(1, -3, 0), axis = vector(0,1,0))
green_sphere = sphere(radius = .2, color = color.green, pos = vector(1, -3, 0), axis = vector(0,1,0))
glass_sphereGr = sphere(radius = .25, pos = vector(1, -3, 0), axis = vector(0,1,0), opacity = .4)
glass_cyl_Gr = cylinder(radius = .2, length = 4, pos = vector(1, -3, 0), axis = vector(0,1,0), opacity = .4)

red_cyl_length = 1
green_cyl_length = 1
red_cyl_delta = .01
green_cyl_delta = .02


while True:
    rate(20)
    red_cyl_length = red_cyl_length + red_cyl_delta
    green_cyl_length = green_cyl_length + green_cyl_delta
    red_cyl.length = red_cyl_length
    green_cyl.length = green_cyl_length
    if red_cyl_length >= 4 or red_cyl_length <= .25:
        red_cyl_delta = red_cyl_delta * (-1)
    
    if green_cyl_length >= 4 or green_cyl_length <= .25:
        green_cyl_delta = green_cyl_delta * (-1)
        
    