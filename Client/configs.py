#===========[ Game-Setting - Begin ]======================
fps = 60                # set the framerate of the game
zoom = 20               # set the size of the output
multiColorBlock = True  # enable multiple colors (blocks - also known as tetriminos - only)
#===========[ Game-Setting - End ]========================

#===========[ Colors - Begin ]============================
# set the color values - (red, green, blue)
clBlack = (0, 0, 0)
clWhite = (255, 255, 255)
clDarkGray = (48, 48, 48)
clMenuBorder = (255, 255, 255)
clMenuBackground = (0, 0, 0)
if multiColorBlock:
    clBlockColors = [
        (0, 240, 240),  # I-Block
        (0, 0, 240),    # J-Block
        (255, 128, 0),  # L-Block
        (220, 220, 0),  # O-Block
        (0, 240, 0),    # Z-Block
        (160, 0, 240),  # T-Block
        (240, 0, 0),    # S-Block
        (255, 255, 255) # unknown Block
    ]
else:
    clActiveBlock = (255, 255, 255) # current block
    clBlockColors = [
        (200, 200, 200), # I-Block
        (200, 200, 200), # J-Block
        (200, 200, 200), # L-Block
        (200, 200, 200), # O-Block
        (200, 200, 200), # Z-Block
        (200, 200, 200), # T-Block
        (200, 200, 200), # S-Block
        (200, 200, 200)  # unknown Block
    ]
#===========[ Colors - End ]==============================

#===========[ Block-List - Begin ]========================
# blocks are in 4x4 matrices, numbered over x:
#   | 0 1 2 3 |
#   | 4 5 6 7 |
#   | 8 9 a b |
#   | c d e f |

# "allBlocks" = [[[[SHAPE POSITIONS] ROTATION] TYPE]]

allBlocks = [
    [[4, 5, 6, 7], [1, 5, 9, 13]],                            # I-Block
    [[0, 4, 5, 6], [0, 1, 4, 8], [0, 1, 2, 6], [1, 5, 8, 9]], # J-Block
    [[2, 4, 5, 6], [0, 4, 8, 9], [0, 1, 2, 4], [0, 1, 5, 9]], # L-Block
    [[0, 1, 4, 5]],                                           # O-Block
    [[1, 2, 4, 5], [0, 4, 5, 9]],                             # Z-Block
    [[1, 4, 5, 6], [0, 4, 5, 8], [0, 1, 2, 5], [1, 4, 5, 9]], # T-Block
    [[0, 1, 5, 6], [1, 4, 5, 8]]                              # S-Block
]
#===========[ Block-List - End ]==========================