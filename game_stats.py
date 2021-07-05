import json
class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings= ai_game.settings
        self.reset_stats()

        #Start Alien Invasion in an active state
        self.game_active = False

        #High score should never be reset
        self.high_score=0
        self.search_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score =0
        self.level=1

    def save_high_score(self):
        """Saves high score to a file"""
        with open("Alien_Invasion/stats/high_score.json",'w') as f:
            json.dump(self.high_score,f)

    def search_high_score(self):
        """Gets high score from file"""
        try:
            with open("Alien_Invasion/stats/high_score.json") as f:
                number=json.load(f)
        except FileNotFoundError:
            self.high_score=0
            print("Not")
        else:
            self.high_score=number
            print(number)
            print(self.high_score)
        