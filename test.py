import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load two images
img_ajax = cv2.imread('ajax.jpg')
img_blank = np.zeros((800, 1200, 3), dtype=np.uint8)
img_blank[:] = (50, 168, 82)

x = 100
y = 200
img_blank[x:x+img_ajax.shape[0], y:y+img_ajax.shape[1]] = img_ajax

cv2.imshow('logo',img_ajax)
cv2.imshow('blank',img_blank)
cv2.waitKey(0)
cv2.destroyAllWindows()
