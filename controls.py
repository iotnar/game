import pygame, sys
from bullet import Bullet
from ino import Ino


def events(screen, gun, bullets):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False

def update(bg_color, screen, gun, inos, bullets):
    """обновление экрана"""

    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(bullets, inos):
    """обновляем позиции пулек"""

    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)

def update_inos(inos):
    inos.update()

def bild_army(screen, inos):
    """создаем армию"""

    ino = Ino(screen)
    ino_width = ino.rect.width
    ino_height = ino.rect.height
    namber_ino_line = int((500 - (ino_width * 2 ) )/ ino_width)
    namber_ino_row = int((600 - 100 - (ino_height*2)) / ino_height)
    print(ino_width, ino_height, namber_ino_row, namber_ino_line)
    for ino_row in range(namber_ino_row-15):
        for ino_line in range(namber_ino_line-int(namber_ino_line/4)):
            ino = Ino(screen)
            ino.x = ino_width + (ino_width+5) * ino_line
            ino.y = ino_height + 2 * ino_height * ino_row
            ino.rect.x = ino.x
            ino.rect.y = ino.y
            inos.add(ino)