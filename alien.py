import pygame
from pygame.sprite import Sprite
from settings import Settings

class ALien(Sprite):

    def __init__(self, game):
        super().__init__()

        self.screen = game.screen
        self.settings = Settings()
    # image of the alien
        self.image = pygame.image.load(self.settings.alienImage_path)
        self.rect = self.image.get_rect()
    # first coordinated of the alien instance
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    # storing specific location of the alienWR
        self.x = float(self.rect.x)
    # local fleet direction indicator
        self.fleet_down = False

    def update(self):
        if not self.fleet_down:
            self.x += (self.settings.alien_speed * self.settings.fleet_direction)
            self.rect.x = self.x


# function belows check if the alien fleet reaches the right border of the screen

    def check_edges(self):
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            self.fleet_down = True
            return True



