import cv2 as cv

img = cv.imread('Photos/Spike-Marks.png')
cv.imshow('Original Image', img)

grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# ret, threshImg = cv.threshold(grayImg, 127, 255, cv.THRESH_BINARY)
# cv.imshow('threshImg', threshImg)

blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

canny = cv.Canny(blur, 50, 175) #creates type of outline in an image
cv.imshow('Canny Edges', canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) #finds contours and hierarchy of shapes in an image
print(f'{len(contours)} contour(s) found!')

for contour in contours:
    if contour.shape[0] == 1:
        cv.drawContours(img, [contour], -1, (0,0,255), 2)

cv.waitKey(0)