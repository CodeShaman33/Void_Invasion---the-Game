

class Stats:

    def __init__(self, game):
        self.game_active = False
        self.settings = game.settings
        self.reset_stats()

    # stats
        self.ship_health = 10

    def reset_stats(self):
        self.ships_left = self.settings.ships_limit
        self.score = 0