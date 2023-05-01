import cv2 as cv

#Reading Photos
img = cv.imread('Photos/dog1.jpg')

cv.imshow('Dog', img)

cv.waitKey(0)

"""
FCC OpenCV Course - https://www.youtube.com/watch?v=oXlwWbU8l2o&t=434s
STOPPED AT 12:57
Resizing & Rescaling
"""


#Reading Videos - Use integers (0,1,2,etc) for webcam or file path for videos
# capture = cv.VideoCapture('Videos/dog1.mp4')

# while True:
#     isTrue, frame = capture.read()

#     cv.imshow("Video", frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()