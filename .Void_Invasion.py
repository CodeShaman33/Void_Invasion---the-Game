import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet, BulletHorizontal
from alien import ALien
from button import Button
from stats import Stats
import time
from score_board import Scoreboard
from functions import Functions


class VoidInvasion:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Invasion from the Void')
        self.ship = Ship(self)
    # sprites
        self.bullets = pygame.sprite.Group()
        self.bullets_horizontal = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
    # sounds
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.collision_sound = pygame.mixer.Sound(self.settings.collision_sound)
        #self.create_fleet()
    #buttons
        self.buttons = []
        self.play_button = Button(self, 'Play', self.settings.position['play'])
        self.buttons.append(self.play_button)
        self.quit_button = Button(self, 'Quit',self.settings.position['quit'])
        self.buttons.append(self.quit_button)
        self.diff_button = Button(self, 'Change Difficulty', self.settings.position['change diff'])
        self.buttons.append(self.diff_button)
        self.diff_status = Button(self, str(self.settings.difficulty_levels[self.settings.difficulty_var]), self.settings.position['diff_status'])
        self.buttons.append(self.diff_status)
        self.functions = Functions(self)

    # additional variables
        self.var = False
    # FPS
        self.FPS = self.settings.FPS
        self.FPS_clock = pygame.time.Clock()
    # stats
        self.stats = Stats(self)
    # scoreboard
        self.sb = Scoreboard(self)
        self.score = self.stats.score
        self.functions = Functions(self)


    def run_game(self):
        self.play_button.draw_button()
        #starting gameplay loop
        while True:
            self.functions.check_events()
            if self.stats.game_active:
                self.ship.update()
                self.bullets.update()
                self.bullets_horizontal.update()
                self._update_aliens()
                self.functions._update_bullets()
                self.functions.check_colissions()
                self.check_ship()
            self.functions.update_screen()
            self.FPS_clock.tick(self.FPS)






















    def _update_aliens(self):

        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        if self.settings.fleet_direction == 1:
            self.settings.fleet_direction = 0
        elif self.settings.fleet_direction == 0:
            self.settings.fleet_direction = 1



    def check_ship(self):
        if self.settings.ship_collision >= 3:
            print('koniec gry')












if __name__ == '__main__':
    #create instance of game model and run it
    ai = VoidInvasion()
    ai.run_game()
