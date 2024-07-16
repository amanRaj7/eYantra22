direction = 1
	for i in range(1, len(paths)):
		# if paths[i] in traffic_signal:
		# 	list_moves.append('WAIT_5')
		if ((paths[i][0]==paths[i-1][0]) and direction==1) or ((paths[i][1]==paths[i-1][1]) and direction==0):
			list_moves.append('STRAIGHT')
		elif (direction==1) and (paths[i][0]<paths[i-1][0]):
			list_moves.append('LEFT')
			direction = 0
		elif (direction==1) and (paths[i][0]>paths[i-1][0]):
			list_moves.append('RIGHT')
			direction = 0
		elif (direction==0) and paths[i][1]<paths[i-1][1]:
			list_moves.append('RIGHT')
			direction = 1
		elif (direction==0) and paths[i][1]>paths[i-1][1]:
			list_moves.append('LEFT')
			direction = 1
		if paths[i] in traffic_signal:
			list_moves.append('WAIT_5')