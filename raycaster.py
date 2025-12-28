from constants import *
import pygame
from player import Player
from ray import Ray
from map import Map
from enemy import Enemy

class Raycaster:
    def __init__(self, player: Player, enemy: Enemy, map: Map) -> None:
        self.rays:list[Ray] = []
        self.player = player
        self.enemy = enemy
        self.map = map

        # texturing walls
        self.wall_texture = pygame.image.load("assets/walls.png").convert()
        self.crosshair = pygame.transform.scale_by(pygame.image.load("assets/crosshair.png").convert_alpha(), 4)
        self.tex_w = self.wall_texture.get_width()
        self.tex_h = self.wall_texture.get_height()
    
    def castAllRays(self):
        self.rays = []
        rayAngle = self.player.rotationAngle - FOV / 2
        for _ in range(NUM_RAYS):
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
                # projection
                distance_to_projection_plane = (WIDTH / 2) / math.tan(FOV / 2)
                dist = max(ray.distance, 0.0001)
                line_height = (WALL_SIZE / dist) * distance_to_projection_plane

                # texturing walls instead of blank rectangles
                hit_pos = 0
                if ray.vertical_hit:
                    hit_pos = ray.wall_hit_y
                else:
                    hit_pos = ray.wall_hit_x
                
                tex_x = int((hit_pos % WALL_SIZE) / WALL_SIZE * self.tex_w) # type: ignore

                draw_begin = (HEIGHT / 2) - (line_height / 2)
                draw_end = line_height

                # pygame.draw.rect(screen, (ray.color, ray.color, ray.color), (i * RES, draw_begin, RES, draw_end)) # type: ignore

                wall_slice = self.wall_texture.subsurface(tex_x, 0, 1, self.tex_h)
                wall_slice = pygame.transform.scale(wall_slice, (RES, int(line_height)))

                screen.blit(wall_slice, (i * RES, draw_begin))

                i += 1

        if not map_view:
            # crosshair rendering
            screen.blit(self.crosshair, (WIDTH // 2, HEIGHT // 2))

            # enemy rendering

            dx = self.enemy.x - self.player.x
            dy = self.enemy.y - self.player.y

            enemy_dist = math.hypot(dx, dy)
            enemy_angle = math.atan2(dy, dx) - self.player.rotationAngle

            screen_x = (enemy_angle / (FOV / 2)) * (WIDTH / 2) + (WIDTH / 2)
            ray_index = int(screen_x // RES)

            if 0 <= ray_index < len(self.rays):
                if enemy_dist < self.rays[ray_index].distance or enemy_dist < 5:
                    # draw enemy
                    self.enemy.render(screen, enemy_dist, screen_x)