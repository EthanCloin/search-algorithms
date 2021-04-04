"""This module defines an potential cost search"""
from node import Node
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

# color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (25, 25, 25)
LIGHT_GREY = (66, 66, 66)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)

# dimensions for screen ... could add a settings module to organize
WIDTH = 800
HEIGHT = 400


def potential_cost_search(graph, start, end, obstacles, constraint, screen):
	
	# check if path is possible via admissible heuristic
	if distance_to_goal(start, end) > constraint:

		return "impossible"

	# Intialize START and GOAL
	start_node = Node(None, start)
	end_node = Node(None, end)

	# Initialize OPEN as a heap of nodes
	open_list = []
	# Initialize CLOSED as a list of nodes
	closed_list = []
	
	# Heappop will return highest U_SCORE
	# Calculate scores and push START to heap
	start_node.h_score = distance_to_goal(start_node.position, end)
	start_node.u_score = calculate_u_score(start_node, constraint)
	heapq.heappush(open_list, start_node)

	loop_count = 0

	# Loop until OPEN is empty
	while open_list:
		# Pop node from OPEN and append to CLOSED
		current_node = heapq.heappop(open_list)
		closed_list.append(current_node)
		# print("Looking at: " + str(current_node.position) + 
		# 		" with USCORE: " + str(current_node.u_score) +
		# 		" with path cost: " + str(current_node.g_score))

		# Get neighbors by step method
		for step in [(LEFT), (RIGHT), (UP), (DOWN), (UP_LEFT), 
						(UP_RIGHT), (DOWN_LEFT), (DOWN_RIGHT)]:
			
			neighbor_position = ( current_node.position[0] + step[0], 
							  current_node.position[1] + step[1] )
			
			# creating neighbor node with scores
			neighbor = Node(current_node, neighbor_position)
			neighbor.g_score = current_node.g_score + 1
			neighbor.h_score = distance_to_goal(neighbor.position, end)

			# Skip neighbor if path cost >= CONSTRAINT
			if neighbor.g_score + neighbor.h_score >= constraint:
				continue
			
			# Skip neighbor if in OPEN with neighbor.GSCORE > stored.GSCORE
			# neighbor_in_open = False
			# if neighbor in open_list:
			# 	skip = False
			# 	neighbor_in_open = True
			# 	for stored_node in open_list:
			# 		if stored_node == neighbor:
			# 			if neighbor.g_score > stored_node.g_score:
			# 				skip = True
			# 				break
			# 	if skip:
			# 		continue # this could probably be optimized
			
			# If neighbor == GOAL, return path by backtracking
			if neighbor.position == end:
				path = []
				current = neighbor					
				while current is not None:
					path.append(current.position)
					current = current.parent
				print("CONSTRAINT: " + str(constraint))
				print("APPROX PATH LEN: " + str(len(path)))
				return path[::1]
			
			# slow version of obstacle, bounds checking TEMP DISABLED
			# skip = False
			# for obstacle in obstacles:
			# 	if obstacle.collidepoint(neighbor.position):
			# 		closed_list.append(neighbor)
			# 		skip = True
			# 		break
			# if skip:
			# 	continue

			if neighbor.position[0] < 0 or neighbor.position[0] > WIDTH or \
				neighbor.position[1] < 0 or neighbor.position[1] > HEIGHT:
				closed_list.append(neighbor)
				continue
			
			# if unexpected color aka obstacle, add to closed list
			if screen.get_at(neighbor.position) != GREY:
				closed_list.append(neighbor)
				screen.set_at(neighbor.position, WHITE)
				continue
				

			# If neighbor already in OPEN, update GSCORE + USCORE
			neighbor_in_open = False
			for stored_node in open_list:
				if stored_node == neighbor:
					neighbor_in_open = True
					stored_node.g_score = neighbor.g_score
					stored_node.u_score = calculate_u_score(stored_node, constraint)
					break

			if not neighbor_in_open:
				# calculate USCORE
				neighbor.u_score = calculate_u_score(neighbor, constraint)
				# push neighbor onto OPEN
				heapq.heappush(open_list, neighbor)

			# Skip neighbor if in CLOSED(obstacle/bounds)
			if neighbor in closed_list:
				continue

		loop_count += 1
		print (loop_count)
		if loop_count == 10000:
			return"impossible"
	
	return "impossible"

	
def testing_heap():
	test_heap = []

	for num in range(11):
		if num % 3 == 0:
			new_node = Node(None, (-11 + num, 6 + num))
			new_node.u_score = -1 *(20 + num)
			print('added node with U_SCORE: ' + str(new_node.u_score))
			heapq.heappush(test_heap, new_node)

			continue
		new_node = Node(None, (0 + num, 0 + num))
		new_node.u_score = -1 * (100 - num)

		heapq.heappush(test_heap, new_node)
		print('added node with U_SCORE: ' + str(new_node.u_score))

	while test_heap:
		node = heapq.heappop(test_heap)
		print('U: ' + str(node.u_score) + ' Pos: ' + str(node.position))


def define_obstacle_points(graph, obstacles):
	blocked = set()
	for obstacle in obstacles:
		print('got one')
		for position in graph:
			if position in obstacle:
				blocked.add(position)
	print(blocked)
	return blocked














""" ATTEMPT TWO """
# def potential_cost_search(graph, start, end, obstacles, constraint):
# 	print('called function')
# 	# initialize start and end nodes
# 	start_node = Node(None, start)
# 	start_node.h_score = distance_to_goal(start, end)
# 	start_node.u_score = calculate_u_score(start_node, constraint)

# 	end_node = Node(None, end)

# 	# create heaps for open/closed 
# 	open_list = []
# 	closed_list = []

# 	#push start onto heap
# 	heapq.heappush(open_list, start_node)

# 	while len(open_list) > 0:
# 		# pop node from heap with greatest u_score
# 		current_node = heapq.heappop(open_list)
# 		print("Current Position: " + str(current_node.position))
# 		print("Current U_SCORE: " + str(current_node.u_score))
		
# 		# get neighbors
# 		neighbors = []
# 		for step in [(LEFT), (RIGHT), (UP), (DOWN), (UP_LEFT), 
# 					(UP_RIGHT), (DOWN_LEFT), (DOWN_RIGHT)]:

# 			node_position = ( current_node.position[0] + step[0], 
# 						  current_node.position[1] + step[1] )
			

# 			# ignore closed nodes
# 			# if new_node in closed_list:
# 			# 	continue
			
# 			# ignore out of bounds
# 			if node_position[0] < 0 or node_position[0] > WIDTH or \
# 				node_position[1] < 0 or node_position[1] > HEIGHT:
# 				closed_node = Node(current_node, node_position)
# 				closed_list.append(closed_node)
# 				continue
			
# 			# ignore obstacles
# 			for obstacle in obstacles:
# 				if obstacle.collidepoint(node_position):
# 					closed_node = Node(current_node, node_position)
# 					if closed_node not in closed_list:
# 						closed_list.append(closed_node)

# 			# add valid node to neighbors
# 			neighbors.append(Node(current_node, node_position))

# 			# update node to best g_score or skip
# 			# if new_node in open_list:
# 			# 	ignore = False
# 			# 	for stored_node in open_list:
# 			# 		if stored_node == new_node:
# 			# 			# ignore if g_score greater than node stored in open_list
# 			# 			if new_node.g_score >= stored_node.g_score:
# 			# 				ignore = True
# 			# 				print('executed sus search for big g')
# 			# 	if ignore:
# 			# 		continue
# 		for new_node in neighbors:
# 			# create heuristic values
# 			new_node.g_score = new_node.parent.g_score + 1
# 			new_node.h_score = distance_to_goal(new_node.position, end)
# 			# check if node fits constraint
# 			if new_node.g_score + new_node.h_score > constraint:
# 				closed_list.append(new_node)
# 				continue

# 			# check if node is at goal
# 			if new_node == end_node:
# 				path = []

# 			# backtrack from goal --> parent ... --> start
# 				current = current_node

# 				while current is not None:
# 					path.append(current.position)
# 					current = current.parent
# 			# return path, reversed
# 				return path[::1]

# 			# add new_node to open or update location
# 			if new_node in open_list:
# 				# loop through list until find and replace g_score
# 				for stored_node in open_list:
# 					if stored_node == new_node:
# 						stored_node.g_score = new_node.g_score
# 						stored_node.h_score = calculate_u_score(stored_node, constraint)
			
# 			# add node to open_list
# 			else: 
# 				new_node.u_score = calculate_u_score(new_node, constraint)
# 				heapq.heappush(open_list, new_node)
# 	return "failure"



""" ATTEMPT ONE """
# def potential_cost_search(graph, start, end, obstacles, constraint):

# 	# initialize start and end nodes
# 	start_node = Node(None, start)
# 	end_node = Node(None, end)

# 	# create lists for open/closed nodes
# 	open_list = []
# 	closed_list = []

# 	# add start to open list
# 	heapq.heappush(open_list, start_node)
# 	loop_count = 0
# 	while len(open_list) > 0:	
# 		print("looping...")	
# 	# set current_node to first node in open_list doesn't matter
# 	#	current_node = open_list[0]
# 	#	current_index = 0

# 	# move smallest priority node from open --> closed
# 		current_node = heapq.heappop(open_list)
# 		closed_list.append(current_node)

# 	# check if reached goal
# 		if current_node == end_node:
# 			path = []

# 	# backtrack from goal --> parent ... --> start
# 			current = current_node

# 			while current is not None:
# 				path.append(current.position)
# 				current = current.parent
# 	# return path, reversed
# 			if len(path) > constraint:
# 				print("Sorry bud not gonna happen")
# 				return
# 			else: 
# 				return path[::1]

# 	# get neighbors by adding 1 to (x,y) in each direction
# 		neighbors = []
# 		for step in [(LEFT), (RIGHT), (UP), (DOWN), (UP_LEFT), 
# 						(UP_RIGHT), (DOWN_LEFT), (DOWN_RIGHT)]:
# 			node_position = ( current_node.position[0] + step[0], 
# 							  current_node.position[1] + step[1] )

# 	# check if position is outside the graph
# 			if node_position[0] < 0 or node_position[0] > WIDTH or \
# 				node_position[1] < 0 or node_position[1] > HEIGHT:
# 				closed_node = Node(current_node, node_position)
# 				closed_list.append(closed_node)
# 				continue

# 	# check if position is obstacle
# 			for obstacle in obstacles:
# 				if obstacle.collidepoint(node_position):
# 					closed_node = Node(current_node, node_position)
# 					if closed_node not in closed_list:
# 						closed_list.append(closed_node)

# 	# create new node and add to neighbors
# 			new_node = Node(current_node, node_position)
# 			neighbors.append(new_node)

# 	# loop through neighbors
# 		for neighbor in neighbors:
# 	# skip if node is in closed_list
# 			if neighbor in closed_list:
# 				continue
			
# 	# otherwise calculate scores
# 			neighbor.g_score = current_node.g_score + 1 
# 			neighbor.h_score = distance_to_goal(neighbor.position, end) 
# 			neighbor.u_score = calculate_u_score(neighbor, constraint)
# 			print("u_score: ", neighbor.u_score)

# 	# if not already in open_list, add node
# 			if neighbor not in open_list:
# 				heapq.heappush(open_list, neighbor)
# 	# check open_list and don't add if g_score is worse
# 			for open_node in open_list:
# 				if neighbor == open_node and neighbor.g_score > open_node.g_score:
# 					continue
		
# 		loop_count+=1	
# 		if (loop_count > 5000):
# 			return "too long bruh"
# 	return "didn't find goal"



# function to get the h_score
def distance_to_goal(position, goal):
	pos_x = position[0] 
	pos_y = position[1] 

	goal_x = goal[0]
	goal_y = goal[1]

	distance = ( (goal_x - pos_x)**2 ) + ( (goal_y - pos_y)**2 )
	return math.sqrt(distance)

def calculate_u_score(node, constraint):
	numerator = constraint - node.g_score
	denominator = node.h_score

	# Make value negative so heap sorts by greatest
	u_score = -1 * (numerator / denominator)

	return u_score











