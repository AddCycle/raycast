import math

# tilesize & wall size
TILESIZE = 64
WALL_SIZE = TILESIZE

# map size
ROWS = 10
COLS = 15

# FOV & sensitivity
FOV = math.radians(60)
MOUSE_SENSITIVITY = 0.1

# resolution: affecting number of rays to calculate
RES = 4

# precision: to avoid rays hitting through walls (gaps between walls)
PRECISION_FIX_GAPS = 0.0001

# lighting: affecting darkness
LIGHT_LEVEL = 60