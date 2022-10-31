

class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (230, 230, 230)
    # ship settings
        self.shipImage_path = 'images/ship.bmp'
        self.ship_speed = 1.5
    # bullet settings
        self.bullet_width = 3
        self.bullet_speed = 1
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
    # alien
        self.alienImage_path = 'images/alien.bmp'
        self.alien_speed = 1.0
        self.fleet_drop_speed = 1.0
    # fleet direction = 1 means right, 0 means down
        self.fleet_direction = 1


