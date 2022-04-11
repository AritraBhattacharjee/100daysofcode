import cv2 as cv

img = cv.imread('images/2.jpg')

cv.imshow('Image',img)

# converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

# bluring an image
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)

# edge detection
canny = cv.Canny(img,125,175)
# canny2 = cv.Canny(blur,125,175)
# cv.imshow('Canny',canny)
# cv.imshow('Canny Blur',canny2)

#dilating the image
dilated = cv.dilate(canny,(3,3),iterations=5)
# cv.imshow('Dilated',dilated)

#eroding
eroded = cv.erode(dilated,(3,3),iterations=3)
# cv.imshow('Eroded',eroded)

#resize
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#cropping image
cropped = img[50:100,150:200]
cv.imshow('Cropped',cropped)

cv.waitKey(0)