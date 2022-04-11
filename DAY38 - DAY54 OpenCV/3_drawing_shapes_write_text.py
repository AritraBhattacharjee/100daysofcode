import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)
img = cv.imread('images/1.jpg')
cv.imshow('Image',img)

# paint the image a certain colour

blank[:] = 0,255,0
blank[:] = 0,0,255
blank[200:300,300:400] = 0,0,255
cv.imshow('Green',blank)


# Drawing a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)

# drawing circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[1]//2),100,(0,0,255),thickness=3)

# drawing line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255))

# writing text 
cv.putText(blank,'Hello',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)


# cv.imshow('Rectangle',blank)
cv.imshow('Circle',blank)
cv.waitKey(0)