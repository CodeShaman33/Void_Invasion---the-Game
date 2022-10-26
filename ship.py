import pygame
from settings import Settings

class Ship:

    def __init__(self, game):
        self.settings = Settings()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    # load image of the ship

        self.image = pygame.image.load(self.settings.shipImage_path)
        self.rect = self.image.get_rect()

    #every new user ship starts at the bottom of the screen

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)


