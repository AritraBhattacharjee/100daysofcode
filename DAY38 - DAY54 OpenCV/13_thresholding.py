# binarization of an image: turinng an image to a binary

import cv2 as cv

img = cv.imread('images/5.jpg')
cv.imshow('Image',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# simple thresholding
threshold, thres = cv.threshold(gray,150,255,cv.THRESH_BINARY)
threshold, thres = cv.threshold(gray,100,255,cv.THRESH_BINARY)

cv.imshow('Simple Threshold',thres)

threshold, thres_inv = cv.threshold(gray,100,255,cv.THRESH_BINARY_INV)

cv.imshow('Simple Threshold inverse',thres_inv)

# adaptive thresholding

adaptive_threshold = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
# adaptive_threshold = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,3)

cv.imshow('Adaptive Thresholding',adaptive_threshold)




cv.waitKey(0)