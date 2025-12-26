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
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # general key commands
    keys = pygame.key.get_just_pressed()

    if keys[pygame.K_ESCAPE]: # quit
        pygame.quit()
        exit()
    if keys[pygame.K_RETURN]: # switch view
        map_view = not map_view

    # update
    player.update()
    raycaster.castAllRays()

    # render
    screen.fill((0,0,0))

    if map_view:
        map.render(screen)
        player.render(screen)

    raycaster.render(screen, map_view)

    pygame.display.update()