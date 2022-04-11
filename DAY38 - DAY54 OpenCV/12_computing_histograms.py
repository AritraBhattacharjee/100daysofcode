# histogram : allows to visualise the pixel intensity distribution in an image.
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# img = cv.imread('images/5.jpg')
# # cv.imshow('Image',img)\
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)
# # gray histogram 
# gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixel')
# plt.plot(gray_hist)
# plt.xlim([0,255])
# plt.show()
# PLotting histogram of pixel intensities with the pc having a mask
img = cv.imread('images/5.jpg')
# cv.imshow('Image',img)\
blank = np.zeros(img.shape[:2],dtype='uint8')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)
circle = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),90,255,-1)
mask = cv.bitwise_and(gray,gray,mask=circle)
# # gray histogram 
gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256])
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixel')
# plt.plot(gray_hist)
# plt.xlim([0,255])
# plt.show()
# color histogram
img = cv.imread('images/5.jpg')
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.title('Color Histogram')
plt.show()
cv.waitKey(0)