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
                self.check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.game._check_buttons(mouse_pos)


    def  check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()

        if event.key == pygame.K_RIGHT:
            self.game.ship.moving_right = True

        if event.key == pygame.K_LEFT:
            self.game.ship.moving_left = True

        if event.key == pygame.K_SPACE:
            self.game._fire_bullet()

        if event.key == pygame.K_r:
            self.game.fire_bullet_horizontal()

        if event.key == pygame.K_UP:
            self.game.ship.moving_up = True

        if event.key == pygame.K_DOWN:
            self.game.ship.moving_down = True

    # key for quit the game
        if event.key == pygame.K_q:
            sys.exit()


    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.game.ship.moving_right = False

        if event.key == pygame.K_LEFT:
            self.game.ship.moving_left = False

        if event.key == pygame.K_UP:
            self.game.ship.moving_up = False

        if event.key == pygame.K_DOWN:
            self.game.ship.moving_down = False
