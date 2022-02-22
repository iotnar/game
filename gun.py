import pygame

class Gun():

    def __init__(self, screen):

        self.screen = screen
        self.image = pygame.image.load('pic/pixilart-drawing.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False
        self.speed = 0.05

    def output(self):
        """рисование пушки"""

        self.screen.blit(self.image, self.rect)

    def updategun(self):


        """обновление позиции пушки"""


        if self.mright == True and self.rect.right < self.screen_rect.right and self.speed >= 0:
            self.center += self.speed  #скорость пушки

        if self.mleft == True and self.rect.left > 0 and self.speed >= 0:
             self.center -= self.speed

        self.rect.centerx = self.center
