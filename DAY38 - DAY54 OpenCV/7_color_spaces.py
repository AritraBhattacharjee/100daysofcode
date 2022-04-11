import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('images/2.jpg')
cv.imshow("Image",img)

# plt.imshow(img)
# plt.show()
# turning picture to grapy scale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

# BGR to HSV

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)

#BGR to LAB(l*a*b)
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)

# BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)