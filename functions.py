'''All main functions are in this particular module so the main file is easier to read'''

import random
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet, BulletHorizontal, AlienBullet
from alien import ALien
from button import Button
from stats import Stats
import time
from score_board import Scoreboard


class Functions:

    def __init__(self, game):
        self.game = game
        self.settings = game.settings



    def check_events(self):
        '''function constantly checking whether the pleyer pressed something or not'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_buttons(mouse_pos)


    def  check_keydown_events(self, event):

        if event.key == pygame.K_q:
            sys.exit()

        if event.key == pygame.K_RIGHT:
            self.game.ship.moving_right = True

        if event.key == pygame.K_LEFT:
            self.game.ship.moving_left = True

        if event.key == pygame.K_SPACE:
            self._fire_bullet()

        if event.key == pygame.K_r:
            self.fire_bullet_horizontal()

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

    def create_fleet(self):
        '''this function at first calculate available space at the screen according to resolution set,
         then it creates equal rows of alien sprites'''
        alien = ALien(self.game)
        self.game.aliens.add(alien)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.game.settings.screen_width - (2 * alien_width)
        number_alien_x = available_space_x // (2 * alien_width)

        # checking how many rows of aliens fit to the screen

        ship_height = self.game.ship.rect.height
        available_space_y = (self.game.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # create full fleet of aliens

        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        '''This function create alien and set its size due to the specific parameters of the screen'''
        alien = ALien(self.game)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.game.aliens.add(alien)

    def change_difficulty(self):
        '''Player can change the difficulty at the beginning, in starting menu with one of the creted buttons,
        difficulty level will have influence on such parameters like alien speed and the number of bullets the alien fleet can shot'''
        if self.game.settings.difficulty_var == 1:
            self.game.settings.difficulty_var += 1

        elif self.game.settings.difficulty_var == 2:
            self.game.settings.difficulty_var += 1

        elif self.game.settings.difficulty_var == 3:
            self.game.settings.difficulty_var = 1

        self.set_params(self.game.settings.difficulty_var)
        print(self.game.settings.difficulty_var)

    def prepare_new(self):
        '''this function prepare new game'''
        self.game.stats.reset_stats()
        self.game.aliens.empty()
        self.game.bullets.empty()
        self.game.functions.create_fleet()
        self.game.ship.center_ship()

    def _check_buttons(self, mouse_pos):
        '''This functions activate response on every buttons in main game menu'''
        play_button_clicked = self.game.play_button.rect.collidepoint(mouse_pos)
        quit_button_clicked = self.game.quit_button.rect.collidepoint(mouse_pos)
        diff_button_clicked = self.game.diff_button.rect.collidepoint(mouse_pos)

        if play_button_clicked and not self.game.stats.game_active:

            self.game.stats.reset_stats()
            self.game.stats.game_active = True
            pygame.mouse.set_visible(False)
            self.game.functions.prepare_new()

        elif quit_button_clicked:
            sys.exit()

        elif diff_button_clicked:
            self.change_difficulty()

        self.update_screen()

    def update_screen(self):
        '''this function update and display all elements of the screen,
        some elements like the buttons are visible when game isnt active yet'''

        self.game.screen.fill(self.settings.background_color)

        if self.game.stats.game_active:
            self.game.ship.blitme()
            self._update_bullets()
            self.game.aliens.draw(self.game.screen)
            # health bar
            self.draw_bar()
            self.game.sb.show_score()

    # display menu if game isnt active
        if not self.game.stats.game_active:
            for button in self.game.buttons:
                if button == self.game.diff_status:
                    button._msg(self.settings.difficulty_levels[self.settings.difficulty_var])
                button.draw_button()

        pygame.display.flip()

    def ship_hit(self):
        '''This function reduces the health level of the ship with every collision
        '''
        if self.game.stats.ship_health > 0:
            self.game.stats.ship_health -= 1
            time.sleep(0.3)
        else:
            pygame.mouse.set_visible(True)
            self.game.stats.game_active=False
            #self.prepare_new()

    def check_colissions(self):
        colissions = pygame.sprite.groupcollide(self.game.bullets, self.game.aliens, True, True)
        colissions2 = pygame.sprite.groupcollide(self.game.bullets_horizontal, self.game.aliens, True, True)
        if colissions or colissions2:
            self.game.stats.score += self.game.settings.alien_points
        # sounds
            pygame.mixer.Sound.play(self.game.collision_sound)
            pygame.mixer.music.stop()
    # score board
        self.game.sb.prep_score()

    # colissions between plyer ship an alien ships
        if pygame.sprite.spritecollideany(self.game.ship, self.game.aliens):
            self.ship_hit()
            if self.game.stats.ship_health > 0:
                self.game.stats.ship_health -= 1
            else:
                self.game.ship.visible = False
            self.game.stats.score += self.settings.alien_points

    def _check_aliens_bottom(self):
        '''It checks whether any alien reaches the bottom of the screen, if it occurs, the current game will end'''
        screen_rect = self.game.screen.get_rect()
        for alien in self.game.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.the_end()
                break

    def _fire_bullet(self):
        '''every "space" hit creates a new instance of a Bullet class, all the sprites are added to te sprites group'''
        new_bullet = Bullet(self.game)
        self.game.bullets.add(new_bullet)
        pygame.mixer.Sound.play(self.game.laser_sound)
        pygame.mixer.music.stop()

    def fire_bullet_horizontal(self):
        '''It works similar to fire_bullet above, but every time it creates two instances of a bullet instead of one, with
        additional variable which is 0 or 1, thanks to this variable class method that are used to update position of the bullet
        know whether the bullet should fly left or right after shot'''
        new_bullet = BulletHorizontal(self.game, 0)
        new_bullet2 = BulletHorizontal(self.game, 1)
        self.game.bullets_horizontal.add(new_bullet)
        self.game.bullets_horizontal.add(new_bullet2)

    def _update_bullets(self):
        '''This functions iterates after all elements of the sprite groups'''
        for bullet in self.game.bullets.sprites():
            bullet.draw_bullet()

        for bullet in self.game.bullets_horizontal.sprites():
            bullet.draw_bullet()

        for bullet in self.game.alien_bullets.sprites():
            bullet.draw_bullet()

    def fleet_down(self):
        '''Every time the fleet reaches the one of the two sides of the screen
        it also falls down a bit due to the set parameter'''
        for alien in self.game.aliens.sprites():
            alien.rect.y += 30

    def alien_shot(self):
        '''Aliens will shot too. Function is using random module to select random aliens (frequency can be altered with
        the second argument of te function below). every new bullet is added to the group of alien bullets'''
        temp_var = random.randint(1, 4000)
        if temp_var % 2 == 0 and temp_var in [(x + 20) for x in range(30)]:
            shooting_alien = random.choice(self.game.aliens.sprites())
            alien_bullet = AlienBullet(self.game, shooting_alien)
            self.game.alien_bullets.add(alien_bullet)

    def draw_bar(self):
        '''This function draws two bars, one red, one green. Red bar is underneath the green. With every health loss by the ship
        the green bar will get smaller, larger red area will be visible'''
# actual life level
        health_level = self.game.stats.ship_health * 6
# red background
        pygame.draw.rect(self.game.screen, (255, 0, 0), pygame.Rect(self.game.ship.rect.x, self.game.ship.rect.y + 50, 60, 10))
# green life indicator
        pygame.draw.rect(self.game.screen, (0, 255, 0), pygame.Rect(self.game.ship.rect.x, self.game.ship.rect.y + 50, self.game.stats.ship_health * 6, 10))
# power bar background
        pygame.draw.rect(self.game.screen, (255, 0, 255), pygame.Rect(self.game.ship.rect.x, self.game.ship.rect.y + 100, 60, 10))
# power bar indicator
        pygame.draw.rect(self.game.screen, (0, 0, 255), pygame.Rect(self.game.ship.rect.x, self.game.ship.rect.y + 100, 60, 10))

    def _update_aliens(self):
        '''Fristly this function check if the fleet reaches the edge of the screen, then it changes the direction'''
        self._check_fleet_edges()
        self.game.aliens.update()

    def _check_fleet_edges(self):
        for alien in self.game.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                self.fleet_down()
                break


    def _change_fleet_direction(self):
        '''Fleet  current direction is indicated by the variable from settings, this variable will be transfered
        to the stats class in the future'''
        if self.settings.fleet_direction == 1:
            self.settings.fleet_direction = 0
        elif self.settings.fleet_direction == 0:
            self.settings.fleet_direction = 1

    def the_end(self):
        pass

    def set_params(self, difficulty_var):
        pass





