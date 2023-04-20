import numpy as np
import cv2
from matplotlib import pyplot as plt

class Gui:
    def __init__(self, width, height, clr):
        self.width = width
        self.height = height
        self.img = np.zeros((width, height, 3), dtype=np.uint8)
        self.img[:] = clr

    def addImage(self, img, x, y):
        self.img[x:x+img.shape[0], y:y+img.shape[1]] = img

    # for some reason calling imshow from class doesn't work
    def getImage(self):
        return self.img
