import cv2 as cv

img = cv.imread('Photos/dog1.jpg')

#Rescales Images, Videos, & Live Video
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale) #frame.shape[1] is the width of the window
    height = int(frame.shape[0] * scale) #frame.shape[0] is the height of the window
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)

cv.imshow('Image', resized_image)

#Only resizes Live Video
def changeRes(width, height):
    capture.set(3, width) #3 corresponds with the width property
    capture.set(4, height) #4 corresponds with the height property

#Reading Videos - Use integers (0,1,2,etc) for webcam or file path for videos
capture = cv.VideoCapture('Videos/dog1.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, .3) #used function to rescale video by .3x

    #cv.imshow("Video", frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()