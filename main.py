import pygame
import libtcodpy as libtcod
import globals

libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT, globals.TITLE, False)
libtcod.sys_set_fps(globals.LIMIT_FPS)


def handle_keys():
    global globals.PLAYER_X, globals.PLAYERY

    # UTILITY INPUT SCANNING
    key = libtcod.console_check_for_keypress()

    # LALT AND ENTER TOGGLE FULL SCREEN
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
    elif key.vk == libtcod.KEY_ESCAPE:
        return True

    # INPUT SCANNING FOR MOVEMENT
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        globals.PLAYER_Y -= 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        globals.PLAYER_Y += 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        globals.PLAYER_X += 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        globals.PLAYER_X -= 1


while not libtcod.console_is_window_closed():
    libtcod.console_set_default_foreground(0, libtcod.white)
    libtcod.console_put_char(0, 1, 1, '@', libtcod.BKGND_NONE)
    libtcod.console_flush()

    # KEY HANDLING AND GAME EXITING
    exit = handle_keys()
    if exit:
        break




