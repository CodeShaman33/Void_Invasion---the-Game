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
        alien = ALien(self.game)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.game.aliens.add(alien)

    def change_difficulty(self):
        if self.game.settings.difficulty_var == 1:
            self.game.settings.difficulty_var += 1

        elif self.game.settings.difficulty_var == 2:
            self.game.settings.difficulty_var += 1

        elif self.game.settings.difficulty_var == 3:
            self.game.settings.difficulty_var = 1

        print(self.game.settings.difficulty_var)

    def prepare_new(self):
        self.game.aliens.empty()
        self.game.bullets.empty()

        self.game.functions.create_fleet()
        self.game.ship.center_ship()

    def _check_buttons(self, mouse_pos):
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
        self.game.screen.fill(self.settings.background_color)
        self.game.ship.blitme()
        for bullet in self.game.bullets.sprites():
            if self.game.var:
                bullet.var = True
            else:
                bullet.var = False
            bullet.draw_bullet()

        for bullet in self.game.bullets_horizontal.sprites():
            if self.game.var:
                bullet.var = True
            else:
                bullet.var = False
            bullet.draw_bullet()

        for bullet in self.game.alien_bullets.sprites():
            bullet.draw_bullet()

        self.game.aliens.draw(self.game.screen)
        self.game.sb.show_score()
    # display menu if game isnt active
        if not self.game.stats.game_active:
            for button in self.game.buttons:
                if button == self.game.diff_status:
                    button._msg(self.settings.difficulty_levels[self.settings.difficulty_var])
                button.draw_button()
    # health bar
        self.draw_bar()
        pygame.display.flip()

    def ship_hit(self):
        if self.game.stats.ships_left > 0:
            self.game.stats.ships_left -= 1
            time.sleep(0.5)
        else:
            pygame.mouse.set_visible(True)
            self.game.stats.game_active=False
            self.prepare_new()

    def check_colissions(self):
        colissions = pygame.sprite.groupcollide(self.game.bullets, self.game.aliens, True, True)
        colissions2 = pygame.sprite.groupcollide(self.game.bullets_horizontal, self.game.aliens, True, True)
        if colissions or colissions2:
            self.game.stats.score += self.game.settings.alien_points
        # sounds
            pygame.mixer.Sound.play(self.game.collision_sound)
            pygame.mixer.music.stop()


        self.game.sb.prep_score()

        if pygame.sprite.spritecollideany(self.game.ship, self.game.aliens):
            self.ship_hit()
            if self.game.stats.ship_health > 0:
                self.game.stats.ship_health -= 1
            else:
                self.game.ship.visible = False
            self.game.stats.score += self.settings.alien_points

    def _check_aliens_bottom(self):
        screen_rect = self.game.screen.get_rect()
        for alien in self.game.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.ship_hit()
                break

    def _fire_bullet(self):
        new_bullet = Bullet(self.game)
        self.game.bullets.add(new_bullet)
        pygame.mixer.Sound.play(self.game.laser_sound)
        pygame.mixer.music.stop()

    def fire_bullet_horizontal(self):

        new_bullet = BulletHorizontal(self.game, 0)
        new_bullet2 = BulletHorizontal(self.game, 1)
        self.game.bullets_horizontal.add(new_bullet)
        self.game.bullets_horizontal.add(new_bullet2)

    def _update_bullets(self):
        if not self.game.aliens:
            self.game.bullets.empty()
            self.game.functions.create_fleet()

    def fleet_down(self):
        for alien in self.game.aliens.sprites():
            alien.rect.y += 30

    def alien_shot(self):
        temp_var = random.randint(1, 4000)
        if temp_var % 2 == 0 and temp_var in [(x + 20) for x in range(30)]:
            shooting_alien = random.choice(self.game.aliens.sprites())
            alien_bullet = AlienBullet(self.game, shooting_alien)
            self.game.alien_bullets.add(alien_bullet)

    def draw_bar(self):

# actual life level
        health_level = self.game.stats.ship_health * 6
# red background
        pygame.draw.rect(self.game.screen, (255, 0, 0), pygame.Rect(self.game.ship.rect.x, self.game.ship.rect.y + 50, 60, 10))
# green life indicator
        pygame.draw.rect(self.game.screen, (0, 255, 0), pygame.Rect(self.game.ship.rect.x, self.game.ship.rect.y + 50, self.game.stats.ship_health * 6, 10))

        print(health_level)


    def _update_aliens(self):
        self._check_fleet_edges()
        self.game.aliens.update()

    def _check_fleet_edges(self):
        for alien in self.game.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                self.fleet_down()
                break


    def _change_fleet_direction(self):
        if self.settings.fleet_direction == 1:
            self.settings.fleet_direction = 0
        elif self.settings.fleet_direction == 0:
            self.settings.fleet_direction = 1

    def check_ship(self):
        if self.settings.ship_collision >= 3:
            print('koniec gry')







