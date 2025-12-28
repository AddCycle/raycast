import math

# window settings
TITLE = "THE DARKNESS FP CHASE"

# tilesize & wall size
TILESIZE = 64
WALL_SIZE = TILESIZE

# map size
ROWS = 15
COLS = 20

# FOV & sensitivity
FOV = math.radians(60)
MOUSE_SENSITIVITY = 0.1

# player settings
RADIUS = 10 # affecting collision distance between walls

# resolution: affecting number of rays to calculate
RES = 4

# precision: to avoid rays hitting through walls (gaps between walls)
PRECISION_FIX_GAPS = 0.0001

# lighting: affecting darkness
LIGHT_LEVEL = 60