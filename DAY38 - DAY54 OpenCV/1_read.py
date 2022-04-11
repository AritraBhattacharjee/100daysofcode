import cv2 as cv

# img = cv.imread('images/1.jpg')
# cv.imshow('Cat',img)
# cv.waitKey(0) 


# We read the video frame by frame using a infinite loop and print the same.
capture = cv.VideoCapture('video/Dog.mp4')
# capture = cv.VideoCapture(1)

while True:
    isTrue,frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()