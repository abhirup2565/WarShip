import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent single alien in fleet"""

    def __init__(self,ai_game):
        """initialize alien and set its starting point"""
        super().__init__()
        self.screen=ai_game.screen

        #loading alien image
        self.image=pygame.image.load('images/alien.bmp')
        self.rect= self.image.get_rect()

        #start new alien from top left
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        #store aliens exact horizontal postion
        self.x=float(self.rect.x)