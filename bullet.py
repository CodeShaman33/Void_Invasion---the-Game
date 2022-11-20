import pygame
from pygame.sprite import Sprite
from settings import Settings

'''
In this module are classes used to create all kind of bullets existing in game.
Player ship can fire normal straight bullet with every space hit,
when power bar are full there player can fire special horizontal bullets'''

class Bullet(Sprite):

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = Settings()
        self.color = self.settings.bullet_color
    # geomery of the bullet
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop
    # set as float to have more control of the location
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class BulletHorizontal(Sprite):

    def __init__(self, game, temp_var):
        super().__init__()
        self.screen = game.screen
        self.settings = Settings()
        self.temp_var = temp_var
        self.color = self.settings.horizontal_bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.horizontal_bullet_width,
                                self.settings.horizontal_bullet_height)
        self.rect.midtop = game.ship.rect.midtop
        self.x = float(self.rect.x)


    def update(self):
        '''horizontal bullets are fired in both ways at the same time,
        temp_var is used to be able update both bullets'''
        if self.temp_var == 0:
            self.x -= self.settings.bullet_speed
            self.rect.x = self.x

        elif self.temp_var == 1:
            self.x += self.settings.bullet_speed
            self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class AlienBullet(Sprite):

    def __init__(self, game, alien):
        super().__init__()
        self.screen = game.screen
        self.settings = Settings()
        self.alien = alien
        self.color = self.settings.alien_bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = self.alien.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.alien_bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)