from node import Node
import math 
import numpy as np

# dimensions for screen
WIDTH = 800
HEIGHT = 400
#step constants 
RIGHT = (1, 0)
LEFT = (-1, 0)
UP = (0, 1)
DOWN = (0, -1)
UP_RIGHT = (1, 1)
UP_LEFT = (-1, 1)
DOWN_RIGHT = (1, -1)
DOWN_LEFT = (-1,-1)

def hill_climbing(graph, start, goal, obstacles):
	# initialize start as current_node
	current_node = Node(None, start)
	current_node.h_score = distance_to_goal(current_node.position, goal)
	print("Starting H_SCORE: " + str(current_node.h_score))

	# keep track of visited nodes for visualization
	visited_nodes = []
	visited_nodes.append(current_node.position)

	searching = True
	while searching:
		# check if goal is reached
		if current_node.h_score == 0:
			return visited_nodes

		# get list of valid neighbors
		neighbors = []
		for step in [(LEFT), (RIGHT), (UP), (DOWN), (UP_LEFT), 
						(UP_RIGHT), (DOWN_LEFT), (DOWN_RIGHT)]:
		# store position		
			node_position = ( current_node.position[0] + step[0], 
								current_node.position[1] + step[1] )

		# ignore if position is outside the graph
			if node_position[0] < 0 or node_position[0] > WIDTH or \
				node_position[1] < 0 or node_position[1] > HEIGHT:
				print("outside graph detected")
				continue


		# create new node and add to neighbors list
			new_node = Node(current_node, node_position)
			neighbors.append(new_node)
			print("Current neighbors: ")
			for neighbor in neighbors:
				
				# remove if position is obstacle
				for obstacle in obstacles:
					if obstacle.collidepoint(neighbor.position):
						print("\n\nobstacle detected at ", node_position)
						neighbors.remove(neighbor)
						

		# first neighbor defaults to best
		best_neighbor = Node(None, neighbors[0].position)
		best_neighbor.h_score = distance_to_goal(best_neighbor.position, goal)

		# select best neighbor
		for neighbor in neighbors:
			neighbor.h_score = distance_to_goal(neighbor.position, goal)
			if neighbor.h_score < best_neighbor.h_score:
				best_neighbor = neighbor
			print(neighbor.h_score, neighbor.position)

		# if neighbor > current .. update current and add to visited
		if best_neighbor.h_score < current_node.h_score:
			current_node = best_neighbor
			visited_nodes.append(current_node.position)


		# else if neighbor <= current ... return current
		elif best_neighbor.h_score >= current_node.h_score:
			print(best_neighbor.h_score, current_node.h_score)
			return visited_nodes


# function to get the h_score
def distance_to_goal(position, goal):
	pos_x = position[0] 
	pos_y = position[1] 

	goal_x = goal[0]
	goal_y = goal[1]

	distance = ( (goal_x - pos_x)**2 ) + ( (goal_y - pos_y)**2 )
	return math.sqrt(distance)

def hill_climbing_k(graph, start, goal, obstacles):
	# initialize start as current_node
	current_node = Node(None, start)
	current_node.h_score = distance_to_goal(current_node.position, goal)
	print("Starting H_SCORE: " + str(current_node.h_score))
	k = 2

	# keep track of visited nodes for visualization
	visited_nodes = []
	visited_nodes.append(current_node.position)

	searching = True
	while searching:
		# check if goal is reached
		if current_node.h_score == 0:
			return visited_nodes

		# get list of valid neighbors
		neighbors = []
		for step in [
					tuple(k * np.array(LEFT)), tuple(k * np.array(RIGHT)), 
					tuple(k * np.array(UP)), tuple(k * np.array(DOWN)), 
					tuple(k * np.array(UP_LEFT)), tuple(k * np.array(UP_RIGHT)), 
					tuple(k * np.array(DOWN_LEFT)), tuple(k * np.array(DOWN_RIGHT))
					]:
		# store position		
			node_position = ( current_node.position[0] + step[0], 
								current_node.position[1] + step[1] )

		# create new node and add to neighbors list
			new_node = Node(current_node, node_position)
			neighbors.append(new_node)
			print("Current neighbors: ")
			for neighbor in neighbors:
				
				# remove if position is obstacle
				for obstacle in obstacles:
					if obstacle.collidepoint(neighbor.position):
						try:
							neighbors.remove(neighbor)
						except ValueError:
							print("caught error and dipped at: ", neighbor.position, neighbor)
							#return visited_nodes
						
				# remove if position is outside the graph
				# if neighbor.position[0] < 0 or neighbor.position[0] > WIDTH or \
				# 	neighbor.position[1] < 0 or neighbor.position[1] > HEIGHT:
				# 	print("outside graph detected")
				# 	neighbors.remove(neighbor)
		# first neighbor defaults to best
		best_neighbor = Node(None, neighbors[0].position)
		best_neighbor.h_score = distance_to_goal(best_neighbor.position, goal)

		# select best neighbor
		for neighbor in neighbors:
			neighbor.h_score = distance_to_goal(neighbor.position, goal)
			if neighbor.h_score < best_neighbor.h_score:
				best_neighbor = neighbor
			print(neighbor.h_score, neighbor.position)

		# if neighbor > current .. update current and add to visited
		if best_neighbor.h_score < current_node.h_score:
			current_node = best_neighbor
			visited_nodes.append(current_node.position)


		# else if neighbor <= current ... return current
		elif best_neighbor.h_score >= current_node.h_score:
			print(best_neighbor.h_score, current_node.h_score)
			return visited_nodes

# need a function to return a list of tuples generated by a scalar
# operation on the directions


# def depth_k_search(k_value, start, goal):

# 	neighbor_tuples = [(LEFT), (RIGHT), (UP), (DOWN), (UP_LEFT), 
# 						(UP_RIGHT), (DOWN_LEFT), (DOWN_RIGHT)]

# 	for k in range(2, k_value + 1):











