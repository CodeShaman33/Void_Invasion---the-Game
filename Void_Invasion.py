import sys
import pygame
from settings import Settings

class VoidInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Invasion from the Void')

    def run_game(self):
        #starting gameplay loop
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

        pygame.display.flip()










if __name__ == '__main__':
    #create instance of game model and run it
    ai = VoidInvasion()
    ai.run_game()
