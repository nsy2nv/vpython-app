# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 14:54:50 2024

@author: MTN-SIMREG
"""

from vpython import *
import numpy as np
arrowL = 1.5
arrowT = .01
theta = 0
pntT = .02
bRadius = .05
Xarrow = arrow(axis = vector(1,0,0),length=arrowL,shaftwidth=arrowT,color=color.red)
Yarrow = arrow(axis = vector(0,1,0),length=arrowL,shaftwidth=arrowT,color=color.green)
Zarrow = arrow(axis = vector(0,0,1),length=arrowL,shaftwidth=arrowT,color=color.blue)
rotateArrow = arrow(axis = vector(arrowL*np.cos(theta),arrowL*np.sin(theta),0),length=arrowL,shaftwidth=pntT,color=color.orange)
myBall = sphere(make_trail = True, color = color.orange, radius= bRadius,axis=vector(1,0,0),pos=vector(arrowL,0,0))
while True:
    for myAngle in np.linspace(0, 2*np.pi,1000):
        rate(50)
        rotateArrow.axis = vector(arrowL*np.cos(myAngle),arrowL*np.sin(myAngle),0)
        rotateArrow.lenght = arrowL
        myBall.pos = vector(arrowL*np.cos(myAngle),arrowL*np.sin(myAngle),0)
    for myAngle in np.linspace(0, 5*np.pi/2,1000):
        rate(50)
        rotateArrow.axis = vector(arrowL*np.cos(myAngle),0,arrowL*np.sin(myAngle))
        rotateArrow.lenght = arrowL
        myBall.pos = vector(arrowL*np.cos(myAngle),0,arrowL*np.sin(myAngle))
    for myAngle in np.linspace(0, 2*np.pi,1000):
        rate(50)
        rotateArrow.axis = vector(0,arrowL*np.sin(myAngle),arrowL*np.cos(myAngle))
        rotateArrow.lenght = arrowL
        myBall.pos = vector(0,arrowL*np.sin(myAngle),arrowL*np.cos(myAngle))
    for myAngle in np.linspace(0, np.pi/2,1000):
        rate(50)
        rotateArrow.axis = vector(arrowL*np.sin(myAngle),0,arrowL*np.cos(myAngle))
        rotateArrow.lenght = arrowL
        myBall.pos = vector(arrowL*np.sin(myAngle),0,arrowL*np.cos(myAngle))