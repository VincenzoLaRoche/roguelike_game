import pygame
import libtcodpy as libtcod
import globals,entity, os

# PYGAME INITIALISATION
pygame.init()
main_surface = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))


player = entity.Entity(20, 20, 4, globals.PLAYER_IMG)



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

        # FUNCTION CALLS
        player.move()
        player.update()

        # DRAW SPRITES TO SCREEN
        pygame.display.flip()

    pygame.quit()


main()







