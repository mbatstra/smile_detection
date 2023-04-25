import numpy as np
import cv2
from TimerBoolClass import Timer
from datetime import datetime
import time
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

def wait_startup():
    # insert image made by iggy here
    img = np.zeros((300, 400, 3), dtype=np.uint8)
    img2 = cv2.imread('assets/strart.jpg')
    img[150:150+img2.shape[0], 110:110+img2.shape[1]] = img2
    while (True):
        cv2.imshow("main", img)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            break

# draw text to image returning offset for subsequent calls
def draw_text(img, text, bg_on,
          font=cv2.FONT_HERSHEY_PLAIN,
          pos=(0, 0),
          font_scale=3,
          font_thickness=2,
          text_color=(255, 255, 255),
          text_color_bg=(0, 0, 0)
          ):

    x, y = pos
    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_w, text_h = text_size
    if bg_on:
        cv2.rectangle(img, pos, (x + text_w, y + text_h), text_color_bg, -1)
    cv2.putText(img, text, (x, y + text_h + font_scale - 1), font, font_scale, text_color, font_thickness)

    return text_size

def countdown():
    start = time.time()
    while True:
        now = time.time() - start
        now_char = 3 - int(now)
        ret, cam = vid.read()
        draw_text(cam, str(now_char), True)
        cam = scale_img(cam, 400, 300)
        cv2.imshow("main", cam)
        cv2.waitKey(1)
        if now > 3:
            break

def record_withdrawal(timer):
    timer.start()
    while(True):
        # get time to draw to frame
        now = time.time() - timer.start_time
        now_str = datetime.utcfromtimestamp(now).strftime('%M:%S.%f')[:-4]

        # scale frame and detect smile
        ret, cam = vid.read()
        ret, cam = smile_detec(cam)
        draw_text(cam, now_str, True)
        cam = scale_img(cam, 400, 300)

        # set timer flag
        timer.set_true() if ret else timer.set_false()
    
        # display frame
        cv2.imshow("main", cam)

        # exit program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return


def main():
    # show starting screen
    wait_startup()

    # show countdown screen
    countdown()

    # init timer
    timer = Timer()

    # start withdrawal
    record_withdrawal(timer)

    # print results
    print("time smiling :", timer.total_true_time)
    print("total time:", timer.get_total_time())

    # cleanup
    vid.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
