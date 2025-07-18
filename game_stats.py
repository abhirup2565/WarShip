class GameStats:
    def __init__(self,ai_game):
        """initialise stats"""
        self.settings=ai_game.Setting 
        self.reset_stats()

    def reset_stats(self):
        """initializing stats to change ship in game"""
        self.ship_left=self.settings.ship_limit
        self.score=0