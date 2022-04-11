# error program not working

import os
import cv2 as cv
import numpy as np
haar_cascade = cv.CascadeClassifier('haar_face.xml')
# people = ['goku','modi','obama']
# DIR = 'D:\\Programming\\Python\\#100daysofcode\\DAY38 - OpenCV\\train'
DIR = r'D:\Programming\Python\#100daysofcode\DAY38 - OpenCV\train'
p = []
for i in os.listdir(DIR):
    p.append(i)

print(p)
feature = []
labels = []
def create_train():
    for person in p:
        path = os.path.join(DIR,person)
        label = p.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                face_roi = gray[y:y+h,x:x+w]
                feature.append(face_roi)
                labels.append(label)
create_train()

print(f'Length of feaures = {len(feature)}')
print(f'Length of labels = {len(labels)}')
features = np.array(feature, dtype= 'object')
labels = np.array(labels)
face_recogniser = cv.face.LBPHFaceRecogniser_create()

face_recogniser.train(feature,labels)
np.save('features.npy',feature)
np.save('labels.npy',labels)