from constants import *
import pygame
from player import Player

class Enemy:
    def __init__(self, x:int, y:int, texture: pygame.Surface, player: Player) -> None:
        self.x = x
        self.y = y
        self.texture = texture
        self.speed = 1.0
        self.radius = 10
        self.player = player
        self.enemy_min_dist = 10 # FIXME : here settings cf. 1

    def update(self):
        dx = self.player.x - self.x
        dy = self.player.y - self.y
        dist = math.hypot(dx, dy)

        if dist > self.player.radius + self.enemy_min_dist: # FIXME : add a proper settings variable for max gap between player & enemy cf. 1
            self.x += (dx / dist) * self.speed
            self.y += (dy / dist) * self.speed
        # else:
        #     # TODO : PROPERLY => GAME OVER (gamestates)
        #     # pygame.quit()
        #     # exit()
        #     # print("GAME OVER")
    
    def render(self, screen: pygame.Surface, enemy_dist, screen_x):
        distance_to_plane = (WIDTH / 2) / math.tan(FOV / 2)
        enemy_height = (WALL_SIZE / enemy_dist) * distance_to_plane
        enemy_width = enemy_height

        texture = pygame.transform.scale(
            self.texture,
            (int(enemy_width), int(enemy_height))
        )

        screen.blit(
            texture,
            (int(screen_x - enemy_width // 2),
             int(HEIGHT // 2 - enemy_height // 2))
        )
    
    def render_2d_pos(self, screen: pygame.Surface):
        pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), self.radius)