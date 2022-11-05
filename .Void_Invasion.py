import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet, BulletHorizontal
from alien import ALien
from button import Button
from stats import Stats
import time


class VoidInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Invasion from the Void')
        self.ship = Ship(self)
    # sprites
        self.bullets = pygame.sprite.Group()
        self.bullets_horizontal = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.create_fleet()
    #buttons
        self.play_button = Button(self, 'Gra')

    # additional variables
        self.var = False
    # FPS
        self.FPS = self.settings.FPS
        self.FPS_clock = pygame.time.Clock()
    #stats
        self.stats = Stats(self)

    def run_game(self):
        self.play_button.draw_button()
        #starting gameplay loop
        while True:

            self.check_events()
            if self.stats.game_active:
                self.ship.update()
                self.bullets.update()
                self.bullets_horizontal.update()
                self._update_aliens()
                self._update_bullets()
                self.check_colissions()
                self._update_bullets()
                self.check_ship()
            self.update_screen()
            self.FPS_clock.tick(self.FPS)




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
                self._check_play_button(mouse_pos)

    def  check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        if event.key == pygame.K_SPACE:
            self._fire_bullet()

        if event.key == pygame.K_r:
            self.fire_bullet_horizontal()

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
            if self.var:
                bullet.var = True
            else:
                bullet.var = False
            bullet.draw_bullet()

        for bullet in self.bullets_horizontal.sprites():
            if self.var:
                bullet.var = True
            else:
                bullet.var = False
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
    # play button
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


    def fire_bullet_horizontal(self):
        new_bullet = BulletHorizontal(self, 0)
        new_bullet2 = BulletHorizontal(self, 1)
        self.bullets_horizontal.add(new_bullet)
        self.bullets_horizontal.add(new_bullet2)




    def create_fleet(self):
        alien = ALien(self)
        self.aliens.add(alien)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = available_space_x // (2 * alien_width)

    #checking how many rows of aliens fit to the screen

        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

    # create full fleet of aliens

        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = ALien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):

        self._check_fleet_edges()
        if self.settings.fleet_direction == 1:
            self.aliens.update()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= 0

    def _update_bullets(self):
        if not self.aliens:
            self.bullets.empty()
            self.create_fleet()

    def check_ship(self):
        if self.settings.ship_collision >= 3:
            print('koniec gry')

    def check_colissions(self):
        colissions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        colissions2 = pygame.sprite.groupcollide(self.bullets_horizontal, self.aliens, True, True)
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_hit()

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.ship_hit()
                break

    def ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            time.sleep(0.5)
        else:
            self.stats.game_active=False
            self.prepare_new()

    def _check_play_button(self, mouse_pos):

    #local variable
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:

            self.stats.reset_stats()
            self.stats.game_active = True

            self.prepare_new()

    def prepare_new(self):
        self.aliens.empty()
        self.bullets.empty()

        self.create_fleet()
        self.ship.center_ship()









if __name__ == '__main__':
    #create instance of game model and run it
    ai = VoidInvasion()
    ai.run_game()
