import pygame
from settings import Settings

class Ship:

    def __init__(self, game):
    # basic settings
        self.settings = Settings()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

    # load image of the ship
        self.image = pygame.image.load(self.settings.shipImage_path)
        self.rect = self.image.get_rect()

    #every new user ship starts at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    # ship orientation settings
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    # movement basic variables
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed

        if self.moving_down:
            if self.rect.bottom <= self.screen_rect.bottom:
                self.y += self.settings.ship_speed

    # upating ship orientation in space
        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

