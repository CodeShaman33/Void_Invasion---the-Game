

class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.background_color = (230, 230, 230)
        self.FPS = 240
    # ship settings
        self.shipImage_path = 'images/ship.bmp'
        self.ship_speed = 1.5
        self.ships_limit = 3
    # bullet settings
        self.bullet_width = 3
        self.bullet_speed = 1
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
    # horizontal bullet
        self.horizontal_bullet_width = 2
        self.horizontal_bullet_height = 25
        self.horizontal_bullet_color = (255, 0, 20)
    # alien
        self.alienImage_path = 'images/alien.bmp'
        self.alien_speed = 0.1
        self.fleet_drop_speed = 0.1
    # fleet direction = 1 means right, 0 means down
        self.fleet_direction = 1
    # colissions
        self.ship_collision = 0
    # buttons
        self.play_button_pos = (self.screen_width/2, self.screen_height/2)
        self.quit_button_pos = (self.screen_width/2, self.screen_height/2 + 100)
        self.diff_button_pos = (self.screen_width/2, self.screen_height/2 + 200)
        self.diff_status_pos = (self.screen_width/2, self.screen_height/2 - 100)

    # difficulty settings
    # variable in range (1 - 3) where 1 = easy; 2 = medium; 3 = hard
        self.difficulty_var = 2
        self.difficulty_levels = {
            1: 'Easy',
            2: 'Medium',
            3: 'Hard'
        }
    # score and more
        self.alien_points = 50



