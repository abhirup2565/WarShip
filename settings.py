class Settings:
    def __init__(self):
        """static settings"""
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        #Bullet settings
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullet_allowed=3
        #Ship Settings
        self.ship_limit=3
        #Alien settings
        self.fleet_drop_speed =10
        #dynamic settings
        self.score_scale=1.5
        self.speedup_scale=1.1
        self.initialize_dynamic_settings()
        #Scoring settings
        self.alien_points=50
        
    def initialize_dynamic_settings(self):
        #Initialse dynamic settings
        self.bullet_speed=2.5
        self.ship_speed = 1.5
        self.alien_speed = 1.0
        #fleet direction 1 represent right and -1 represent left
        self.fleet_direction=1

    def increase_speed(self):
        """increase speed settings"""
        self.ship_speed*=self.speedup_scale
        self.bullet_speed*=self.speedup_scale
        self.alien_speed*=self.speedup_scale
        self.alien_points=int(self.alien_points*self.score_scale)