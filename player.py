from settings import *
import pygame

class Player:
    def __init__(self) -> None:
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.radius = 3
        self.turnDirection = 0
        self.walkDirection = 0
        self.rotationAngle = 0
        self.moveSpeed = 2.5
        self.rotationSpeed = math.radians(2)

    def update(self):
        keys = pygame.key.get_pressed()
        
        self.turnDirection = 0
        self.walkDirection = 0

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.turnDirection = 1
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.turnDirection = -1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.walkDirection = 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.walkDirection = -1

        # rotation
        self.rotationAngle += self.turnDirection * self.rotationSpeed

        # movement
        moveStep = self.moveSpeed * self.walkDirection
        self.x += math.cos(self.rotationAngle) * moveStep
        self.y += math.sin(self.rotationAngle) * moveStep

    def render(self, screen: pygame.Surface):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 3)

        pygame.draw.line(screen, (0, 0, 255), (self.x, self.y), (self.x + math.cos(self.rotationAngle) * 50, self.y + math.sin(self.rotationAngle) * 50))