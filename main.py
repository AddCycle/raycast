from settings import *
import pygame
from map import Map

screen = pygame.display.set_mode((WIDTH, HEIGHT))
map = Map(COLS, ROWS)
print(map)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0,0,0))

    map.render(screen)

    pygame.display.update()