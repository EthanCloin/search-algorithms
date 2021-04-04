import pygame as pg


class Settings:
    """Use this object to share constant values and any
    other conveniences"""
    # Display Settings
    environment_one_color = pg.Color("Red")
    environment_two_color = pg.Color("Green")

    def __init__(self):
        print("I live")
