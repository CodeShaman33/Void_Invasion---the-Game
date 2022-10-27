import pygame
from pygame.sprite import Sprite
from settings import Settings

class Bullet(Sprite):

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = Settings()
        self.color = self.settings.bullet_color
    # additional variable using to set course of the bullet
        self.varSide = False
    # geomery of the bullet
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
    def update(self):
        if self.varSide:
            self.y -= self.settings.bullet_speed
            self.rect.y = self.y
        else:
            self.x -= self.settings.bullet_speed
            self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


