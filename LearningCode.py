import numpy as np
import cv2 as cv
import sys


cap = cv.VideoCapture(0)

if not cap.isOpened():
    print('Your camera is not open :(')
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print('We cant get the frames for some reason?')
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        quit

    
