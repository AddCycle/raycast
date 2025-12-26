import pygame
import random as rand
from settings import *

class Map:

    def __init__(self, cols: int, rows: int) -> None:
        self.cols = cols
        self.rows = rows
        self.horiz_walls = 2
        self.vert_walls = 2
        # self.procedural_random_grid()
        # self.sample_grid()
        self.procedural_maze()
    
    def init_grid(self):
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def random_grid(self):
        self.grid = [[rand.randint(0,1) for _ in range(self.cols)] for _ in range(self.rows)]

    # shitty debug function for sample only no maze actually
    def procedural_maze(self, wall_chance=0.3):
        self.grid = [
        [
            1 if (
                x == 0 or y == 0 or
                x == self.cols - 1 or y == self.rows - 1 or
                rand.random() < wall_chance
            ) else 0
            for x in range(self.cols)
        ]
        for y in range(self.rows)
    ]

    # 15,10 only
    def sample_grid(self):
        self.grid = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
            [1,1,0,0,0,0,1,0,0,0,0,0,0,0,1],
            [1,0,1,0,0,0,0,0,0,1,1,1,1,1,1],
            [1,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,0,1,0,0,0,0,0,0,0,0,1],
            [1,0,1,0,0,1,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ]

    # working on it TODO
    def procedural_random_grid(self):
        self.init_grid()
        self.put_map_edges()
        for i in range(self.horiz_walls):
            edge_space = 2
            length = rand.randint(1, self.cols - 1 - edge_space) # length of the wall but a small exit
            print(f"length : {length}")
            y = rand.randint(0 + edge_space, self.rows - 1 - edge_space) # edges walls
            x = rand.choice((0, self.cols - 1)) # left or right wall
            print(f"x : {x}")
            if (x == 0):
                self.h_wall(x + 1, y, length)
            else:
                self.h_wall(x - length, y, length)

    def put_map_edges(self):
        self.put_horizontal_wall(0, self.cols, 0) # top
        self.put_horizontal_wall(0, self.cols, self.rows - 1) # bottom
        self.put_vertical_wall(0, 0, self.rows) # left
        self.put_vertical_wall(self.cols - 1, 0, self.rows) # right
    
    # pixel coords for player pos
    def has_wall_at(self, x:float, y:float):
        return self.grid[int(y // TILESIZE)][int(x // TILESIZE)]

    # with length
    def h_wall(self, x:int, y:int, len: int):
        self.put_horizontal_wall(x, x + len, y)

    # with length
    def v_wall(self, x:int, y:int, len: int):
        self.put_vertical_wall(x, y, y + len)

    # Between 2 points
    def put_horizontal_wall(self, x1: int, x2: int, y: int):
        self.put_wall((x1, y), (x2, y))

    # Between 2 points
    def put_vertical_wall(self, x: int, y1: int, y2: int):
        self.put_wall((x, y1), (x, y2))
    
    # Between 2 points
    def put_wall(self, p1:tuple, p2:tuple):
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        xDist = abs(x2 - x1)
        yDist = abs(y2 - y1)

        # vertical wall
        if x1 == x2 and y1 != y2:
            for i in range(yDist):
                if (y1 + i < self.rows):
                    self.grid[y1 + i][x1] = 1
                else:
                    self.grid[self.rows - 1][x1] = 1

        # horizontal wall
        elif x1 != x2 and y1 == y2:
            for i in range(xDist):
                if (x1 + i < self.cols):
                    self.grid[y1][x1 + i] = 1
                else:
                    self.grid[y1][self.cols - 1] = 1
        
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