import pygame
import libtcodpy as libtcod
import globals

PLAYER_X = 20
PLAYER_Y = 20

# PYGAME INITIALISATION
pygame.init()
main_surface = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))


# INPUT SCANNING
def handle_keys():
    global PLAYER_X, PLAYER_Y

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # PLAYER MOVEMENT
            if event.key == pygame.K_UP:
                PLAYER_Y -= 1
            if event.key == pygame.K_DOWN:
                PLAYER_Y += 1
            if event.key == pygame.K_LEFT:
                PLAYER_X -= 1
            if event.key == pygame.K_RIGHT:
                PLAYER_X += 1


# DRAWS GRID ON SCREEN TO ILLUSTRATE TILES
def grid():
    for x in range(0, globals.SCREEN_WIDTH):
        for y in range(0, globals.SCREEN_HEIGHT):
            if x >= globals.TILE_SIZE and y >= globals.TILE_SIZE:
                if x % globals.TILE_SIZE == 0 and y % globals.TILE_SIZE == 0:
                    pygame.draw.line(main_surface, (255, 255, 255), (x, 0), (x, globals.SCREEN_HEIGHT))
                    pygame.draw.line(main_surface, (255, 255, 255), (0, y), (globals.SCREEN_WIDTH, y))


def main():
    globals.CLOCK.tick(globals.LIMIT_FPS)
    grid()

    while True:
        handle_keys()

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

        pygame.display.flip()
    pygame.quit()


main()







