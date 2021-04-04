"""This module defines an A* search"""
from node_a import Node_A
import math as math
import heapq as heapq

#step constants 
RIGHT = (1, 0)
LEFT = (-1, 0)
UP = (0, 1)
DOWN = (0, -1)
UP_RIGHT = (1, 1)
UP_LEFT = (-1, 1)
DOWN_RIGHT = (1, -1)
DOWN_LEFT = (-1,-1)


GREY = (25, 25, 25)
WHITE = (255, 255, 255)

# dimensions for screen ... could add a settings module to organize
WIDTH = 800
HEIGHT = 400

def a_star(graph, start, end, screen):
# initialize start and end nodes
	start_node = Node_A(None, start)
	end_node = Node_A(None, end)
# change to PRIORITY QUEUE
# create lists for open/closed nodes
	open_list = []
	closed_list = []

# add start to open list
	heapq.heappush(open_list, start_node)
	loop_count = 0
	while len(open_list) > 0:	
	
# set current_node to first node in open_list
#		current_node = open_list[0] i think this does nothing since heappop runs on line 39 anyway

# move smallest priority node from open --> closed
		current_node = heapq.heappop(open_list)
		closed_list.append(current_node)

# check if reached goal
		if current_node == end_node:
			path = []

# backtrack from goal --> parent ... --> start
			current = current_node

			while current is not None:
				path.append(current.position)
				current = current.parent
# return path, reversed
			return path[::1]

# get neighbors by adding 1 to (x,y) in each direction
		neighbors = []
		for step in [(LEFT), (RIGHT), (UP), (DOWN), (UP_LEFT), 
						(UP_RIGHT), (DOWN_LEFT), (DOWN_RIGHT)]:
			node_position = ( current_node.position[0] + step[0], 
							  current_node.position[1] + step[1] )

# check if position is outside the graph
			if node_position[0] < 0 or node_position[0] > WIDTH or \
				node_position[1] < 0 or node_position[1] > HEIGHT:
				closed_node = Node_A(current_node, node_position)
				closed_list.append(closed_node)
				continue

# check if position is obstacle
			# for obstacle in obstacles:
			# 	if obstacle.collidepoint(node_position):
			# 		closed_node = Node(current_node, node_position)
			# 		if closed_node not in closed_list:
			# 			closed_list.append(closed_node)
			if screen.get_at(node_position) != GREY:
				closed_node = Node_A(current_node, node_position)
				closed_list.append(closed_node)
				screen.set_at(node_position, WHITE)
				continue
# create new node and add to neighbors
			new_node = Node_A(current_node, node_position)
			neighbors.append(new_node)

# loop through neighbors
		for neighbor in neighbors:
	# skip if node is in closed_list
			if neighbor in closed_list:
				continue
			
	# otherwise calculate scores
			neighbor.g_score = current_node.g_score + 1 
			neighbor.h_score = distance_to_goal(neighbor.position, end) 
			neighbor.f_score = neighbor.g_score + neighbor.h_score

# if not already in open_list, add node
			if neighbor not in open_list:
				# open_list.append(neighbor)
				heapq.heappush(open_list, neighbor)
# check open_list and don't add if g_score is worse
			for open_node in open_list:
				if neighbor == open_node and neighbor.g_score > open_node.g_score:
					continue
		
		loop_count+=1	
		print("G_SCORE: " + str(current_node.g_score)
			+ "H_SCORE: " + str(current_node.h_score))

	return "didn't find goal"

# function to get the h_score
def distance_to_goal(position, goal):
	pos_x = position[0] 
	pos_y = position[1] 

	goal_x = goal[0]
	goal_y = goal[1]

	distance = ( (goal_x - pos_x)**2 ) + ( (goal_y - pos_y)**2 )
	return distance


"""old version that used list instead of heap"""
def a_star_legacy(graph, start, end, shapes):

# initialize start and end nodes
	start_node = Node_A(None, start)
	end_node = Node_A(None, end)
# change to PRIORITY QUEUE
# create lists for open/closed nodes
	open_list = []
	closed_list = []

# add start to open list
	open_list.append(start_node)
	loop_count = 0
	while len(open_list) > 0:
		print('this is iteration ', loop_count)
		
# set current_node to first Node_A in open_list
		current_node = open_list[0]
		current_index = 0
		

# iterate through open_list to find Node_A with lowest f_score
		for index, item in enumerate(open_list):
			if item.f_score < current_node.f_score:
				current_node = item
				current_index = index

# move selected node from open --> closed
		open_list.pop(current_index)
		closed_list.append(current_node)

# check if reached goal
		if current_node == end_node:
			path = []

# backtrack from goal --> parent ... --> start
			current = current_node

			while current is not None:
				path.append(current.position)
				current = current.parent
# return path, reversed
			return path[::1]

# get neighbors by adding 1 to (x,y) in each direction
		neighbors = []
		for step in [(LEFT), (RIGHT), (UP), (DOWN), (UP_LEFT), 
						(UP_RIGHT), (DOWN_LEFT), (DOWN_RIGHT)]:
			node_position = ( current_node.position[0] + step[0], 
							  current_node.position[1] + step[1] )

# check if position is outside the graph
			if node_position[0] < 0 or node_position[0] > WIDTH or \
				node_position[1] < 0 or node_position[1] > HEIGHT:
				print(node_position, ' is out of bounds')
				closed_node = Node_A(current_node, node_position)
				closed_list.append(closed_node)
				continue

# check if position is obstacle
	# not sure on how to do this on actual graph but can confirm later
		# need to change this if statement to check against tuple in list
			for shape in shapes:
				if shape.collidepoint(node_position):
					print(node_position, 'is an obstacle')
					closed_node = Node_A(current_node, node_position)
					if closed_node not in closed_list:
						closed_list.append(closed_node)
						print('added ', closed_node.position, ' to closed_list')
			
			# if graph[node_position[0]][node_position[1]] == 1:

			# 	print(node_position, 'is an obstacle')
			# 	closed_node = Node_A(current_node, node_position)
			# 	if closed_node not in closed_list:
			# 		closed_list.append(closed_node)
			# 		print('added ', closed_node.position, ' to closed_list')
			# 	continue

# create new Node_A and add to neighbors
			new_node = Node_A(current_node, node_position)
			neighbors.append(new_node)


# loop through neighbors
		for neighbor in neighbors:
	# skip if node is in closed_list
			if neighbor in closed_list:
				continue
			#for closed in closed_list: # check for specific value instead of loop thru whole list
				#if closed == neighbor:
					#continue
	# otherwise calculate scores
			neighbor.g_score = current_node.g_score + 1 
			neighbor.h_score = distance_to_goal(neighbor.position, end) 
			neighbor.f_score = neighbor.g_score + neighbor.h_score

# if not already in open_list, add node
			if neighbor not in open_list:
				open_list.append(neighbor)
				print('added ', neighbor.position, ' to open list')
# check open_list and don't add if g_score is worse
			for open_node in open_list:
				if neighbor == open_node and neighbor.g_score > open_node.g_score:
					continue
			
# if neighbor already exists in list
# 			if neighbor in open_list:
# 				print('located neigbhor in open list')
# 				index = open_list.index(neighbor)
# 				match = open_list[index]
# 				print('neighbor: ', neighbor.f_score, ' match ',  match.f_score)
# # compare f_scores and replace if necessary
# 				if neighbor.f_score < match.f_score:
# 					match.f_score = neighbor.f_score
# 					print('replaced: ', neighbor.f_score, ' with ',  match.f_score)

		# for open_node in open_list:
		# 	if neighbor == open_node and neighbor.f_score > open_node.f_score:
		# 		continue
# add neighbor to open_list if not already present OR
# if present AND f_score >> then update f_score
			# open_list.append(open_node)
			# print(open_list)
		loop_count+=1	
		print("G_SCORE: " + str(current_node.g_score)
			+ " H_SCORE: " + str(current_node.h_score))
	return "didn't find goal"





