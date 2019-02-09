import pygame
import globals


class Ent(pygame.sprite.Sprite):

    def __init__(self, x, y, sprite, hp):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.hp = hp

        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def health_points(self):
        # DEALS WITH DEATH CONDITION
        if self.hp == 0:
            print("hello")






