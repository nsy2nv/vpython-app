# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:48:03 2024

@author: MTN-SIMREG
"""

from vpython import *
import numpy as np
mRadius = 1
myOrb = sphere(radius = mRadius, color = vector(1,1,0))
rChan = 1
gChan = 1
bChan = 0

rInc = .001
gInc = -.001
bInc = .001

while True:
    rate(50)
    
    rChan = rChan + rInc
    gChan = gChan + gInc
    bChan = bChan + bInc
    

    if rChan <= 1:
        rApply = rChan
    if rChan > 1:
        rApply = 1
        
    if gChan <= 1:
        gApply = gChan
    if gChan > 1:
        gApply = 1
        
    if bChan <= 1:
        bApply = bChan
    if bChan > 1:
        bApply = 1
    
    myOrb.color = vector(rApply,gApply,bApply)
    
    if rChan >= 1.5 or rChan <= 0:
        rInc = rInc * (-1)
        
    if gChan >= 1.5 or gChan <= 0:
        gInc = gInc * (-1)
        
    if bChan >= 1.5 or bChan <= 0:
        bInc = bInc * (-1)
    print(rApply+gApply+bApply)