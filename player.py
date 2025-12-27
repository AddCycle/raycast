from constants import *
import pygame

def normalizeAngle(angle: float):
    angle = angle % (2 * math.pi)
    if (angle <= 0):
        angle += 2 * math.pi
    return angle

class Player:
    def __init__(self) -> None:
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.radius = 3
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
        self.x += math.cos(self.rotationAngle) * moveStep
        self.y += math.sin(self.rotationAngle) * moveStep

        strafeStep = self.moveSpeed * self.strafeDirection
        self.x += -math.sin(self.rotationAngle) * strafeStep
        self.y +=  math.cos(self.rotationAngle) * strafeStep

    def render(self, screen: pygame.Surface):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 3)

        pygame.draw.line(screen, (0, 0, 255), (self.x, self.y), (self.x + math.cos(self.rotationAngle) * 50, self.y + math.sin(self.rotationAngle) * 50))