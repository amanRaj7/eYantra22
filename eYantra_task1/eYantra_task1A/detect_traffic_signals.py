from pickletools import uint8
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def detect_traffic_signals(img):
    #plt.imshow(img)
    #plt.show()
    traffic_signals = []
    corner = "0ABCDEFG"
    for i in range(1, 8):
        for j in range(1, 8):
            if(img[i*100, j*100, 2]==255):
                traffic_signals.append(corner[j]+str(i))
    return traffic_signals

for image in range(8):

    path = r"public_test_images\maze_"+str(image)+".png"
    image = cv.imread(path)
    cv.imshow('image', image)
    list = detect_traffic_signals(image)
    print(list)


cv.waitKey(0)
cv.destroyAllWindows()