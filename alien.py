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