from settings import *
import pygame
from map import Map
from player import Player
from raycaster import Raycaster

screen = pygame.display.set_mode((WIDTH, HEIGHT))
map = Map(COLS, ROWS)
player = Player()
raycaster = Raycaster(player, map)
map_view = True

clock = pygame.Clock()
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEMOTION:
            player.using_keyboard_rotation = False
    
    # general key commands
    keys = pygame.key.get_just_pressed()
    long_press_keys = pygame.key.get_pressed()

    if long_press_keys[pygame.K_RIGHT] or long_press_keys[pygame.K_d] or long_press_keys[pygame.K_LEFT] or long_press_keys[pygame.K_a]:
        player.using_keyboard_rotation = True

    if keys[pygame.K_ESCAPE]: # quit
        pygame.quit()
        exit()
    if keys[pygame.K_RETURN]: # switch view
        map_view = not map_view

    # update
    player.update(map_view)
    raycaster.castAllRays()

    # render
    screen.fill((0,0,0))

    if map_view:
        map.render(screen)
        player.render(screen)

    raycaster.render(screen, map_view)

    pygame.display.update()