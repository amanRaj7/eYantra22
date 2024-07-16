import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def detect_horizontal_roads_under_construction(image):
    roads =[]
    corner = "0ABCDEFG"
    #plt.imshow(image)
    #plt.show()
    for i in range(1, 7):
        for j in range(1, 8):
            if(image[i*100+50, j*100, 0]==255) and (image[i*100+50, j*100, 1]==255) and (image[i*100+50, j*100, 2]==255):
                roads.append(corner[j]+str(i)+'-'+corner[j]+str(i+1))
    return roads


for image in range(15):
    path = r"public_test_images\maze_"+str(image)+".png"
    image = cv.imread(path)
    cv.imshow('image', image)
    list = detect_horizontal_roads_under_construction(image)
    print(list)