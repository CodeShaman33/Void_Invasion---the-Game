import pygame

class Bar:
    '''basic class for game bars, which is automaticaly used for health bar'''
    def __init__(self, game, color=(0,255,0)):

        self.game = game
        self.settings = self.game.settings
        self.color = color


    def draw_bar(self, ship):

        pygame.draw.rect(self.game.screen, (self.color), (self.game.ship.rect.x, self.game.ship.rect.y + 30, 50, 10))

    def update_bar(self):
        pass


class PowerBar(Bar):
    '''This class is similar to health_bar class so it inherits most of its atributtes'''
    def __init__(self, game, color=(100, 0, 255)):

        Bar.__init__(self, game)
        self.color = color



    def draw_bar(self, ship):

        pygame.draw.rect(self.game.screen, (self.color), (self.game.ship.rect.x, self.game.ship.rect.y + 30, 50, 10))

    def update_bar(self):
        pass



