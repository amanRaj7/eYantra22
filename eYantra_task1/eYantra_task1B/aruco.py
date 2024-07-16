
from cv2 import aruco
import numpy as np
import cv2 as cv
import cv2
import math

path1 = r"D:\eYantra\eYantra_task1\test_pb_task1_windows\task_1B\public_test_cases\aruco_0.png"
path2 = r"D:\eYantra\eYantra_task1\test_pb_task1_windows\task_1B\public_test_cases\aruco_1.png"
image1 = cv.imread(path1)
image2 = cv.imread(path2)

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def detect_ArUco_details(image):

    """
    Purpose:
    ---
    This function takes the image as an argument and returns a dictionary such
    that the id of the ArUco marker is the key and a list of details of the marker
    is the value for each item in the dictionary. The list of details include the following
    parameters as the items in the given order
        [center co-ordinates, angle from the vertical, list of corner co-ordinates] 
    This order should be strictly maintained in the output

    Input Arguments:
    ---
    `image` :	[ numpy array ]
            numpy array of image returned by cv2 library
    Returns:
    ---
    `ArUco_details_dict` : { dictionary }
            dictionary containing the details regarding the ArUco marker
    
    Example call:
    ---
    ArUco_details_dict = detect_ArUco_details(image)
    """    
    ArUco_details_dict = {} #should be sorted in ascending order of ids
    ArUco_corners = {}
    
    ##############	ADD YOUR CODE HERE	##############
    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
    parameters =  aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    for (markerCorner, markerID) in zip(corners, ids):
        # extract the marker corners (which are always returned in
        # top-left, top-right, bottom-right, and bottom-left order)
        
        corners = markerCorner.reshape((4, 2))
        (topLeft, topRight, bottomRight, bottomLeft) = corners

        x_sum = markerCorner[0][0][0] + markerCorner[0][1][0] + markerCorner[0][2][0] + markerCorner[0][3][0]
        y_sum = markerCorner[0][0][1] + markerCorner[0][1][1] + markerCorner[0][2][1] + markerCorner[0][3][1]
        x_cent = x_sum/4
        y_cent= y_sum/4 
        x_centre = int(x_sum/4)	
        y_centre = int(y_sum/4)
        # num = y_cent-topLeft[1]
        # deno = x_cent-topLeft[0]
        # angle = (topRight[1]-topLeft[1])/(distance(topLeft, topRight))
        #angle = (math.degrees(math.atan(angle)))+90
        #if angle >= 180:
        #    angle = 180 - (angle-180)
        #else:
        #    angle = angle
        # slope = num/deno
        # if deno > 0 :
        #     if num < 0 :
        #         mid_x = (markerCorner[0][2][0] + markerCorner[0][3][0])/2
        #         mid_y = (markerCorner[0][2][1] + markerCorner[0][3][1])/2
        #         num  = (mid_x - x_cent)
        #         deno = (mid_y - y_cent)
        #         slope = num/deno
        #         angle= math.degrees(math.atan(slope))
        #         angle = int(180+angle)
        #     elif num > 0 :
        #         angle= math.degrees(math.atan(slope))
        #         angle = int(180-angle)
        # else :
        #     angle = math.degrees(math.atan(slope))
        #     angle = int(angle)
        # angle = int(angle)
        # angle = (math.degrees(math.acos((topRight[0]-topLeft[0])/distance(topLeft, topRight))))
        # mid_x = (markerCorner[0][2][0] + markerCorner[0][3][0])/2
        # mid_y = (markerCorner[0][2][1] + markerCorner[0][3][1])/2
        # x = (mid_x-x_cent)
        # y = (mid_y-y_cent)
        # # if x<0 and y<0:
        # #     angle = -(180 + angle)  #thik hai
        # if x>0 and y>0:
        #     angle = angle #thik hai
        # elif x<0 and y<0:
        #     angle = -angle
        # elif x<0 and y>0:
        #     angle = -angle
        # elif x>0 and y<0:
        #     angle = 180 - angle #thik hai
        
        # if angle<0:
        #     angle  = -(180 + angle)
        y = topLeft[1]-topRight[1]
        x = topLeft[0]-topRight[1]
        angle = math.degrees(math.atan2(y, -x))
        # if x>0 and y>0:
        #     angle = angle
        # elif x>0 and y<0:
        #     angle = 180-angle
        # elif x<0 and y>0:
        #     angle = -angle
        # elif x<0 and y<0:
        #     angle = -(90+angle)

        angle = int(angle)

        for i in markerID:
            ArUco_details_dict[int(i)] = [[x_centre, y_centre], angle]
            ArUco_corners[int(i)] = corners

    ##################################################
    
    return ArUco_details_dict, ArUco_corners

def mark_ArUco_image(image,ArUco_details_dict, ArUco_corners):

    for ids, details in ArUco_details_dict.items():
        center = details[0]
        cv2.circle(image, center, 5, (0,0,255), -1)

        corner = ArUco_corners[int(ids)]
        cv2.circle(image, (int(corner[0][0]), int(corner[0][1])), 5, (50, 50, 50), -1)
        cv2.circle(image, (int(corner[1][0]), int(corner[1][1])), 5, (0, 255, 0), -1)
        cv2.circle(image, (int(corner[2][0]), int(corner[2][1])), 5, (128, 0, 255), -1)
        cv2.circle(image, (int(corner[3][0]), int(corner[3][1])), 5, (255, 255, 255), -1)

        tl_tr_center_x = int((corner[0][0] + corner[1][0]) / 2)
        tl_tr_center_y = int((corner[0][1] + corner[1][1]) / 2) 

        cv2.line(image,center,(tl_tr_center_x, tl_tr_center_y),(255,0,0),5)
        display_offset = 2*int(math.sqrt((tl_tr_center_x - center[0])**2+(tl_tr_center_y - center[1])**2))
        cv2.putText(image,str(ids),(center[0]+int(display_offset/2),center[1]),cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        angle = details[1]
        cv2.putText(image,str(angle),(center[0]-display_offset,center[1]),cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    return image 

cv.imshow('image1', image1)
ArUco_details_dict, ArUco_corners = detect_ArUco_details(image1)

new_image = mark_ArUco_image(image1, ArUco_details_dict, ArUco_corners)
cv.imshow('newimage', new_image)
cv.waitKey(0)
cv.destroyAllWindows()