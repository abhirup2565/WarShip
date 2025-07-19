import pygame
from pygame.sprite import Sprite 
class Ship(Sprite):
    """class to manage ship"""

    def __init__(self, ai_game):
        super().__init__()
        """initialize ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings=ai_game.Setting
        #load ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #start new ship at bottom center of ship
        self.rect.midbottom=self.screen_rect.midbottom
        #store float for horizontal postion
        self.x=float(self.rect.x)
        #movement flag
        self.moving_right=False
        self.moving_left=False

    def update(self):
        """update ship postion based on flag"""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x-=self.settings.ship_speed
        self.rect.x=self.x

    def blitme(self):
        """draw ship at its current location"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.rect.midbottom=self.screen_rect.midbottom
        self.x = float(self.rect.x)