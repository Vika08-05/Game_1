import pygame
from pygame.sprite import Sprite

class Gun(Sprite):
    def __init__(self,screen):
        # Ініціалізація пушки
        super(Gun,self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = float(self.screen_rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False


    def output(self):
            #Рисования пушки
            self.screen.blit(self.image, self.rect)

    def update_gun(self):
        # Обновление позиции пушки
        if self.mright and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.mleft and self.rect.left > 0:
            self.rect.centerx -= 1
    def create_gun(self):
        # Пушка по центру в низу
        self.center = self.screen_rect.centerx
