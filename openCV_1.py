# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:57:15 2024

@author: MTN-SIMREG
"""

import cv2
print(cv2.__version__)

cam = cv2.VideoCapture(0)
while True:
    ignore, frame = cam.read()
    cv2.imshow('webcam', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()