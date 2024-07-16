import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_all_nodes(image):
	"""
	Purpose:
	---
	This function takes the image as an argument and returns a list of
	nodes in which traffic signals, start_node and end_node are present in the image

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`traffic_signals, start_node, end_node` : [ list ], str, str
			list containing nodes in which traffic signals are present, start and end node too
	
	Example call:
	---
	traffic_signals, start_node, end_node = detect_all_nodes(maze_image)
	"""    
	traffic_signals = []
	start_node = ""
	end_node = ""

	##############	ADD YOUR CODE HERE	##############
	corner = "0ABCDEFG"
	for i in range(1, 7):
		for j in range(1, 7):
			if (image[i*100, j*100, 2]==255):
				traffic_signals.append(corner[j]+str(i))
			elif (image[i*100, j*100, 1]==255):
				start_node = corner[j]+str(i)
			elif (image[i*100, j*100, 0]!=255):
				end_node = corner[j]+str(i)
	traffic_signals.sort()
	##################################################
	# print(traffic_signals, start_node, end_node)
	return traffic_signals, start_node, end_node

img_dir_path = "test_images/"
for i in range(10):
    img_key = 'maze_00' + str(i)
    img_file_path = img_dir_path + img_key  + '.png'
    # read image using opencv
    image = cv2.imread(img_file_path)
    detect_all_nodes(image)
    # plt.imshow(image)
    # plt.show()