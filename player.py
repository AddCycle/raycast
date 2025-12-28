from constants import *
from map import Map
import pygame

def normalizeAngle(angle: float):
    angle = angle % (2 * math.pi)
    if (angle <= 0):
        angle += 2 * math.pi
    return angle

class Player:
    def __init__(self, map: Map) -> None:
        self.x = map.entrance[1] * TILESIZE + TILESIZE // 2
        self.y = map.entrance[0] * TILESIZE + TILESIZE // 2
        self.map = map
        self.radius = RADIUS
        self.turnDirection = 0
        self.walkDirection = 0
        self.strafeDirection = 0
        self.rotationAngle = 0
        self.pitchAngle = 0 # TODO later adding support to y-axis
        self.moveSpeed = 2.5
        self.rotationSpeed = math.radians(2)

    def update(self, map_view: bool):
        keys = pygame.key.get_pressed()
        mx,my = pygame.mouse.get_pos()
        
        self.turnDirection = 0
        self.walkDirection = 0
        self.strafeDirection = 0
        self.rotationSpeed = math.radians(2)

        # rotation
        if map_view:
            self.rotationAngle = math.atan2(my - self.y, mx - self.x)
        else:
            dx, _ = pygame.mouse.get_rel()
            self.rotationAngle += dx * self.rotationSpeed * MOUSE_SENSITIVITY

        # movement
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.walkDirection = 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.walkDirection = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.strafeDirection = 1
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.strafeDirection = -1

        moveStep = self.moveSpeed * self.walkDirection
        strafeStep = self.moveSpeed * self.strafeDirection

        next_x = self.x
        next_y = self.y

        next_x += math.cos(self.rotationAngle) * moveStep
        next_y += math.sin(self.rotationAngle) * moveStep

        next_x += -math.sin(self.rotationAngle) * strafeStep
        next_y +=  math.cos(self.rotationAngle) * strafeStep

        r = self.radius

        # X axis
        if not (
            self.map.has_wall_at(next_x + r, self.y) or
            self.map.has_wall_at(next_x - r, self.y)
        ):
            self.x = next_x

        # Y axis
        if not (
            self.map.has_wall_at(self.x, next_y + r) or
            self.map.has_wall_at(self.x, next_y - r)
        ):
            self.y = next_y

    def render(self, screen: pygame.Surface):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 3)

        pygame.draw.line(screen, (0, 0, 255), (self.x, self.y), (self.x + math.cos(self.rotationAngle) * 50, self.y + math.sin(self.rotationAngle) * 50))