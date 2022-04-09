import pygame

# ПУЛІ

class Bullet(pygame.sprite.Sprite):
    def __init__(self,screen,gun):
        # Пуля в центрі пушки
        super(Bullet,self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,2,12)
        self.color = 204,220,57
        self.speed = 5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        #Переміщення пулі вверх
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        #Пуля на екрані
        pygame.draw.rect(self.screen,self.color,self.rect)

