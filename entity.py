import pygame
import globals


class Entity(pygame.sprite.Sprite):

    def __init__(self, x, y, move_speed,sprite):
        self.x = x
        self.y = y
        self.sprite = sprite

        pygame.sprite.Sprite.__init__(self)
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):



    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # PLAYER MOVEMENT
                print(self.y)
                if event.key == pygame.K_w:
                    self.y -= 64
                    print("w")
                if event.key == pygame.K_DOWN:
                    self.y += 64
                if event.key == pygame.K_LEFT:
                    self.y -= 64
                if event.key == pygame.K_RIGHT:
                    self.y += 64









