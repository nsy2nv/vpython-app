# -*- coding: utf-8 -*-
"""
Vpthon designed Analog Clock that uses the system time to keep accurate time

@author: Nsikan
"""

from vpython import *
import numpy as np
import time
clockR = 1
clockT = clockR/20
majorTickL = clockR/10
majorTickT = 2*np.pi*clockR/500
majorTickW = clockT*1.2

minorTickL = clockR/20
minorTickT = 2*np.pi*clockR/700
minorTickW = clockT*1.2

minuteHandL = clockR-majorTickL*1.5
minuteHandT = minorTickL/2
minuteHandOffSet = clockT/2+minuteHandT

hourHandL = minuteHandL*.75
hourHandT = minuteHandT*1.25
hourHandOffSet = clockT+hourHandT

minInc = 0

clockCenter = sphere(color = color.black, radius = clockT)
secondHand = arrow(axis = vector(0,1,0),color = color.black, length = clockR,shaftwidth = clockT/2.5, pos= vector(0,0,clockT))
minutesHand = arrow(color = color.black, length = minuteHandL,shaftwidth = minuteHandT, pos= vector(0,0,minuteHandOffSet))
hourHand = arrow(color = color.black, length = hourHandL,shaftwidth = hourHandT, pos= vector(0,0,hourHandOffSet))

for theta in np.linspace(0,2*np.pi,13):
    majorTick = box(axis = vector(clockR*np.cos(theta),clockR*np.sin(theta),0), color = color.black, length = majorTickL, width = majorTickW, height = majorTickT, pos = vector((clockR-majorTickL/2)*np.cos(theta),(clockR-majorTickL/2)*np.sin(theta),0))

for theta in np.linspace(0,2*np.pi,61):
    minorTick = box(axis = vector(clockR*np.cos(theta),clockR*np.sin(theta),0), color = color.black, length = minorTickL, width = minorTickW, height = minorTickT, pos = vector((clockR-minorTickL/2)*np.cos(theta),(clockR-minorTickL/2)*np.sin(theta),0))
clock = cylinder(axis = vector(0,0,1), length = clockT, color = vector(.9,.6,.2), radius = clockR, pos = vector(0,0,-clockT/2))
while True:
    rate(5000)
    second = time.localtime(time.time())[5]
    minute = time.localtime(time.time())[4]
    hour = time.localtime(time.time())[3]

    if hour > 12:
        hour = hour - 12
    secondAngle = -(second/60)*2*np.pi+np.pi/2
    minuteAngle = -((minute + second/60 )/ 60) * 2 * np.pi + np.pi / 2
    hourAngle = -((hour + minute/60)/12)*2*np.pi+np.pi/2
    print(secondAngle)
    secondHand.axis = vector(clockR*np.cos(secondAngle),clockR*np.sin(secondAngle),0)
    minutesHand.axis = vector(minuteHandL*np.cos(minuteAngle),minuteHandL*np.sin(minuteAngle),0)
    hourHand.axis = vector(hourHandL*np.cos(hourAngle),hourHandL*np.sin(hourAngle),0)
