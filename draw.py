"""
FCC OpenCV Course - https://www.youtube.com/watch?v=oXlwWbU8l2o&t=434s
STOPPED AT 22:58
Drawing Shapes & Putting Text
"""
import cv2 as cv
import numpy as np
                #width, height, & # of color channels
blank = np.zeros((500,500, 3), dtype='uint8') #uint8 is the datatype for an image
# cv.imshow('Blank', blank)

    #1. Paint the image a certain color
# blank[200:300, 300:400] = 0,255,0
# cv.imshow('Green', blank)

#Draw a rectangle (Bottom Left Point, Top Right Point, & thickness)
cv.rectangle(blank, (0,0), (150,250), (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

# img = cv.imread('Photos/dog1.jpg')
# cv.imshow('Dog', img)

cv.waitKey(0)