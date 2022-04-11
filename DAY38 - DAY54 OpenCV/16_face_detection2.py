import cv2 as cv

# capture = cv.VideoCapture('video/Dog.mp4')
capture = cv.VideoCapture(0) # from webcam
haar_cascade = cv.CascadeClassifier('haar_face.xml')

while True:
    isTrue,frame = capture.read()
    # cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    faces_rect = haar_cascade.detectMultiScale(frame,scaleFactor = 1.1, minNeighbors=2)
    # print(f'Numver of faces found = {len(faces_rect)}')

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv.imshow('Face',frame)

capture.release()
cv.destroyAllWindows()