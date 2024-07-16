import numpy as np
import cv2
import matplotlib.pyplot as plt


def detect_paths_to_graph(image):
	"""
	Purpose:
	---
	This function takes the image as an argument and returns a dictionary of the
	connect path from a node to other nodes and will be used for path planning

	HINT: Check for the road besides the nodes for connectivity 

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`paths` : { dictionary }
			Every node's connection to other node and set it's value as edge value 
			Eg. : { "D3":{"C3":1, "E3":1, "D2":1, "D4":1}, 
					"D5":{"C5":1, "D2":1, "D6":1 }  }

			Why edge value 1? -->> since every road is equal

	Example call:
	---
	paths = detect_paths_to_graph(maze_image)
	"""    

	paths = {}

	##############	ADD YOUR CODE HERE	##############
	corner = "0ABCDEF"
	for i in range(1, 7):
		for j in range(1, 7):
			cor = {}
			if image[i*100, (j-1)*100+50, 1] == 255 and (j-1)!=0:
				cor[corner[j-1]+str(i)]=0
			elif (j-1)!=0:
				cor[corner[j-1]+str(i)]=1
			if image[i*100, (j)*100+50, 1] == 255 and (j+1)!=7:
				cor[corner[j+1]+str(i)] = 0
			elif (j+1)!=7:
				cor[corner[j+1]+str(i)] = 1
			if image[(i-1)*100+50, j*100, 1] == 255 and (i-1)!=0:
				cor[corner[j]+str(i-1)] = 0
			elif (i-1)!=0:
				cor[corner[j]+str(i-1)] = 1
			if image[i*100+50, j*100, 1] == 255 and (i+1)!=7:
				cor[corner[j]+str(i+1)] = 0
			elif (i+1)!=7:
				cor[corner[j]+str(i+1)] = 1
			paths[corner[j]+str(i)] = cor
		
	##################################################
	print(paths)

	return paths







img_dir_path = "test_images/"
for i in range(10):
    img_key = 'maze_00' + str(i)
    img_file_path = img_dir_path + img_key  + '.png'
    # read image using opencv
    image = cv2.imread(img_file_path)
    detect_paths_to_graph(image)
    # plt.imshow(image)
    # plt.show()