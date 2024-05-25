# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 20:28:24 2024

@author: MTN-SIMREG
"""
import numpy as np
from vpython import *
glass_sphere = sphere(radius = 4, color = color.white, opacity = .3)
glass_cylinder = cylinder(radius = 3, color = color.white, opacity = .3, length = 15 )
therm_sphere = sphere(radius = 3, color = color.red)
therm_cylinder = cylinder(radius = 3, color = color.red, length = 15)
for tick in np.linspace(1, 15, 30):
    box(size = vector(.05,.5, .25), color = color.white, pos = vector(tick, 0, 5))
while True:
    for therm in np.linspace(1, 15, 200):
        therm_cylinder.length = therm
        rate(25)
    for therm in np.linspace(15, 1, 200):
        therm_cylinder.length = therm
        rate(25)