import pygame
import random

#===========[ Game-Setting - Begin ]======================
fps = 60                # set the framerate of the game
zoom = 20               # set the size of the output
multiColorBlock = True  # enable multiple colors (blocks - also known as tetriminos - only)
#===========[ Game-Setting - End ]========================



#===========[ Create Window - Begin ]=====================
pygame.init()
screen = pygame.display.set_mode((18 * zoom, 22 * zoom))
pygame.display.set_caption("Tetris")
#===========[ Create Window - End ]=======================

#===========[ Colors - Begin ]============================
# set the color values - (red, green, blue)
clBlack = (0, 0, 0)
clWhite = (255, 255, 255)
clDarkGray = (48, 48, 48)
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
        self.type = random.randint(0, len(allBlocks) - 1)

    # get the shape of the block
    def image(self):
        return allBlocks[self.type][self.rotation]

    # rotate the block clockwise
    def rotateRight(self):
        self.rotation = (self.rotation + 1) % len(allBlocks[self.type])

    # rotate the block counter-clockwise
    def rotateLeft(self):
        self.rotation = (self.rotation - 1) % len(allBlocks[self.type])
#===========[ Block-Class - End ]=========================

#===========[ Game-Class - Begin ]========================
class Tetris:
    height = 0         # height of the field
    width = 0          # width of the field
    field = []         # the filed list
    score = 0          # current sore of the game
    state = "ignore"   # state oth the game
    fieldPosX = 0      # position of the field in the window - only used on draw
    fieldPosY = 0      # position of the field in the window - only used on draw
    block = None       # the current block
    goDownSpeed = 0    # the speed for the current block to go down to the ground - in frames
    goDownCounter = 0  # the counter for updating the current block to go down to the ground
    series = 0         # the counter for deleted lines in differ moves

    # set the default values for this game
    def __init__(self, _width, _height, posX, posY):
        self.height = _height
        self.width = _width
        self.fieldPosX = posX * zoom
        self.fieldPosY = posY * zoom
        self.field = []
        self.score = 0
        self.state = "running"
        self.goDownSpeed = fps * 2
        self.goDownCounter = 1
        self.series = 0

        # create the field lines and values
        for i in range(_height):
            new_line = []
            for j in range(_width):
                new_line.append(0)
            self.field.append(new_line)

    def newBlock(self):
        self.block = Block(3, 0)
        if self.checkInterscetion():
            self.state = "gameover"
            self.block = None

    # rotate the current block clockwise
    def rotateRight(self):
        self.block.rotateRight()
        if self.checkInterscetion():
            self.block.rotateLeft()

    # rotate the current block counter-clockwise
    def rotateLeft(self):
        self.block.rotateLeft()
        if self.checkInterscetion():
            self.block.rotateRight()

    # move the current block in "deltaX" way
    def moveSideway(self, deltaX):
        self.block.x += deltaX
        if self.checkInterscetion():
            self.block.x -= deltaX

    # move the current block to the right side
    def moveRight(self):
        self.moveSideway(1)

    # move the current block to the left side
    def moveLeft(self):
        self.moveSideway(-1)

    # place the current block in the field
    def placeBlock(self):
        if self.block is not None:
            for i in range(4):
                for j in range(4):
                    position = i * 4 + j
                    if position in self.block.image():
                        self.field[i + self.block.y][j + self.block.x] = self.block.type + 1

        self.cleanField()

    # drop the current block and place the block in the field
    def drop(self):
        while not self.checkInterscetion():
            self.block.y += 1

        self.block.y -= 1
        self.placeBlock()

        self.newBlock()

    # move the current block down
    def goDown(self):
        if self.goDownCounter == 0:
            self.block.y += 1
            if (self.checkInterscetion()):
                self.block.y -= 1
                self.placeBlock()
                self.newBlock()

        self.goDownCounter =  (self.goDownCounter + 1) % self.goDownSpeed

    # check the filed and remove complete lines
    def cleanField(self):
        deletedLines = 0
        for i in range(self.height - 1, 0, -1):
            # mark complete kines
            line = self.field[i]
            lineIsFull = True
            for j in range(self.width):
                if line[j] == 0:
                    lineIsFull = False
                    break

            # remove line
            if lineIsFull:
                deletedLines += 1
                self.field.pop(i)

        # fill the field up - create new lines
        for i in range(deletedLines):
            new_line = []
            for j in range(self.width):
                new_line.append(0)
            self.field.insert(0, new_line)

        # update score
        if deletedLines > 0:
            self.series += 1
            self.score += ((deletedLines + 1) ** 2) * self.series
        else:
            self.series = 0

    # check the new position of the current block for intersection
    def checkInterscetion(self):
        if self.block is not None:
            for i in range(4):
                for j in range(4):
                    position = i * 4 + j
                    if position in self.block.image():
                        # the block is outside of the field or a block ist on the same position
                        if i + self.block.y > self.height - 1 or i + self.block.y < 0 or\
                           j + self.block.x > self.width - 1 or j + self.block.x < 0 or\
                           self.field[i + self.block.y][j + self.block.x] > 0:
                            return True
        return False

#===========[ Game-Class - End ]==========================


#===========[ Main-Loop - Begin ]=========================
# list of all running games
gameList = [Tetris(10, 20, 4, 1)]
gameInput = gameList[0]  # the local game
gameList[0].newBlock()

# hold "right move key" update variables
pressingRight = False
pressingRightCounter = 0
pressingRightFirstUpdate = 0
# hold "left move key" update variables
pressingLeft = False
pressingLeftCounter = 0
pressingLeftFirstUpdate = 0

# create font and text
gameover_font = pygame.font.SysFont('DejaVu Sans', int(2.44 * zoom), True, False)
text_gameover = gameover_font.render("Game Over!", True, (255, 255, 255))

exitGame = False
clock = pygame.time.Clock()
updatePressingKey = fps / 10 # update the pressed keys per second
while not exitGame:
    #=======[ Game-Input - Begin ]========================
    for event in pygame.event.get():
        # exit application
        if event.type == pygame.QUIT:
                exitGame = True

        elif gameInput.state != "gameover":
            # set the pressed keys and update key-events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    gameInput.rotateRight()
                if event.key == pygame.K_DOWN:
                    gameInput.rotateLeft()
                if event.key == pygame.K_RIGHT:
                    pressingRight = True
                    pressingRightCounter = 1
                    pressingRightFirstUpdate = 0
                    gameInput.moveRight()
                if event.key == pygame.K_LEFT:
                    pressingLeft = True
                    pressingLeftCounter = 1
                    pressingLeftFirstUpdate = 0
                    gameInput.moveLeft()
                if event.key == pygame.K_SPACE:
                    gameInput.drop()

            # reset the pressed keys
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    pressingRight = False
                if event.key == pygame.K_LEFT:
                    pressingLeft = False

    # update pressed keys
    if gameInput.state != "gameover":
        updateCounter = False
        if pressingLeft and pressingLeftCounter == 0:
            gameInput.moveLeft()
            pressingLeftCounter = 1
        if pressingRight and pressingRightCounter == 0:
            gameInput.moveRight()
            pressingRightCounter = 1

        pressingLeftFirstUpdate += 1
        pressingRightFirstUpdate += 1
        if pressingLeftFirstUpdate > updatePressingKey * 5:
            pressingLeftCounter = (pressingLeftCounter + 1) % (updatePressingKey + 1)
        if pressingRightFirstUpdate > updatePressingKey * 5:
            pressingRightCounter = (pressingRightCounter + 1) % (updatePressingKey + 1)
    #=======[ Game-Input - End ]==========================

    #=======[ Draw Game - Begin ]=========================
    screen.fill(color=clBlack)  # "clear" the screen
    # draw every field
    for game in gameList:
        # update current block - go to the ground
        if game.state != "gameover":
            game.goDown()

        # draw game field border
        pygame.draw.rect(screen, color=clWhite, rect=[game.fieldPosX - 1, game.fieldPosY - 1, game.width * zoom + 2, game.height * zoom + 2], width=1)

        # draw game field
        for i in range(game.height):
            for j in range(game.width):
                border = 0
                clBlock = clWhite
                if game.field[i][j] == 0:
                    border = 1
                    clBlock = clDarkGray
                elif game.field[i][j] > 0:
                    clBlock = clBlockColors[game.field[i][j] - 1]

                pygame.draw.rect(screen, color=clBlock, rect=[game.fieldPosX + j * zoom, game.fieldPosY + i * zoom, zoom, zoom], width=border)

        # draw game current block
        if game.block is not None:
            for i in range(4):
                for j in range(4):
                    position = i * 4 + j
                    if position in game.block.image():
                        clBlock = clBlockColors[game.block.type]
                        if not multiColorBlock:
                            clBlock = clActiveBlock
                        pygame.draw.rect(screen, color=clBlock, rect=[game.fieldPosX + (j + game.block.x) * zoom, game.fieldPosY + (i + game.block.y) * zoom, zoom, zoom])

        # draw game over screen
        if game.state == "gameover":
            pygame.draw.rect(screen, color=clBlack, rect=[int(0.5 * zoom), int(9.175 * zoom), int(17 * zoom), int(3.25 * zoom)])
            pygame.draw.rect(screen, color=clWhite, rect=[int(0.5 * zoom), int(9.175 * zoom), int(17 * zoom), int(3.25 * zoom)], width=1)
            screen.blit(text_gameover, [int(0.9 * zoom), int(9.375 * zoom)])

    pygame.display.flip()  # update screen
    #=======[ Draw Game - End ]===========================

    clock.tick(fps)  # wait time to reach the fps

pygame.quit()
#===========[ Main-Loop - End ]===========================