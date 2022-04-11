import cv2 as cv

img = cv.imread('images/5.jpg')
cv.imshow('Image',img)

# Averaging
average = cv.blur(img,(7,7))
cv.imshow("AverageBlur",average)

# gaussian Blur
gauss = cv.GaussianBlur(img,(7,7),0)
cv.imshow("GaussianBlur",gauss)

#median blur
median = cv.medianBlur(img,7)
cv.imshow("MedianBlur",median)

# bilateral : applies blur but retains the edges     
bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow("BilateralBlur",bilateral)



cv.waitKey(0)