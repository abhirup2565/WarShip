import sys

import pygame

class Warship:
    """overall class to manage game assests and behavior"""

    def __init__(self):
        """initialize the game and create resource"""
        pygame.init()
        
        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Warship")

    def run_game(self):
        """Start main loop for the game """
        while True:
            #watch for keyboard and mouse movement
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #make recently drawn screen visible
            pygame.display.flip()

if __name__=="__main__":
    ai=Warship()
    ai.run_game()
