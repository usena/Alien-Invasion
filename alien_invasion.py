#Book Link: https://bedford-computing.co.uk/learning/wp-content/uploads/2015/10/No.Starch.Python.Oct_.2015.ISBN_.1593276036.pdf

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship=Ship(ai_settings,screen)
    bullets=Group()
    
    bg_color=(230,230,230)
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,bullets)
run_game()