import numpy as np
import cv2
from GuiClass import Gui
from TimerBoolClass import Timer
from matplotlib import pyplot as plt

# load opencv classifiers
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_smile.xml')
# video capture
vid = cv2.VideoCapture(0)

# read image and draw rects around faces and smiles
def smile_detec(img):
    # convert captured frame to greyscale and detect faces
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    ret = False
    # draw rectangle around each face
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        # draw rectangle around smiles and set flag
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
        if len(smiles) != 0:
            ret = True
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
    return ret, img

# scale image to desired size
def scale_img(img, width, height):
    old_width = img.shape[1]
    old_height = img.shape[0]
    scale_x = width / old_width
    scale_y = height / old_height
    scaled_img = cv2.resize(img, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_LINEAR)
    return scaled_img

def main():
    # compose gui
    gui = Gui(800, 1200, (5, 197, 255))
    button = cv2.imread('assets/buynow.png')
    button = scale_img(button, 500, 100)
    gui.addImage(button, 100, 600)
    gui.addImage(button, 300, 600)
    logo = cv2.imread('assets/euronet.png')
    logo = scale_img(logo , 1000, 200)
    gui.addImage(logo, 500, 100)

    # init timer
    timer = Timer()
    timer.start()
    while(True):
        # scale frame and detect smile
        ret, cam = vid.read()
        ret, cam = smile_detec(cam)
        cam = scale_img(cam, 400, 300)

        # set timer flag
        timer.set_true() if ret else timer.set_false()
    
        # display frame
        gui.addImage(cam, 100, 100)
        cv2.imshow('gui', gui.getImage())
        
        # exit program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # print results
    print("time smiling :", timer.total_true_time)
    print("time not smiling :", timer.total_false_time)
    # cleanup
    vid.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
