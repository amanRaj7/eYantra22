import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def detect_horizontal_roads_under_construction(image):
    roads =[]
    corner = "0ABCDEFG"
    #plt.imshow(image)
    #plt.show()
    for i in range(1, 8):
        for j in range(1, 7):
            if(image[i*100, j*100+50, 0]==255) and (image[i*100, j*100+50, 1]==255) and (image[i*100, j*100+50, 2]==255):
                roads.append(corner[j]+str(i)+'-'+corner[j+1]+str(i))
    return roads


for image in range(8):
    path = r"public_test_images\maze_"+str(image)+".png"
    image = cv.imread(path)
    cv.imshow('image', image)
    list = detect_horizontal_roads_under_construction(image)
    print(list)