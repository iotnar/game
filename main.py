import pygame, controls
from gun import GUN
from pygame.sprite import Group

def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Заруба")
    bg_color = (0, 00, 00)
    gun = GUN(screen)
    bullets = Group()
    while True:
        controls.events(screen, gun, bullets)
        gun.updategun()
        controls.update(bg_color, screen, gun, bullets)
        controls.updete_bullets(bullets)

run()

