import numpy as np
import cv2
import matplotlib.pyplot as plt


def shortestPath(graph, st, end, path = []):
	path = path + [st]
	if st==end:
		return path
	shortest = None
	for node in graph[st]:
		if node not in path:
			newpath = shortestPath(graph, node, end, path)
			if newpath:
				if not shortest or len(newpath)<len(shortest):
					shortest = newpath
	return shortest



def path_planning(graph, start, end):

	"""
	Purpose:
	---
	This function takes the graph(dict), start and end node for planning the shortest path

	** Note: You can use any path planning algorithm for this but need to produce the path in the form of 
	list given below **

	Input Arguments:
	---
	`graph` :	{ dictionary }
			dict of all connecting path
	`start` :	str
			name of start node
	`end` :		str
			name of end node


	Returns:
	---
	`backtrace_path` : [ list of nodes ]
			list of nodes, produced using path planning algorithm

		eg.: ['C6', 'C5', 'B5', 'B4', 'B3']
	
	Example call:
	---
	arena_parameters = detect_arena_parameters(maze_image)
	"""    

	backtrace_path=[]

	##############	ADD YOUR CODE HERE	##############
	nodes = {}
	for key in graph.keys():
		path = []
		for node in graph[key].keys():
			if graph[key][node] !=0:
				path = path + [node]
		nodes[key] = path

	backtrace_path = shortestPath(nodes, start, end)
	print(backtrace_path)
	##################################################


	return backtrace_path


graph = {'A1': {'B1': 1, 'A2': 1}, 'B1': {'A1': 1, 'C1': 1, 'B2': 1}, 'C1': {'B1': 1, 'D1': 1, 'C2': 1}, 'D1': {'C1': 1, 'E1': 1, 'D2': 1}, 'E1': {'D1': 1, 'F1': 1, 'E2': 1}, 'F1': {'E1': 1, 'F2': 1}, 'A2': {'B2': 1, 'A1': 1, 'A3': 1}, 'B2': {'A2': 1, 'C2': 1, 'B1': 1, 'B3': 1}, 'C2': {'B2': 1, 'D2': 1, 'C1': 1, 'C3': 1}, 'D2': {'C2': 1, 'E2': 1, 'D1': 1, 'D3': 1}, 'E2': {'D2': 1, 'F2': 1, 'E1': 1, 'E3': 0}, 'F2': {'E2': 1, 'F1': 1, 'F3': 1}, 'A3': {'B3': 1, 'A2': 1, 'A4': 0}, 'B3': {'A3': 1, 'C3': 1, 'B2': 1, 'B4': 1}, 'C3': {'B3': 1, 'D3': 1, 'C2': 1, 'C4': 1}, 'D3': {'C3': 1, 'E3': 1, 'D2': 1, 'D4': 1}, 'E3': {'D3': 1, 'F3': 1, 'E2': 0, 'E4': 1}, 'F3': {'E3': 1, 'F2': 1, 'F4': 1}, 'A4': {'B4': 1, 'A3': 0, 'A5': 0}, 'B4': {'A4': 1, 'C4': 1, 'B3': 1, 'B5': 0}, 'C4': {'B4': 1, 'D4': 1, 'C3': 1, 'C5': 1}, 'D4': {'C4': 1, 'E4': 1, 'D3': 1, 'D5': 1}, 'E4': {'D4': 1, 'F4': 0, 'E3': 1, 'E5': 0}, 'F4': {'E4': 0, 'F3': 1, 'F5': 1}, 'A5': {'B5': 1, 'A4': 0, 'A6': 1}, 'B5': {'A5': 1, 'C5': 1, 'B4': 0, 'B6': 1}, 'C5': {'B5': 1, 'D5': 1, 'C4': 1, 'C6': 0}, 'D5': {'C5': 1, 'E5': 0, 'D4': 1, 'D6': 1}, 'E5': {'D5': 0, 'F5': 0, 'E4': 0, 'E6': 0}, 'F5': {'E5': 0, 'F4': 1, 'F6': 0}, 'A6': {'B6': 1, 'A5': 1}, 'B6': {'A6': 1, 'C6': 1, 'B5': 1}, 'C6': {'B6': 1, 'D6': 1, 'C5': 0}, 'D6': {'C6': 1, 'E6': 1, 'D5': 1}, 'E6': {'D6': 1, 'F6': 0, 'E5': 0}, 'F6': {'E6': 0, 'F5': 0}}
st, end = 'E6', 'E4'
path_planning(graph, st, end)
