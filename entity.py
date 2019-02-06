import pygame
import globals


class Entity(pygame.sprite.Sprite):

    def __init__(self, x, y, sprite, hp):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.hp = hp

        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        # INPUT HANDLING FOR MOVEMENT
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.rect.y -= globals.TILE_SIZE
                if event.key == pygame.K_s:
                    self.rect.y += globals.TILE_SIZE
                if event.key == pygame.K_a:
                    self.rect.x -= globals.TILE_SIZE
                if event.key == pygame.K_d:
                    self.rect.x += globals.TILE_SIZE





