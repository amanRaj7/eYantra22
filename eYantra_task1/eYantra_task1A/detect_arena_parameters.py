import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

path1 = r"D:\eYantra\eYantra_task1\public_test_images\maze_0.png"
path2 = r"D:\eYantra\eYantra_task1\public_test_images\maze_1.png"
path3 = r"D:\eYantra\eYantra_task1\public_test_images\maze_2.png"
path4 = r"D:\eYantra\eYantra_task1\public_test_images\maze_3.png"
path5 = r"D:\eYantra\eYantra_task1\public_test_images\maze_4.png"

image1 = cv.imread(path1)
image2 = cv.imread(path2)
image3 = cv.imread(path3)
image4 = cv.imread(path4)
image5 = cv.imread(path5)

def shop(shop_, n):
    shop_detail = []
    color = {(0, 255, 0): "Green", (0, 127, 255):"Orange", (180, 0, 255):"Pink", (255, 255, 0):"Skyblue"}
    gray = cv.cvtColor(shop_, cv.COLOR_BGR2GRAY)
    _, thresh = cv.threshold(gray, 240, 255, cv.THRESH_BINARY)
    contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    for contour in contours:
        approx = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        #print(approx)
        shopr = []
        shopr.append('Shop_'+str(n))
        if x == 0 and y == 0:
            continue
        elif len(approx)==5:
            if x==60 and y==45:
                shopr.append(color[tuple(shop_[60, 60].tolist())])
                point = [n*100+70, n*100+70]
                shopr.append(point)
            elif x==20 and y==45:
                shopr.append(color[tuple(shop_[60, 20].tolist())])
                point = [n*100+30, n*100+70]
                shopr.append(point)
            elif x==20 and y==5:
                shopr.append(color[tuple(shop_[20, 20].tolist())]) 
                point = [n*100+30, n*100+30]
                shopr.append(point)
            elif x==60 and y==5:
                shopr.append(color[tuple(shop_[20, 60].tolist())]) 
                point = [n*100+70, n*100+30]
                shopr.append(point)
            shopr.append('Triangle')
        elif len(approx)==8:
            if x==49 and y==50:
                shopr.append(color[tuple(shop_[60, 60].tolist())])
                point = [n*100+70, n*100+70]
                shopr.append(point)
            elif x==9 and y==50:
                shopr.append(color[tuple(shop_[20, 60].tolist())])
                point = [n*100+30, n*100+70]
                shopr.append(point)
            elif x==9 and y==10:
                shopr.append(color[tuple(shop_[20, 20].tolist())]) 
                point = [n*100+30, n*100+30]
                shopr.append(point)
            elif x==49 and y==50:
                shopr.append(color[tuple(shop_[60, 20].tolist())])  
                point = [n*100+70, n*100+30]
                shopr.append(point) 
            shopr.append('Square')
        elif approx.ravel()[0]!=0 and approx.ravel()[1]!=0:
            if x==60 and y==47:
                shopr.append(color[tuple(shop_[60, 60].tolist())])
                point = [n*100+70, n*100+70]
                shopr.append(point)
            elif x==20 and y==47:
                shopr.append(color[tuple(shop_[20, 60].tolist())])
                point = [n*100+30, n*100+70]
                shopr.append(point)
            elif x==20 and y==7:
                shopr.append(color[tuple(shop_[20, 20].tolist())]) 
                point = [n*100+30, n*100+30]
                shopr.append(point)
            elif x==60 and y==7:
                shopr.append(color[tuple(shop_[60, 20].tolist())])  
                point = [n*100+70, n*100+30]
                shopr.append(point) 
            shopr.insert(2, 'Circle')
        shop_detail.append(shopr)
    shop_detail.sort()
    return shop_detail


p = image1[110:190, 210:290]
#cv.imshow('image32', p)
#print(p[20, 60])
#plt.imshow(p)
#plt.show()
print(shop(p, 1))
#plt.imshow(p)
#plt.show()
#print(p[60, 20])
#shop(p)            
cv.waitKey(0)
cv.destroyAllWindows()