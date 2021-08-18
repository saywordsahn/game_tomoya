import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/bullet.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, enemy_group):
        self .rect.y -= 3

        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.spritecollide(self, enemy_group, True):
            self.kill()
