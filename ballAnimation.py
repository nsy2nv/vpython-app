# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:36:32 2024

@author: MTN-SIMREG
"""

from vpython import *
import numpy as np

myBall = sphere(radius = 2, color = color.red, opacity = .5)

while True:
    for myRadius in np.linspace(2, .01, 1000):
        rate(250)
        myBall.radius = myRadius
    
    for myRadius in np.linspace(.01, 2, 1000):
        rate(250)
        myBall.radius = myRadius