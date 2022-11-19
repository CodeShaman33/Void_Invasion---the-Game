import pygame
from health_bar import Bar

class PowerBar(Bar):

    def __init__(self, game, color=(100, 0, 255)):

        Bar.__init__(self, game)
        self.color = color



    def draw_bar(self, ship):

        pygame.draw.rect(self.game.screen, (self.color), (self.game.ship.rect.x, self.game.ship.rect.y + 30, 50, 10))

    def update_bar(self):
        pass


