import sys
import pygame

from settings import Settings

class Warship:
    """overall class to manage game assests and behavior"""

    def __init__(self):
        """initialize the game and create resource"""
        pygame.init()
        self.Setting=Settings()
        self.clock=pygame.time.Clock()

        self.screen=pygame.display.set_mode((self.Setting.screen_width,self.Setting.screen_height))
        pygame.display.set_caption("Warship")
        self.bg_color=self.Setting.bg_color

    def run_game(self):
        """Start main loop for the game """
        while True:
            #watch for keyboard and mouse movement
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            #make recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)

if __name__=="__main__":
    ai=Warship()
    ai.run_game()
