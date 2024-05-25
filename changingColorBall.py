# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 17:08:24 2024

@author: MTN-SIMREG
"""

from vpython import *
import random
redColor = .1
greenColor = .3
blueColor = .5
xPos = 0
yPos = 0
zPos = 0
deltaX = 1
deltaY = 1
deltaZ = 1
mRadius = .1

while True:
    redColorDelta = random.random()
    greenColorDelta = random.random()
    blueColorDelta = random.random()
   
    redColor = redColor + redColorDelta
    greenColor = greenColor + greenColorDelta
    blueColor = blueColor + blueColorDelta
   
    
    
    mySphere = sphere(radius = mRadius, color = vector(redColor,greenColor,blueColor), pos = vector(0,0,0))
    rate(2)
    if redColor >= 1 or redColor <= 0:
        redColor = random.random()
    if greenColor >= 1 or greenColor <= 0:
        greenColor = random.random()
    if blueColor >= 1 or blueColor <= 0:
        blueColor = random.random()
    
   
    

    
        

            
        
            
            