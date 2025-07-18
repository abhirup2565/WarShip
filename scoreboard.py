import pygame.font

class Scoreboard:
    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        self.settings=ai_game.Setting
        self.stats=ai_game.stats
        #font setting
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)
        #Prepare initial score image
        self.prep_score()

    def prep_score(self):
        """Turn the score into a render image"""
        score_str = str(self.stats.score)
        rounded_score=round(self.stats.score,-1)
        score_str=f"{rounded_score:,}"
        self.score_image=self.font.render(score_str,True,self.text_color,self.settings.bg_color)
        #Display the score at the top right of the screen
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect) 