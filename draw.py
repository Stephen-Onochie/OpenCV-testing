"""
FCC OpenCV Course - https://www.youtube.com/watch?v=oXlwWbU8l2o&t=434s
STOPPED AT 22:58
Drawing Shapes & Putting Text
"""
import cv2 as cv
import numpy as np
                #width, height, & # of color channels
blank = np.zeros((500,500, 3), dtype='uint8') #uint8 is the datatype for an image
cv.imshow('Blank', blank)

    #1. Paint the image a certain color
blank[:] = 0,255,0
cv.imshow('Green', blank)

# img = cv.imread('Photos/dog1.jpg')
# cv.imshow('Dog', img)

cv.waitKey(0)