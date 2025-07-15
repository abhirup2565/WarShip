import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class Warship:
    """overall class to manage game assests and behavior"""

    def __init__(self):
        """initialize the game and create resource"""
        pygame.init()
        self.Setting=Settings()
        self.bg_color=self.Setting.bg_color
        self.clock=pygame.time.Clock()

        self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.Setting.screen_width=self.screen.get_rect().width
        self.Setting.screen_height=self.screen.get_rect().height
        pygame.display.set_caption("Warship")
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        self._create_fleet()

    def _create_fleet(self):
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size

        current_x,current_y=alien_width,alien_height
        while current_y<(self.Setting.screen_height-3*alien_height):
            while current_x<(self.Setting.screen_width-2*alien_width):
                self._create_alien(current_x,current_y)
                current_x+=2*alien_width
            current_x=alien_width
            current_y+=2*alien_height

    def _create_alien(self,x_positon,y_position):
        new_alien = Alien(self)
        new_alien.x=x_positon
        new_alien.rect.x=x_positon
        new_alien.rect.y=y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y+=self.Setting.fleet_drop_speed
        self.Setting.fleet_direction *=-1

                    
    def _check_keydown_events(self,event):
        """respond to keypress"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left=True
        elif event.key == pygame.K_q:
            sys.exit()
             

    def _check_keyup_events(self,event):
         """Response to key release"""
         if event.key == pygame.K_RIGHT:
            self.ship.moving_right=False
         elif event.key == pygame.K_LEFT:
            self.ship.moving_left=False

    def _fire_bullet(self):
        if len(self.bullets)<self.Setting.bullet_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)  

    def _check_events(self):
        """response to event"""
        #watch for keyboard and mouse movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event) 
        
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
                if bullet.rect.bottom<=0:
                    self.bullets.remove(bullet)   

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        #recent draw of bullet
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)
        #make recently drawn screen visible
        pygame.display.flip()

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        

    def run_game(self):
        while True:
            """Start main loop for the game """
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)



if __name__=="__main__":
    ai=Warship()
    ai.run_game()
