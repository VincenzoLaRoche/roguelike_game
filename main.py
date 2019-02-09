import pygame
import libtcodpy as libtcod
import globals
from player import Player

# PYGAME INITIALISATION
pygame.init()
pygame.mixer.init()
pygame.display.set_caption(globals.TITLE)
main_surface = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))

# SPRITE GROUP
player_sprites = pygame.sprite.Group()
player = Player(20, 20, globals.PLAYER_IMG, 0)
player_sprites.add(player)


# INPUT SCANNING
def handle_keys():
    pass


# DRAWS GRID ON SCREEN TO ILLUSTRATE TILES
def grid():
    for x in range(0, globals.SCREEN_WIDTH):
        for y in range(0, globals.SCREEN_HEIGHT):
            if x >= globals.TILE_SIZE and y >= globals.TILE_SIZE:
                if x % globals.TILE_SIZE == 0 and y % globals.TILE_SIZE == 0:
                    pygame.draw.line(main_surface, (255, 255, 255), (x, 0), (x, globals.SCREEN_HEIGHT))
                    pygame.draw.line(main_surface, (255, 255, 255), (0, y), (globals.SCREEN_WIDTH, y))


def main():
    grid()

    running = True
    while running:
        globals.CLOCK.tick(globals.LIMIT_FPS)

        # UPDATE
        player_sprites.update()

        # DRAW
        main_surface.fill((0, 255, 255))
        player_sprites.draw(main_surface)

        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

        # DISPLAY FLIP
        pygame.display.flip()

    pygame.quit()


main()







