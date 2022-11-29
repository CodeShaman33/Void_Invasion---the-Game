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
from bars import Bar
from bars import PowerBar

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
        self.alien_bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
    # sounds
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.collision_sound = pygame.mixer.Sound(self.settings.collision_sound)
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
        self.ship_health = Bar(self)
        self.power_bar = PowerBar(self)
    # scoreboard
        self.sb = Scoreboard(self)
        self.score = self.stats.score
    # in separate  .py file
        self.functions = Functions(self)


    def run_game(self):

        while True:
            self.functions.check_events()
            if self.stats.game_active:
                self.ship.update()
                self.functions.alien_shot()
                self.bullets.update()
                self.bullets_horizontal.update()
                self.alien_bullets.update()
                self.functions._update_aliens()
                self.functions._update_bullets()
                self.functions.check_colissions()
                self.ship_health.draw_bar(self.ship)

            self.functions.update_screen()
            self.FPS_clock.tick(self.FPS)





if __name__ == '__main__':
#create instance of game model and run it
    ai = VoidInvasion()
    ai.run_game()
