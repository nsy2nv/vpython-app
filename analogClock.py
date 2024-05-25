# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 20:09:07 2024

@author: MTN-SIMREG
"""

from vpython import *
import numpy as np
mRadius = 3
ringThk = .02
arrowT = .02
theta = 0
minuteT = .04
hourT = .06
myClock = ring(radius = mRadius, pos = vector(0,0,0),axis= vector(0,0,1),thickness = ringThk)
clockCenter = sphere(radius = .08,pos = vector(0,0,0))
secondHand = arrow(length=mRadius,shaftwidth=arrowT)
minuteHand = arrow(length=mRadius-.5,shaftwidth=minuteT,axis = vector(0,1,0))
hourHand = arrow(length=mRadius-1,shaftwidth=hourT,axis = vector(-1,0,0))
while True:
    for myAngle in np.linspace(np.pi/2,5*np.pi/2,13):
        rate(50)
        box(axis = vector(mRadius*np.cos(myAngle),mRadius*np.sin(myAngle),0),size = vector(.05,.15, .05), color = color.orange, pos = vector(mRadius*np.cos(myAngle),mRadius*np.sin(myAngle),0))
        secondHand.length = mRadius
    for myAngle in np.linspace(np.pi/2,5*np.pi/2,61):
        box(axis = vector(mRadius*np.cos(myAngle),mRadius*np.sin(myAngle),0),size = vector(.03,.08, .05), color = color.orange, pos = vector(mRadius*np.cos(myAngle),mRadius*np.sin(myAngle),0)) 
    while True:
        for myAngle in np.linspace(0,-2*np.pi,61):
            rate(1)
            secondHand.axis = vector(mRadius*np.cos(myAngle),mRadius*np.sin(myAngle),0)
            secondHand.length = mRadius
 
    