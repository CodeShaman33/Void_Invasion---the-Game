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
    # geomery of the bullet
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)
    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class BulletHorizontal(Sprite):

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = Settings()
        self.color = self.settings.horizontal_bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.horizontal_bullet_width,
                                self.settings.horizontal_bullet_height)

        self.rect2 = pygame.Rect(0, 0, self.settings.horizontal_bullet_width,
                                self.settings.horizontal_bullet_height)


        self.rect.midtop = game.ship.rect.midtop
        self.rect2.midtop = game.ship.rect.midtop


        self.x = float(self.rect.x)
        self.x2 = float(self.rect2.x)


    def update(self):
        self.x -= self.settings.bullet_speed
        self.rect.x = self.x

        self.x2 += self.settings.bullet_speed
        self.rect2.x = self.x2




    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect2)

