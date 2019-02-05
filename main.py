import pygame
import libtcodpy as libtcod
import globals

PLAYER_X = 20
PLAYER_Y = 20


def handle_keys():
    global PLAYER_X, PLAYER_Y



def main():
    # GAME INITIALISATION AND GAME LOOP
    pygame.init()
    main_surface = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))

    globals.clock.tick(globals.LIMIT_FPS)
    while True:
        event = pygame.event.poll()

        if event.type == pygame.QUIT:
            break

        main_surface.fill((0, 200, 255))

        pygame.display.flip()
    pygame.quit()
main()






