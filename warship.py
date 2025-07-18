import sys
import pygame
from time import sleep

from button import Button
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from scoreboard import Scoreboard

class Warship:
    """overall class to manage game assests and behavior"""

    def __init__(self):
        """initialize the game and create resource"""
        pygame.init()
        #alien invasion in active state
        self.game_active=False
        self.Setting=Settings()
        self.bg_color=self.Setting.bg_color
        self.clock=pygame.time.Clock()
        self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.Setting.screen_width=self.screen.get_rect().width
        self.Setting.screen_height=self.screen.get_rect().height
        pygame.display.set_caption("Warship")
        self.stats=GameStats(self)
        self.sb = Scoreboard(self)
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        self._create_fleet()
        self.play_button=Button(self,"play")
        

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
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self,mouse_pos):
            button_clicked=self.play_button.rect.collidepoint(mouse_pos)
            if button_clicked and not self.game_active:
                self.Setting.initialize_dynamic_settings()
                self.stats.reset_stats()
                self.game_active=True
                self.bullets.empty()
                self.aliens.empty()
                self._create_fleet()
                self.ship.center_ship()
                #hide mouse cursor
                pygame.mouse.set_visible(False)
        
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
                if bullet.rect.bottom<=0:
                    self.bullets.remove(bullet) 
        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):  
        collisions=pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if collisions:
            self.stats.score+=self.Setting.alien_points
            self.sb.prep_score()
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.Setting.increase_speed()

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        #recent draw of bullet
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        if not self.game_active:
            self.play_button.draw_button()
        #make recently drawn screen visible
        pygame.display.flip()

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        self._check_alien_bottom()
        
    def _ship_hit(self):
        if self.stats.ship_left>0:
            self.stats.ship_left-=1
            #deleting any bullets or aliens
            self.bullets.empty()
            self.aliens.empty()
            #create new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            #pause
            sleep(0.5)
        else:
            self.game_active=False

    def _check_alien_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom>=self.Setting.screen_height:
                self._ship_hit()
                break

    def run_game(self):
        while True:
            """Start main loop for the game """
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)



if __name__=="__main__":
    ai=Warship()
    ai.run_game()
