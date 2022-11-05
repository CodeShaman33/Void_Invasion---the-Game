import pygame
import sys

class Functions:

    def __init__(self, game):
        self.game = game
        self.settings = game.settings



    def check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self.game.check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self.game.check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.game._check_buttons(mouse_pos)

