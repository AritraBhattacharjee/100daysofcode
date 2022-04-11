import cv2 as cv
import numpy as np
img = cv.imread('images/3.jpg')
cv.imshow('Image',img)
# translating images
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1],img.shape[0])

    return cv.warpAffine(img,transMat,dimension)
"""
-x --> Left
-y --> Up
x --> Right
y --> Down
"""
translated = translate(img,50,100)
cv.imshow('Translated',translated)

# rotating an image
# (+ : rotate anticlockwi se)
# (- : rotate clockwise)
def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,45)
cv.imshow('Rotated',rotated)

# flipping
# 0 : flipping vertically
# 1: flipping horizontally
#  -1: both 
flip = cv.flip(img,-1)
cv.imshow('Flipped',flip)
cv.waitKey(0)