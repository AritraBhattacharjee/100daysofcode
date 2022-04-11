import cv2 as cv
import numpy as np

# img = cv.imread('images/5.jpg')
# cv.imshow('Image',img)

blank = np.zeros((400,400),dtype='uint8')
cv.imshow('Blank',blank)

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Circle',circle)
cv.imshow('Rectangle',rectangle)

#bitwise AND: returns the intersection of the two images
bitwiseand = cv.bitwise_and(rectangle,circle)
cv.imshow('AND',bitwiseand)

# bitwise OR : returns the superimposed images of the input images(intersecting as well as non intersection)
bitwiseor = cv.bitwise_or(rectangle,circle)
cv.imshow('OR',bitwiseor)

# bitwise xor : returns the not intersecting region
bitwisexor = cv.bitwise_xor(rectangle,circle)
cv.imshow('XOR',bitwisexor)

#bitwise not: inverts the binary color
bitwisenot = cv.bitwise_not(circle)
cv.imshow('Not',bitwisenot)
cv.waitKey(0)