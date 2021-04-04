#!/usr/bin/python
import math as math
import heapq as heapq
import pygame as pygame
import sys
from a_star import a_star_legacy, a_star
from environment import Environment
from hill_climb import hill_climbing, hill_climbing_k
from potential_cost_search import testing_heap, potential_cost_search, define_obstacle_points




def main():
	# build environment with polygonal obstacles
	start_one = ( (10,10) )
	end_one = ( (790, 390) )
	environment_one = Environment(start_one, end_one)
	environment_one.build_graph()
	environment_one.build_obstacles_one()

	# build second environment
	start_two = ( (10, 10) )
	end_two = ( (400, 150)  )
	environment_two = Environment(start_two, end_two)
	environment_two.build_graph()
	environment_two.build_obstacles_two()

	# default constraint
	constraint = 10000


	# execute a_star search function on the environment
	# path = a_star_legacy(environment.graph, environment.start, 
	#				environment.end, environment.obstacles)
	
	#path = hill_climbing(environment.graph, environment.start, 
	# 				environment.goal, environment.obstacles)

	# path = potential_cost_search(environment.graph, environment.start, 
	#  				environment.goal, environment.obstacles, 30)
	
	# # display results
	# print(path)
	# path = define_obstacle_points(environment.graph, environment.obstacles) # isn't working as hoped
	
	# environment.show_path(path)
	
	active_env = environment_two
	
	# setup for taking input 
	font = pygame.font.Font(None, 32)
	color_inactive = pygame.Color('lightskyblue3')
	color_active = pygame.Color('dodgerblue2')
	color = color_inactive
	taking_input = False
	input_string = ''


	# primary game loop
	running = True
	while running:
		for event in pygame.event.get():
			
	    	# exit correctly
			if event.type == pygame.QUIT:
				running = False
				pygame.quit()
				sys.exit()
	        
	        # check for mouse click
			elif event.type == pygame.MOUSEBUTTONDOWN:
				active_env.instruction_text = "Enter an Integer value for a constraint!"
				active_env.build_instruction_box()
				# click button_one
				if active_env.search_button_one.collidepoint(event.pos):					
					active_env = environment_one
					active_env.reset_display_one()
					pygame.display.flip()


				
				# click button_two	
				elif active_env.search_button_two.collidepoint(event.pos):
					active_env = environment_two
					active_env.reset_display_two()
					pygame.display.flip()


				
				# click input_box
				elif active_env.input_box.collidepoint(event.pos):
					taking_input = True
					
				# clicking anywhere else
				else:
					taking_input = False

				color = color_active if taking_input else color_inactive
				
			# check for keyboard input
			if event.type == pygame.KEYDOWN:
				if taking_input:
					# ENTER stores input as int and runs the search 
					if event.key == pygame.K_RETURN:
						print("Constraint Input: " + input_string)

						# ignore if invalid input
						try:
							constraint = int(input_string)
							ignore = False
						except ValueError as e:
							ignore = True
							pass
						input_string = ''
						
						if not ignore:
							#path = hill_climbing(active_env.graph, active_env.start, active_env.end, active_env.obstacles)
							path = potential_cost_search(active_env.graph, active_env.start, active_env.end, 
								active_env.obstacles, constraint, active_env.screen)
							#path = a_star(active_env.graph, active_env.start, active_env.end, active_env.screen)
							if path == "impossible":
								active_env.instruction_text = "No path within constraint!"
								active_env.update_instruction_box()								
							else:
								active_env.show_path(path)


					# BACKSPACE deletes last character
					elif event.key == pygame.K_BACKSPACE:
						input_string = input_string[:-1]
					else:
						input_string += event.unicode
		
		# blank input_box
		active_env.screen.fill((66, 66, 66), active_env.input_box)
		# render display of text
		text_surface = font.render(input_string, True, color)
		width = max(active_env.input_box.w, text_surface.get_width()+10)
		active_env.input_box.w = width
		active_env.screen.blit(text_surface, (active_env.input_box.x+5, active_env.input_box.y+5))
		
		# redraw input_box
		pygame.draw.rect(active_env.screen, color, active_env.input_box, 2)	
		
		pygame.display.update()


	#call main function
if __name__ == "__main__":
	pygame.init()
	pygame.font.init()
	main()
	
