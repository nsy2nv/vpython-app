# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 20:48:04 2024

@author: MTN-SIMREG
"""

from vpython import *
from time import *
"""ball = sphere(color = color.magenta)
sleep(5)
ball.color = color.red
sleep(5)
ball.color = color.blue
sleep(5)"""
wallThickness = .1
roomHeight =15
roomWidth = 10
roomDepth = 3
mRadius = .5

floor = box(pos = vector(0, -roomHeight/2, 0), color = color.white, size = vector(roomWidth,wallThickness,roomDepth) )
ceiling = box(pos = vector(0, roomHeight/2, 0), color = color.white, size = vector(roomWidth,wallThickness,roomDepth))
leftWall = box(pos = vector(-roomWidth/2, 0, 0), color = color.white, size = vector(wallThickness,roomHeight,roomDepth))
rightWall = box(pos = vector(roomWidth/2, 0, 0), color = color.white, size = vector(wallThickness,roomHeight,roomDepth))
backWall = box(pos = vector(0, 0, -roomDepth/2), color = color.white, size = vector(roomWidth,roomHeight,wallThickness))
ball = sphere(radius = mRadius, color = color.magenta)


deltaX = .1
deltaY = .1
deltaZ = .1

xPos = 0
yPos = 0
zPos = 0


while True:
    rate(50)
    xPos = xPos + deltaX
    yPos = yPos + deltaY
    zPos = zPos + deltaZ
    
    Xrme = xPos + mRadius
    Xlme = xPos - mRadius
    Ycme = yPos + mRadius
    Yflme = yPos - mRadius
    Zbme = zPos - mRadius
    Zfme = zPos + mRadius
    
    Rwe = roomWidth/2 - wallThickness/2
    Lwe = -roomWidth/2 + wallThickness/2
    Cwe = roomHeight/2 - wallThickness/2
    Flwe = -roomHeight/2 + wallThickness/2
    Bwe = -roomDepth/2 + wallThickness/2
    Fwe = roomDepth/2 - wallThickness/2
    
    if (Xrme >= Rwe or Xlme <= Lwe):
        deltaX = deltaX * (-1)
        
    if (Ycme >= Cwe or Yflme <= Flwe):
        deltaY = deltaY * (-1)
        
    if (Zfme >= Fwe or Zbme <= Bwe):
        deltaZ = deltaZ * (-1)
    ball.pos = vector(xPos, yPos, zPos)
   