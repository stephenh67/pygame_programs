import pygame


class Settings:
    """ A class to store blackjack settings """

    def __init__(self):
        """ Initialize the game's static settings. """
        self.screen_width = 1200
        self.screen_height = 700
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.bg_color = (22, 84, 8)
