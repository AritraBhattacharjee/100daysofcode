import cv2 as cv

def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# changes resolution of live video
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)


if __name__=="__main__":

    #resizing images
    img = cv.imread('images/1.jpg')
    cv.imshow('Cat',img)
    cv.imshow('Image',rescaleFrame(img,scale=0.5))


    # resizing vodeo frames
    # capture = cv.VideoCapture('video/Dog.mp4')
    capture = cv.VideoCapture(0)
    while True:
        isTrue,frame = capture.read()
        # frame_resized = rescaleFrame(frame,scale=.2)
        frame_resized = changeRes(500,500)

        cv.imshow('Video',frame)
        cv.imshow('Resized',frame_resized)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break
    capture.release()
    cv.destroyAllWindows()

    cv.waitKey(0) 

