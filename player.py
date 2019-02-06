import pygame
import entity
import globals


class Player(entity.Entity):

    def __init__(self):
        entity.Entity(1, 2)

    def movement(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # PLAYER MOVEMENT
                if event.key == pygame.K_UP:
                    globals.PLAYER_Y -= 64
                if event.key == pygame.K_DOWN:
                    globals.PLAYER_Y += 64
                if event.key == pygame.K_LEFT:
                    globals.PLAYER_X -= 64
                if event.key == pygame.K_RIGHT:
                    globals.PLAYER_X += 64


