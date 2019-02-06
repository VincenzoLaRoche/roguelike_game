import pygame
import os


# DISPLAY VALUES
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1280
CLOCK = pygame.time.Clock()
LIMIT_FPS = 120
TITLE = "Rogue like test game"

# MAP VALUES
TILE_SIZE = 32

# FILE LOCATIONS
GAME_FOLDER = os.path.dirname(__file__)
IMG_FOLDER = os.path.join(GAME_FOLDER, 'img')

# SPRITES
PLAYER_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'player.jpg'))

