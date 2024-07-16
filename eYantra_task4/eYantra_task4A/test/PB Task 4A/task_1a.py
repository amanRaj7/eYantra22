'''
*****************************************************************************************
*
*        		===============================================
*           		Pharma Bot (PB) Theme (eYRC 2022-23)
*        		===============================================
*
*  This script is to implement Task 1A of Pharma Bot (PB) Theme (eYRC 2022-23).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:			[ PB_2256 ]
# Author List:		[ Aman Raj ]
# Filename:			task_1a.py
# Functions:		detect_traffic_signals, detect_horizontal_roads_under_construction, detect_vertical_roads_under_construction,
#					detect_medicine_packages, detect_arena_parameters
# 					[ shop ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv)                    ##
##############################################################
import cv2
import numpy as np
##############################################################

################# ADD UTILITY FUNCTIONS HERE #################
def shop(shop_, n):
    shop_detail = []
    color = {(0, 255, 0): "Green", (0, 127, 255):"Orange", (180, 0, 255):"Pink", (255, 255, 0):"Skyblue"}
    gray = cv2.cvtColor(shop_, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
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
                point = [n*100+70, 1*100+70-1]
                shopr.append(point)
            elif x==20 and y==45:
                shopr.append(color[tuple(shop_[60, 20].tolist())])
                point = [n*100+30, 1*100+70-1]
                shopr.append(point)
            elif x==20 and y==5:
                shopr.append(color[tuple(shop_[20, 20].tolist())]) 
                point = [n*100+30, 1*100+30-1]
                shopr.append(point)
            elif x==60 and y==5:
                shopr.append(color[tuple(shop_[20, 60].tolist())]) 
                point = [n*100+70, 1*100+30-1]
                shopr.append(point)
            shopr.insert(2, 'Triangle')
        elif len(approx)==8:
            if x==49 and y==50:
                shopr.append(color[tuple(shop_[60, 60].tolist())])
                point = [n*100+70, 1*100+70]
                shopr.append(point)
            elif x==9 and y==50:
                shopr.append(color[tuple(shop_[60, 20].tolist())])
                point = [n*100+30, 1*100+70]
                shopr.append(point)
            elif x==9 and y==10:
                shopr.append(color[tuple(shop_[20, 20].tolist())]) 
                point = [n*100+30, 1*100+30]
                shopr.append(point)
            elif x==49 and y==10:
                shopr.append(color[tuple(shop_[20, 60].tolist())])  
                point = [n*100+70, 1*100+30]
                shopr.append(point) 
            shopr.insert(2, 'Square')
        elif approx.ravel()[0]!=0 and approx.ravel()[1]!=0:
            if x==60 and y==47:
                shopr.append(color[tuple(shop_[60, 60].tolist())])
                point = [n*100+70, 1*100+70]
                shopr.append(point)
            elif x==20 and y==47:
                shopr.append(color[tuple(shop_[60, 20].tolist())])
                point = [n*100+30, 1*100+70]
                shopr.append(point)
            elif x==20 and y==7:
                shopr.append(color[tuple(shop_[20, 20].tolist())]) 
                point = [n*100+30, 1*100+30]
                shopr.append(point)
            elif x==60 and y==7:
                shopr.append(color[tuple(shop_[20, 60].tolist())])  
                point = [n*100+70, 1*100+30]
                shopr.append(point) 
            shopr.insert(2, 'Circle')
        shop_detail.append(shopr)
    shop_detail.sort()
    return shop_detail

##############################################################

def detect_traffic_signals(maze_image):

	"""
	Purpose:
	---
	This function takes the image as an argument and returns a list of
	nodes in which traffic signals are present in the image
	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`traffic_signals` : [ list ]
			list containing nodes in which traffic signals are present
	
	Example call:
	---
	traffic_signals = detect_traffic_signals(maze_image)
	"""    
	traffic_signals = []

	##############	ADD YOUR CODE HERE	##############
	corner = "0ABCDEFG"
	for i in range(1, 7):
		for j in range(1, 7):
			if (maze_image[i*100, j*100, 2]==255):
				traffic_signals.append(corner[j]+str(i))
			elif (maze_image[i*100, j*100, 1]==255):
				start_node = corner[j]+str(i)
			elif (maze_image[i*100, j*100, 0]!=255):
				end_node = corner[j]+str(i)
	traffic_signals.sort()
	##################################################
	
	return traffic_signals
	

def detect_horizontal_roads_under_construction(maze_image):
	
	"""
	Purpose:
	---
	This function takes the image as an argument and returns a list
	containing the missing horizontal links
	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`horizontal_roads_under_construction` : [ list ]
			list containing missing horizontal links
	
	Example call:
	---
	horizontal_roads_under_construction = detect_horizontal_roads_under_construction(maze_image)
	"""    
	horizontal_roads_under_construction = []

	##############	ADD YOUR CODE HERE	##############
	corner = "0ABCDEFG"
    #plt.imshow(image)
    #plt.show()
	for i in range(1, 7):
		for j in range(1, 6):
			if(maze_image[i*100, j*100+50, 0]==255) and (maze_image[i*100, j*100+50, 1]==255) and (maze_image[i*100, j*100+50, 2]==255):
				horizontal_roads_under_construction.append(corner[j]+str(i)+'-'+corner[j+1]+str(i))
	horizontal_roads_under_construction.sort()
	##################################################
	
	return horizontal_roads_under_construction	

def detect_vertical_roads_under_construction(maze_image):

	"""
	Purpose:
	---
	This function takes the image as an argument and returns a list
	containing the missing vertical links
	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`vertical_roads_under_construction` : [ list ]
			list containing missing vertical links
	
	Example call:
	---
	vertical_roads_under_construction = detect_vertical_roads_under_construction(maze_image)
	"""    
	vertical_roads_under_construction = []

	##############	ADD YOUR CODE HERE	##############
	corner = "0ABCDEFG"
    #plt.imshow(image)
    #plt.show()
	for i in range(1, 6):
		for j in range(1, 7):
			if(maze_image[i*100+50, j*100, 0]==255) and (maze_image[i*100+50, j*100, 1]==255) and (maze_image[i*100+50, j*100, 2]==255):
				vertical_roads_under_construction.append(corner[j]+str(i)+'-'+corner[j]+str(i+1))
	vertical_roads_under_construction.sort()
	##################################################
	
	return vertical_roads_under_construction


def detect_medicine_packages(maze_image):

	"""
	Purpose:
	---
	This function takes the image as an argument and returns a nested list of
	details of the medicine packages placed in different shops
	** Please note that the shop packages should be sorted in the ASCENDING order of shop numbers 
	   as well as in the alphabetical order of colors.
	   For example, the list should first have the packages of shop_1 listed. 
	   For the shop_1 packages, the packages should be sorted in the alphabetical order of color ie Green, Orange, Pink and Skyblue.
	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`medicine_packages` : [ list ]
			nested list containing details of the medicine packages present.
			Each element of this list will contain 
			- Shop number as Shop_n
			- Color of the package as a string
			- Shape of the package as a string
			- Centroid co-ordinates of the package
	Example call:
	---
	medicine_packages = detect_medicine_packages(maze_image)
	"""    
	medicine_packages_present = []

	##############	ADD YOUR CODE HERE	##############
	for i in range(1, 6):
		for j in shop(maze_image[110:190, i*100+10:i*100+90], i):
			medicine_packages_present.append(j)
	##################################################

	return medicine_packages_present

def detect_arena_parameters(maze_image):

	"""
	Purpose:
	---
	This function takes the image as an argument and returns a dictionary
	containing the details of the different arena parameters in that image
	The arena parameters are of four categories:
	i) traffic_signals : list of nodes having a traffic signal
	ii) horizontal_roads_under_construction : list of missing horizontal links
	iii) vertical_roads_under_construction : list of missing vertical links
	iv) medicine_packages : list containing details of medicine packages
	These four categories constitute the four keys of the dictionary
	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`arena_parameters` : { dictionary }
			dictionary containing details of the arena parameters
	
	Example call:
	---
	arena_parameters = detect_arena_parameters(maze_image)
	"""    
	arena_parameters = {}

	##############	ADD YOUR CODE HERE	##############
	arena_parameters['traffic_signals'], arena_parameters["start_node"], arena_parameters['end_node'] = detect_traffic_signals(maze_image)
	arena_parameters['horizontal_roads_under_construction'] = detect_horizontal_roads_under_construction(maze_image)
	arena_parameters['vertical_roads_under_construction'] = detect_vertical_roads_under_construction(maze_image)
	arena_parameters['medicine_packages'] = detect_medicine_packages(maze_image)
	##################################################
	
	return arena_parameters

######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THIS FUNCTION #########	

if __name__ == "__main__":

    # path directory of images in test_images folder
	img_dir_path = "public_test_images/"

    # path to 'maze_0.png' image file
	file_num = 0
	img_file_path = img_dir_path + 'maze_' + str(file_num) + '.png'
	
	# read image using opencv
	maze_image = cv2.imread(img_file_path)
	
	print('\n============================================')
	print('\nFor maze_' + str(file_num) + '.png')

	# detect and print the arena parameters from the image
	arena_parameters = detect_arena_parameters(maze_image)

	print("Arena Prameters: " , arena_parameters)

	# display the maze image
	cv2.imshow("image", maze_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	choice = input('\nDo you want to run your script on all test images ? => "y" or "n": ')
	
	if choice == 'y':

		for file_num in range(1, 15):
			
			# path to maze image file
			img_file_path = img_dir_path + 'maze_' + str(file_num) + '.png'
			
			# read image using opencv
			maze_image = cv2.imread(img_file_path)
	
			print('\n============================================')
			print('\nFor maze_' + str(file_num) + '.png')
			
			# detect and print the arena parameters from the image
			arena_parameters = detect_arena_parameters(maze_image)

			print("Arena Parameter: ", arena_parameters)
				
			# display the test image
			cv2.imshow("image", maze_image)
			cv2.waitKey(2000)
			cv2.destroyAllWindows()