import cv2 as cv

# img = cv.imread('images/7.jpeg')
# img = cv.imread('images/10.jpeg')
img = cv.imread('images/11.jpg')
cv.imshow('Image',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor = 1.1, minNeighbors=2)

print(f'Numver of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv.imshow('Face',img)
cv.waitKey(0)
