class Settings():
    """A class to store all settings in alien invasion"""

    def __init__(self):
        """Initialize game's settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #Ship settings
        self.ship_limit = 3

        #Bullet settings
        #change width to 3 once game is complete 
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #Aliens settings
        self.fleet_drop_speed = 10

        #How quickly the game speeds up.
        self.speedup_scale = 1.1

        self.intialize_dynamic_settings()

    def intialize_dynamic_settings(self):
        """ Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

