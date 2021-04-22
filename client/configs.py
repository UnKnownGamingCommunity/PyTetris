#===========[ Game-Setting - Begin ]======================
fps = 60                     # set the framerate of the game
zoom = 30                    # set the size of the output
multiColorBlock = True       # enable multiple colors (blocks - also known as tetriminos - only)
multiColorMenu = True        # enable multiple menu colors
updatePressingKey = fps / 20 # update the pressed keys per second
maxItemStack = 10            # count of stored items
itemsOnFiled = 0.05             # percent of items on the filed
#===========[ Game-Setting - End ]========================

#===========[ Colors - Begin ]============================
# set the color values - (red, green, blue)
clBlack = (0, 0, 0)
clWhite = (255, 255, 255)
clDarkGray = (48, 48, 48)
clMenuBorder = (255, 255, 255)
clMenuBackground = (0, 0, 0)
clMenuTextSelected = (255, 255, 255)
clMenuTextUnselected = (200, 200, 200)
clMenuTextDisabled = (128, 128, 128)
clMenuBackgroundSelected = (60, 60, 60)

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
    clBlockBorderColors = [
        (0, 200, 200),  # I-Block
        (0, 0, 200),    # J-Block
        (210, 100, 0),  # L-Block
        (220, 185, 0),  # O-Block
        (0, 200, 0),    # Z-Block
        (130, 0, 200),  # T-Block
        (200, 0, 0),    # S-Block
        (210, 210, 210) # unknown Block
    ]
else:
    clActiveBlock = (255, 255, 255) # current block
    clActiveBlockBorder = (210, 210, 210) # current block
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
    clBlockBorderColors = [
        (160, 160, 160), # I-Block
        (160, 160, 160), # J-Block
        (160, 160, 160), # L-Block
        (160, 160, 160), # O-Block
        (160, 160, 160), # Z-Block
        (160, 160, 160), # T-Block
        (160, 160, 160), # S-Block
        (160, 160, 160)  # unknown Block
    ]

if multiColorMenu:
    clChckeBoxOnSelected = (0, 200, 0)
    clChckeBoxOffSelected = (200, 0, 0)
    clChckeBoxOnUnselected = (0, 130, 0)
    clChckeBoxOffUnselected = (130, 0, 0)
else:
    clChckeBoxOnSelected = (255, 255, 255)
    clChckeBoxOffSelected = (255, 255, 255)
    clChckeBoxOnUnselected = (200, 200, 200)
    clChckeBoxOffUnselected = (200, 200, 200)
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

#===========[ Level Increase - Begin ]====================
# points to increase the level - point divergent
levelUp = [
    300,   # to level 2
    400,   # to level 3
    550,   # to level 4
    750,   # to level 5
    1000,  # to level 6
    1300,  # to level 7
    1650,  # to level 8
    2050,  # to level 9
    2500,  # to level 10
    3000,  # to level 11
    3550,  # to level 12
    4150,  # to level 13
    4800,  # to level 14
    5500,  # to level 15
    6250,  # to level 16
    7050,  # to level 17
    7900,  # to level 18
    8800,  # to level 19
    9750,  # to level 20
    10750, # to level 21
    11800, # to level 22
    12900, # to level 23
    14050, # to level 24
    15250, # to level 25
    17800, # to level 26
    19150, # to level 27
    20550, # to level 28
    22000, # to level 29
    23500  # to level 30
]
#===========[ Level Increase - End ]======================

#===========[ Items - Begin ]=============================
# list of singleplayer item IDs
itemIDsSingleplayer = [
    1001, # nuke
    1002, # left shift
    1003, # down shift
    1004  # delete line
]

# list of multiplayer item IDs
itemIDsMultiPlayer = [
    2001, # random blocks
    2002, # swap field
    2003  # add line
    # ToDo: add item ids of the single player items
]
#===========[ Items - End ]===============================
