import cv2 as cv
import numpy as np
# contours are the boundaries of the image.
img = cv.imread('images/6.jpg')
cv.imshow('Image',img)

blank = np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

# canny = cv.Canny(img,125,175)
# cv.imshow('Canny Edges', canny)

ret,thres = cv.threshold(gray,125,255,cv.THRESH_BINARY)
# takes a image and convert to binary



# contours,heirarchy = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
contours,heirarchy = cv.findContours(thres,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
# returns the list of coordinates of contours
# cv.RETR_TREE,cv.RETR_LIST, etc
# cv.CHAIN_APPROX_NONE,cv.CHAIN_APPROX_SIMPLE
# print(contours)
# print(heirarchy)
print(f"{len(contours)} found in the image")


cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow("Contour Drawn",blank)
cv.waitKey(0)