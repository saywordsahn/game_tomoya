import random

import pygame

from player import Player

from enemy import Enemy
pygame.init()

screen_width = 600
screen_height = 800
clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load('img/bg.png')

player = Player(screen_width)
player_group = pygame.sprite.Group(player)

enemy_group = pygame.sprite.Group()

for row in range(5):
    for col in range(5):
        enemy = Enemy( 100 + col * 100, 100 + row * 70)
        enemy_group.add(enemy)

bullet_group = pygame.sprite.Group()
while True:

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            exit(0)

    player.update(keys, bullet_group)

    for bullet in bullet_group:
        bullet.update(enemy_group)

    screen.blit(background, (0,0))
    player_group.draw(screen)
    enemy_group.draw(screen)
    bullet_group.draw(screen)
    pygame.display.flip()

    clock.tick(FPS)









