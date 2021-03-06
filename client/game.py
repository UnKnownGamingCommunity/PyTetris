import pygame
import configs
import block
import functions

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
    nextBlock = None   # the next block
    goDownSpeed = 0    # the speed for the current block to go down to the ground - in frames
    goDownCounter = 0  # the counter for updating the current block to go down to the ground
    series = 0         # the counter for deleted lines in differ moves
    level = 1
    itemEnabled = False
    nextLevel = 0
    levelSpeed = 0

    # hold "right move key" update variables
    pressingRight = False
    pressingRightCounter = 0
    pressingRightFirstUpdate = 0
    # hold "left move key" update variables
    pressingLeft = False
    pressingLeftCounter = 0
    pressingLeftFirstUpdate = 0

    # set the default values for this game
    def __init__(self, _width, _height, posX, posY, _level, _levelSpeed, _itemsEnabled):
        self.height = _height
        self.width = _width
        self.fieldPosX = posX * configs.zoom
        self.fieldPosY = posY * configs.zoom
        self.field = []
        self.score = 0
        self.state = "running"
        self.goDownCounter = 1
        self.series = 0
        self.pressingRight = False
        self.pressingRightCounter = 0
        self.pressingRightFirstUpdate = 0
        self.pressingLeft = False
        self.pressingLeftCounter = 0
        self.pressingLeftFirstUpdate = 0
        self.level = _level
        self.itemEnabled = _itemsEnabled
        self.nextLevel = configs.levelUp[_level - 1] * _levelSpeed
        self.levelSpeed = _levelSpeed
        self.block = block.Block(3, 0)
        self.nextBlock = block.Block(3, 0)

        self.updateDropSpeed()

        # create the field lines and values
        for i in range(_height):
            new_line = []
            for j in range(_width):
                new_line.append(0)
            self.field.append(new_line)

    def newBlock(self):
        self.block = self.nextBlock
        self.nextBlock = block.Block(3, 0)
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
            self.score += (deletedLines ** 2) * self.series * self.level
            if self.score >= self.nextLevel:
                self.nextLevel += configs.levelUp[self.level] * self.levelSpeed
                self.level += 1
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

    # update the game by the input
    def updateInput(self, event):
        if self.state == "running":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.rotateRight()
                if event.key == pygame.K_DOWN:
                    self.rotateLeft()
                if event.key == pygame.K_RIGHT:
                    self.pressingRight = True
                    self.pressingRightCounter = 1
                    self.pressingRightFirstUpdate = 0
                    self.moveRight()
                if event.key == pygame.K_LEFT:
                    self.pressingLeft = True
                    self.pressingLeftCounter = 1
                    self.pressingLeftFirstUpdate = 0
                    self.moveLeft()
                if event.key == pygame.K_SPACE:
                    self.drop()

            # reset the pressed keys
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.pressingRight = False
                if event.key == pygame.K_LEFT:
                    self.pressingLeft = False

    # update pressed keys
    def updatePressedImput(self):
        if self.state != "gameover":
            if self.pressingLeft and self.pressingLeftCounter == 0:
                self.moveLeft()
                self.pressingLeftCounter = 1
            if self.pressingRight and self.pressingRightCounter == 0:
                self.moveRight()
                self.pressingRightCounter = 1

            self.pressingLeftFirstUpdate += 1
            self.pressingRightFirstUpdate += 1
            if self.pressingLeftFirstUpdate > configs.updatePressingKey * 5:
                self.pressingLeftCounter = (self.pressingLeftCounter + 1) % (configs.updatePressingKey + 1)
            if self.pressingRightFirstUpdate > configs.updatePressingKey * 5:
                self.pressingRightCounter = (self.pressingRightCounter + 1) % (configs.updatePressingKey + 1)

    def updateDropSpeed(self):
        self.goDownSpeed = configs.fps * 2 - int(configs.fps * 0.065 * self.level)

    def draw(self, screen):
        # draw game field border
        pygame.draw.rect(screen, color=configs.clWhite, rect=[self.fieldPosX - 1, self.fieldPosY - 1, self.width * configs.zoom + 2, self.height * configs.zoom + 2], width=1)

        # draw game field
        for i in range(self.height):
            for j in range(self.width):
                border = False
                clBlock = configs.clWhite
                clBorder = configs.clWhite
                if self.field[i][j] == 0 or self.state == "paused":
                    border = True
                    clBorder = configs.clDarkGray
                elif self.field[i][j] > len(configs.clBlockColors):
                    clBlock = configs.clBlockColors[7]
                    clBorder = configs.clBlockBorderColors[7]
                elif self.field[i][j] > 0:
                    clBlock = configs.clBlockColors[self.field[i][j] - 1]
                    clBorder = configs.clBlockBorderColors[self.field[i][j] - 1]

                if not border:
                    pygame.draw.rect(screen, color=clBlock, rect=[self.fieldPosX + j * configs.zoom, self.fieldPosY + i * configs.zoom, configs.zoom, configs.zoom])
                pygame.draw.rect(screen, color=clBorder, rect=[self.fieldPosX + j * configs.zoom, self.fieldPosY + i * configs.zoom, configs.zoom, configs.zoom], width=1)

        # draw game current block
        if self.block is not None and self.state != "paused":
            functions.DrawSingleBlock(screen, self.fieldPosX + self.block.x * configs.zoom, self.fieldPosY + self.block.y * configs.zoom, self.block)
#===========[ Game-Class - End ]==========================