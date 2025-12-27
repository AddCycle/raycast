from constants import *
import pygame
from player import Player
from ray import Ray
from map import Map

class Raycaster:
    def __init__(self, player: Player, map: Map) -> None:
        self.rays:list[Ray] = []
        self.player = player
        self.map = map
    
    def castAllRays(self):
        self.rays = []
        rayAngle = self.player.rotationAngle - FOV / 2
        for i in range(NUM_RAYS):
            ray = Ray(rayAngle, self.player, self.map)
            ray.cast()
            self.rays.append(ray)
            rayAngle += FOV / NUM_RAYS

    def render(self, screen: pygame.Surface, map_view: bool):
        i = 0
        for ray in self.rays:
            if map_view:
                ray.render(screen)
            else:
                distance_to_projection_plane = (WIDTH / 2) // math.tan(FOV / 2)
                line_height = (WALL_SIZE / ray.distance) * distance_to_projection_plane

                draw_begin = (HEIGHT / 2) - (line_height / 2)
                draw_end = line_height
                pygame.draw.rect(screen, (ray.color, ray.color, ray.color), (i * RES, draw_begin, RES, draw_end)) # type: ignore

                i += 1