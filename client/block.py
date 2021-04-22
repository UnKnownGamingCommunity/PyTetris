import configs
import random

#===========[ Block-Class - Begin ]=======================
class Block:
    x = 0        # position in the game field
    y = 0        # position in the game field
    rotation = 0 # rotation index of "allBlocks"
    type = 0     # type index of "allBlocks"

    # set the default values for this block
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        self.rotation = 0
        self.type = random.randint(0, len(configs.allBlocks) - 1)

    # get the shape of the block
    def image(self):
        return configs.allBlocks[self.type][self.rotation]

    # rotate the block clockwise
    def rotateRight(self):
        self.rotation = (self.rotation + 1) % len(configs.allBlocks[self.type])

    # rotate the block counter-clockwise
    def rotateLeft(self):
        self.rotation = (self.rotation - 1) % len(configs.allBlocks[self.type])
#===========[ Block-Class - End ]=========================