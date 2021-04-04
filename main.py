#!/usr/bin/python
import math as math
import heapq as heapq
import pygame as pg
import sys
from a_star import a_star_legacy, a_star
from environment import Environment
from hill_climb import hill_climbing, hill_climbing_k
from potential_cost_search import testing_heap, potential_cost_search, define_obstacle_points
from settings import Settings

"""This script is an expansion on an assignment for Intro to AI 
The goal is to make a more user friendly interface for the visualization
and to organize the code in a more logical, OOP format

Current idea is to allow the user to try and draw the most optimal path, then
display the result from a given algorithm. The user can select which algorithm they compete 
with from the dropdown

Could also turn that into a maze racer. And I can adjust the algorithms speed stat to 
have different levels
"""



def main():
    # initialize settings object
    settings = Settings()
    # build environment with polygonal obstacles
    environment_one = Environment(settings.environment_one_color)
    environment_one.build_graph()
    environment_one.build_obstacles_one()

    # build second environment
    environment_two = Environment(settings.environment_two_color)
    environment_two.build_graph()
    environment_two.build_obstacles_two()

    # Default display second environment
    active_env = environment_two

    # setup for taking input
    # font = pg.font.Font(None, 32)
    # color_inactive = pg.Color('lightskyblue3')
    # color_active = pg.Color('dodgerblue2')
    # color = color_inactive
    # taking_input = False
    # input_string = ''

    # primary game loop
    running = True
    while running:
        for event in pg.event.get():

            # exit correctly
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()

            # check for mouse click
            elif event.type == pg.MOUSEBUTTONDOWN:
                # active_env.instruction_text = "Enter an Integer value for a constraint!"
                # active_env.build_instruction_box()

                # click button_one
                if active_env.search_button_one.collidepoint(event.pos):
                    active_env = environment_one
                    active_env.clear_screen()
                    active_env.draw_components(environment_one.obstacle_color)

                # click button_two
                elif active_env.search_button_two.collidepoint(event.pos):
                    active_env = environment_two
                    active_env.clear_screen()
                    active_env.draw_components(environment_two.obstacle_color)

                # click input_box
                # elif active_env.input_box.collidepoint(event.pos):
                #     taking_input = True

                # clicking anywhere else
                # else:
                #     taking_input = False
                #
                # color = color_active if taking_input else color_inactive

            # check for keyboard input
            if event.type == pg.KEYDOWN:
                print("foo")
                # if taking_input:
                #     # ENTER stores input as int and runs the search
                #     if event.key == pg.K_RETURN:
                #
                #         # ignore if invalid input
                #         try:
                #             constraint = int(input_string)
                #             ignore = False
                #         except ValueError as e:
                #             ignore = True
                #             pass
                #         input_string = ''
                #
                #         if not ignore:
                #             path = a_star(active_env.graph, active_env.start, active_env.end, active_env.screen)
                #             if path == "impossible":
                #                 active_env.instruction_text = "No path within constraint!"
                #                 active_env.update_instruction_box()
                #             else:
                #                 active_env.show_path(path)
                #

                    # BACKSPACE deletes last character
                    # elif event.key == pg.K_BACKSPACE:
                    #     input_string = input_string[:-1]
                    # else:
                    #     input_string += event.unicode

        # blank input_box
        # active_env.screen.fill((66, 66, 66), active_env.input_box)
        # render display of text
        # text_surface = font.render(input_string, True, color)
        # width = max(active_env.input_box.w, text_surface.get_width() + 10)
        # active_env.input_box.w = width
        # active_env.screen.blit(text_surface, (active_env.input_box.x + 5, active_env.input_box.y + 5))

        # redraw input_box
        #pg.draw.rect(active_env.screen, color, active_env.input_box, 2)

        active_env.draw_components(active_env.obstacle_color)
        pg.display.update()


# call main function
if __name__ == "__main__":
    pg.init()
    pg.font.init()
    main()
