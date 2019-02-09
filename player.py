import pygame
from entity import Ent
import globals


class Player(Ent):

    def __init__(self,x, y, sprite, hp):
        Ent.__init__(self, x, y, sprite, hp)

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



