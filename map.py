import pygame
import random as rand
from constants import *

class Map:
    def __init__(self, cols: int, rows: int) -> None:
        self.cols = cols
        self.rows = rows
        self.procedural_maze()
    
    def init_grid(self):
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
    
    # helper functions
    def in_bounds(self, x, y):
        return 0 <= x < self.cols and 0 <= y < self.rows
    
    def neighbors(self, x, y):
        # Only cardinal directions (up, down, left, right)
        dirs = [(0, -2), (2, 0), (0, 2), (-2, 0)]
        result = []
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if self.in_bounds(nx, ny) and self.grid[ny][nx] == 1:
                result.append((nx, ny))
        return result

    def init_maze_grid(self):
        self.grid = [[1 for _ in range(self.cols)] for _ in range(self.rows)]
    
    def generate_maze(self):
        self.init_maze_grid()
    
        stack = []
        start_x, start_y = 1, 1  # always start at top-left inner cell
        self.grid[start_y][start_x] = 0
        stack.append((start_x, start_y))
    
        while stack:
            x, y = stack[-1]
            nbs = self.neighbors(x, y)
            if nbs:
                nx, ny = nbs[rand.randint(0, len(nbs)-1)]
                # Remove wall between current and neighbor
                wall_x = (x + nx) // 2
                wall_y = (y + ny) // 2
                self.grid[wall_y][wall_x] = 0
                self.grid[ny][nx] = 0
                stack.append((nx, ny))
            else:
                stack.pop()
    
        # Entrance and exit
        self.grid[0][1] = 0  # top entrance
        self.grid[self.rows-1][self.cols-2] = 0  # bottom exit
        self.entrance = (0, 1)
        self.exit = (self.rows-1, self.cols-2)
    
    def procedural_maze(self):
        self.generate_maze()

    # pixel coords for player pos
    def has_wall_at(self, x: float, y: float):
        grid_x = int(x // TILESIZE)
        grid_y = int(y // TILESIZE)
    
        if grid_x < 0 or grid_x >= self.cols or grid_y < 0 or grid_y >= self.rows:
            return True  # treat out-of-map as wall
    
        return self.grid[grid_y][grid_x]
    
    def render(self, screen: pygame.Surface) -> None:
        rows = len(self.grid)
        cols = len(self.grid[0])
        for i in range(rows):
            for j in range(cols):
                tile_x = j * TILESIZE
                tile_y = i * TILESIZE
                if i == self.entrance[0] and j == self.entrance[1]:
                    pygame.draw.rect(screen, (0, 0, 255), (tile_x, tile_y, TILESIZE, TILESIZE)) # wall
                elif i == self.exit[0] and j == self.exit[1]:
                    pygame.draw.rect(screen, (255, 0, 0), (tile_x, tile_y, TILESIZE, TILESIZE)) # wall
                elif self.grid[i][j] == 1:
                    pygame.draw.rect(screen, (40, 40, 40), (tile_x, tile_y, TILESIZE, TILESIZE)) # wall
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (tile_x, tile_y, TILESIZE, TILESIZE)) # empty
        
        self.draw_grid(screen)
    
    def draw_grid(self, screen: pygame.Surface):
        rows = len(self.grid)
        cols = len(self.grid[0])
        for i in range(cols):
            pygame.draw.line(screen, (0, 0, 0), (i * TILESIZE, 0), (i * TILESIZE, HEIGHT))

        for j in range(rows):
            pygame.draw.line(screen, (0, 0, 0), (0, j * TILESIZE), (WIDTH, j * TILESIZE))
        
    def __str__(self) -> str:
        fmt = ""
        rows = len(self.grid)
        cols = len(self.grid[0])
        for i in range(rows):
            for j in range(cols):
                num = str(self.grid[i][j])
                fmt += f"{num} "
            fmt = fmt.strip()
            fmt += '\n'
        
        fmt += f"ROWS: {rows}, COLS: {cols}"
        
        return fmt