import pygame as pg
from settings import Settings

# dimensions for screen
WIDTH = 805
HEIGHT = 600

MAP_WIDTH = 800
MAP_HEIGHT = 400

# color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (25, 25, 25)
LIGHT_GREY = (66, 66, 66)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)


def build_screen():
    """Initializes environment screen"""
    background_color = GREY
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption('Polygon Pathfinding')
    screen.fill(background_color)

    border_rect = pg.Rect(0, 0, MAP_WIDTH, MAP_HEIGHT)
    pg.draw.rect(screen, WHITE, border_rect, 5)

    return screen


class Environment:
    """This class represents the Environment, with attributes deciding
    both the visual representation and the operative values for the algorithms"""

    def __init__(self, obstacle_color):
        """Initialize visualization to screen"""
        self.screen = build_screen()
        self.obstacles = None
        self.obstacle_color = obstacle_color
        self.graph = None

        # Initialize travel top left --> bottom right
        self.start = (25, 25)
        self.end = (375, 725)

        # Create components of visualization
        self.input_box = self.build_input_box()
        self.search_button_one = self.build_search_button_one()
        self.search_button_two = self.build_search_button_two()

        self.instruction_text = "Enter an Integer value for a constraint!"
        self.instruction_box = self.build_instruction_box()

    def draw_components(self, color):
        """Draw all visual components of Environment onto its screen"""

        # Obstacles
        if color is Settings.environment_one_color:
            self.build_obstacles_one()
        elif color is Settings.environment_two_color:
            self.build_obstacles_two()

        # Buttons
        pg.draw.rect(self.screen, RED, self.search_button_one, 2)
        pg.draw.rect(self.screen, GREEN, self.search_button_two, 2)

    def build_obstacles_one(self):
        """This function defines obstacles as pg shapes"""
        screen = self.screen

        lower_rectangle = pg.draw.rect(screen, RED, (160, 250, 240, 80), 3)
        upper_rectangle = pg.draw.rect(screen, RED, (480, 25, 90, 160), 3)

        left_tri_pts = ((280, 210), (350, 210), (310, 90))
        left_triangle = pg.draw.polygon(screen, RED, left_tri_pts, 3)
        right_tri_pts = ((410, 190), (430, 290), (480, 240))
        right_triangle = pg.draw.polygon(screen, RED, right_tri_pts, 3)

        left_pentagon_pts = ((130, 120), (140, 200), (210, 215), (280, 120), (220, 40))
        left_pentagon = pg.draw.polygon(screen, RED, left_pentagon_pts, 3)

        mid_quad_pts = ((355, 45), (355, 140), (450, 80), (425, 35))
        mid_quad = pg.draw.polygon(screen, RED, mid_quad_pts, 3)

        right_hexagon_pts = ((580, 220), (620, 250), (620, 330),
                             (570, 350), (520, 320), (520, 250))
        right_hexagon = pg.draw.polygon(screen, RED, right_hexagon_pts, 3)

        right_quad_pts = ((580, 55), (610, 45), (640, 70), (630, 230))
        right_quad = pg.draw.polygon(screen, RED, right_quad_pts, 3)

        shapes = [right_quad, right_hexagon, mid_quad, left_pentagon,
                  right_triangle, left_triangle, upper_rectangle, lower_rectangle]

        self.obstacles = shapes

    def build_graph(self):
        """This function defines a list to hold all points/nodes in the environment"""
        graph = []
        for x in range(0, MAP_WIDTH + 1):
            for y in range(0, MAP_HEIGHT + 1):
                graph.append((x, y))

        self.graph = graph

    def show_path(self, path):
        """Draws lines from list to screen representing the path of nodes
        chosen by the search algorithm"""
        pg.draw.lines(self.screen, BLUE, False, path, 4)

    def set_start(self, start):
        self.start = start

    def set_end(self, end):
        self.end = end

    def build_obstacles_two(self):
        """Construct list of obstacles to be displayed on environment two"""
        screen = self.screen

        circle = pg.draw.circle(screen, GREEN, (190, 290), 95, 3)
        other_circle = pg.draw.circle(screen, GREEN, (300, 100), 80, 3)

        rectangle = pg.draw.rect(screen, GREEN, (600, 130, 190, 100), 3)
        other_rectangle = pg.draw.rect(screen, GREEN, (420, 69, 140, 92), 3)

        triangle = pg.draw.polygon(screen, GREEN, ((50, 70), (70, 190), (190, 90)), 3)
        other_triangle = pg.draw.polygon(screen, GREEN, ((350, 320), (520, 185), (666, 333)), 3)
        obstacles = [circle, other_circle, rectangle, other_rectangle, triangle, other_triangle]

        self.obstacles = obstacles

    def display_start(self):
        """draws a white circle at start position"""
        pg.draw.circle(self.screen, WHITE, self.start, 2)

    def display_end(self):
        """draws a cyan circle at end position"""
        pg.draw.circle(self.screen, CYAN, self.end, 2)

    def clear_screen(self):
        """Clears the visualization part of environment"""
        reset = build_screen()
        self.screen = reset

    def build_input_box(self):
        # build a light grey rect below the MAP
        input_box = pg.Rect(25, MAP_HEIGHT + 50, MAP_WIDTH / 3, HEIGHT - MAP_HEIGHT - 100)
        return input_box

    def build_search_button_one(self):
        search_button = pg.Rect(WIDTH - 200, MAP_HEIGHT + 25, 175, 50)
        return search_button

    def build_search_button_two(self):
        search_button = pg.Rect(WIDTH - 200, MAP_HEIGHT + 125, 175, 50)
        return search_button

    # Probably won't keep instruction_box
    def build_instruction_box(self):
        font = pg.font.Font(None, 20)
        instruction_box = pg.Rect(self.input_box.w + 50, MAP_HEIGHT + self.input_box.h - 25, 175, 50)
        text_surface = font.render(self.instruction_text, True, pg.Color('goldenrod2'))

        width = max(100, text_surface.get_width() + 10)
        instruction_box.w = width
        pg.draw.rect(self.screen, LIGHT_GREY, instruction_box)
        self.screen.blit(text_surface, (instruction_box.x + 5, instruction_box.y + 5))

        return instruction_box

    def update_instruction_box(self):
        self.screen.fill(LIGHT_GREY, self.instruction_box)
        font = pg.font.Font(None, 20)
        instruction_box = pg.Rect(self.input_box.w + 50, MAP_HEIGHT + self.input_box.h - 25, 175, 50)
        text_surface = font.render(self.instruction_text, True, pg.Color('goldenrod2'))

        width = max(100, text_surface.get_width() + 10)
        instruction_box.w = width
        pg.draw.rect(self.screen, LIGHT_GREY, instruction_box)
        self.screen.blit(text_surface, (instruction_box.x + 5, instruction_box.y + 5))

        return instruction_box
