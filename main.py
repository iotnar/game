import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from random import randint

pygame.mixer.pre_init
pygame.init()
pygame.mixer.music.load('Wav/start_muzik.mp3')
pygame.mixer.music.play()

gun_shot = pygame.mixer.Sound('Wav/vyistrel-s-vibratsiey.wav')
vzruv = pygame.mixer.Sound('Wav/vzruv.wav')





def run():


    pygame.init()
    screen = pygame.display.set_mode((500, 600))
    pygame.display.set_caption("Заруба")
    clock = pygame.time.Clock()
    FPS = 120
    bg_color = (0, 00, 00)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.bild_army(screen, inos)

    while True:
        controls.events(screen, gun,  bullets, gun_shot)
        gun.updategun()
        controls.update(bg_color, screen, gun, inos, bullets)
        controls.update_bullets(screen, bullets, inos, vzruv)
        controls.update_inos(inos)
        clock.tick(FPS)

run ()



