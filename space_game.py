import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():
    pygame.init()
    screen = pygame.display.set_mode((700,700))
    pygame.display.set_caption("Космические защитники")
    bg_color = (0,0,0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()  
    score = Scores(screen,stats)


    while True:
        controls.events(screen,gun,bullets)
        if stats.run_game:
            gun.update_gun() 
            controls.update(bg_color,screen,stats,score,gun,inos,bullets)
            controls.update_bullets(screen,stats,score,inos,bullets)  
            controls.update_inos_y(stats,screen,score,gun,inos,bullets)  
                      

run()
   