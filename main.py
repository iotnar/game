import pygame, controls
from gun import Gun
from pygame.sprite import Group


def run():

    pygame.init()
    screen = pygame.display.set_mode((500, 600))
    pygame.display.set_caption("Заруба")
    bg_color = (0, 00, 00)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.bild_army(screen, inos)

    while True:
        controls.events(screen, gun,  bullets)
        gun.updategun()
        controls.update(bg_color, screen, gun, inos, bullets)
        controls.update_bullets(bullets, inos)
        controls.update_inos(inos)

run ()



