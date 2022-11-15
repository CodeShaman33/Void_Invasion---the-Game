import pygame

class PowerBar:

    def __init__(self, game, color=(100, 0, 255)):

        self.game = game
        self.settings = self.game.settings
        self.color = color



    def draw_bar(self, ship):

        pygame.draw.rect(self.game.screen, (self.color), (self.game.ship.rect.x, self.game.ship.rect.y + 30, 50, 10))

    def update_bar(self):
        pass
