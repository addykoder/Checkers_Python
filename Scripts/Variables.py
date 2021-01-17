
# physical properties of the game

# this will create a board of dimension ( dimension * dimension pixels)
dimension = 720

# this will create a board with units (unit * unit)
units = 8
unit_size = dimension//units

# Colors
dark_block = (0, 0, 0)
light_block = (255, 255, 255)

dark_piece = (255, 100, 0)
dark_king = (255, 0, 100)

light_piece = (0, 100, 255)
light_king = (0, 255, 0)

# Game Flow

# chancing
chance = [1,3]
next = [2,4]


# hovering the grabbed piece
hover_piece = 0
took_from = 0
avails = []

d = [1,3]
u = [2,4]
