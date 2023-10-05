import cv2 as cv
import numpy as np

"""
Steps to find contours
Step 1: Get Image/Camera Frame
Step 2: Turn into grayscale
Step 3: Turn into Gausian Blur
Step 4: Turn into Canny image (desired outline)
"""


img = cv.imread('Photos/preset-shapes.jpg') #input image into OpenCV

cv.imshow('Dog', img) #show the specific dog image in a window

blank = np.zeros(img.shape, dtype='uint8')
#cv.imshow('Blank',blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #convert image into grayscale
#cv.imshow('Gray', gray) #show the grayscale image

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175) #creates type of outline in an image
cv.imshow('Canny Edges', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# #cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) #finds contours and hierarchy of shapes in an image
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 2)
#cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
