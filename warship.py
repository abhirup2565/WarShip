import sys
import pygame

from settings import Settings
from ship import Ship

class Warship:
    """overall class to manage game assests and behavior"""

    def __init__(self):
        """initialize the game and create resource"""
        pygame.init()
        self.Setting=Settings()
        self.bg_color=self.Setting.bg_color
        self.clock=pygame.time.Clock()

        self.screen=pygame.display.set_mode((self.Setting.screen_width,self.Setting.screen_height))
        pygame.display.set_caption("Warship")
        self.ship=Ship(self)

    def _check_events(self):
        """response to event"""
        while True:
            #watch for keyboard and mouse movement
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        #make recently drawn screen visible
        pygame.display.flip()

    def run_game(self):
        """Start main loop for the game """
        self._check_events()
        self._update_screen()
        self.clock.tick(60)


if __name__=="__main__":
    ai=Warship()
    ai.run_game()
