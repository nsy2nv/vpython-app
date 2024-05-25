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
floor = box(pos = vector(0, -5, 0), color = color.white, size = vector(10,10,.1) )
ceiling = box(pos = vector(0, 5, 0), color = color.white, length = 10, width = 10, height = .1)
leftWall = box(pos = vector(-5, 0, 0), color = color.white, length = .1, width = 10, height = 10)
rightWall = box(pos = vector(5, 0, 0), color = color.white, length = .1, width = 10, height = 10)
backWall = box(pos = vector(0, 0, -5), color = color.white, length = 10, width = .1, height = 10)
ball = sphere(color = color.magenta)
deltaX = .1
xPos = 0
while True:
    rate(10)
    xPos = xPos + deltaX
    if (xPos > 4 or xPos < -4):
        deltaX = deltaX * (-1)
    ball.pos = vector(xPos, 0, 0)