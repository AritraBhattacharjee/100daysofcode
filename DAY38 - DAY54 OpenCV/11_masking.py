import cv2 as cv
import numpy as np
img = cv.imread('images/5.jpg')
# cv.imshow('Image',img)
# focussing on certain specific parts of a image/video : masking
 
blank = np.zeros(img.shape[:2],dtype='uint8')

# cv.imshow('Blank',blank)

# mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2+45),90,255,-1)
# cv.imshow('Mask',mask)

# masked = cv.bitwise_and(img,img,mask=mask)
# cv.imshow('Masked image',masked)

circle = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),90,255,-1)
# cv.imshow('Circle',circle)
rectangle = cv.rectangle(blank.copy(),(50,50),(200,200),255,-1)
# cv.imshow('Rectangle',rectangle)

weird_shape = cv.bitwise_and(circle,rectangle)
# cv.imshow('Weird',weird_shape)

weired_mask = cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('Weird',weired_mask)
cv.waitKey(0)
