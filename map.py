import pygame
import random as rand
from settings import *

class Map:

    def __init__(self, cols: int, rows: int) -> None:
        self.cols = cols
        self.rows = rows
        self.init_grid()
        self.put_map_edges()
    
    def init_grid(self):
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def random_grid(self):
        return [[rand.randint(0,1) for _ in range(self.cols)] for _ in range(self.rows)]

    # working
    def randomize_grid(self):
        self.init_grid()

    def put_map_edges(self):
        self.put_horizontal_wall(0, self.cols, 0) # top
        self.put_horizontal_wall(0, self.cols, self.rows - 1) # bottom
        self.put_vertical_wall(0, 0, self.rows) # left
        self.put_vertical_wall(self.cols - 1, 0, self.rows) # right

    def put_horizontal_wall(self, x1: int, x2: int, y: int):
        self.put_wall((x1, y), (x2, y))

    def put_vertical_wall(self, x: int, y1: int, y2: int):
        self.put_wall((x, y1), (x, y2))
    
    def put_wall(self, p1:tuple, p2:tuple):
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        xDist = abs(x2 - x1)
        yDist = abs(y2 - y1)
        print(f"xDist: {xDist}")
        print(f"yDist: {yDist}")

        # vertical wall
        if x1 == x2 and y1 != y2:
            for i in range(yDist):
                if (y1 + i < self.rows):
                    self.grid[y1 + i][x1] = 1

        # horizontal wall
        elif x1 != x2 and y1 == y2:
            for i in range(xDist):
                if (x1 + i < self.cols):
                    self.grid[y1][x1 + i] = 1
        
        # diagonal wall TODO
        else:
            pass
    
    def render(self, screen: pygame.Surface) -> None:
        rows = len(self.grid)
        cols = len(self.grid[0])
        for i in range(rows):
            for j in range(cols):
                tile_x = j * TILESIZE
                tile_y = i * TILESIZE
                if self.grid[i][j]:
                    pygame.draw.rect(screen, (40, 40, 40), (tile_x, tile_y, TILESIZE, TILESIZE)) # wall
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (tile_x, tile_y, TILESIZE, TILESIZE)) # empty
    
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