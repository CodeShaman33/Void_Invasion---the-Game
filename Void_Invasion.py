import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class VoidInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Invasion from the Void')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        #starting gameplay loop
        while True:
            self.check_events()
            self.ship.update()
            self.bullets.update()
            self.update_screen()




    def check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def  check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        if event.key == pygame.K_SPACE:
            self._fire_bullet()

        if event.key == pygame.K_UP:
            self.ship.moving_up = True

        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True

    # key for quit the game
        if event.key == pygame.K_q:
            sys.exit()

    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

        if event.key == pygame.K_UP:
            self.ship.moving_up = False

        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False



    def update_screen(self):
        self.screen.fill(self.settings.background_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)









if __name__ == '__main__':
    #create instance of game model and run it
    ai = VoidInvasion()
    ai.run_game()
