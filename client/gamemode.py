import configs
import game
import pygame
import menu
import functions


gameMenuScale = 1
gameMenuWidth = 8
gameFiledBorderDistanceX = 1.5
gameFiledBorderDistanceY = 1

# "gameMenuItemList" = [[vertical menu, menu items ...] menu areas]
gameMenuItemList = [[
    True,
    menu.Button("Resume", 1, gameMenuScale, gameMenuWidth, True, "resume", True),
    menu.Button("Main Menu", 1, gameMenuScale, gameMenuWidth, True, "main_menu", True),
    menu.Button("Exit", 1, gameMenuScale, gameMenuWidth, True, "exit", True)
]]

class SinglePlayer:
    gameList = []      # the list of all needed games
    gameInput = None   # the local game
    screen = None
    level = 0
    itemsEnabled = False

    gameover_font = None
    text_gameover = None
    value_font = None
    header_font = None
    text_next = None
    text_score = None
    text_level = None

    def __init__(self, _screen, _level, _levelSpeed, _itemsEnabled, _windowWidth, _windowHeight):
        filedWidth = 10
        filedHeight = 20
        self.gameList = [game.Tetris(filedWidth, filedHeight, _windowWidth - gameFiledBorderDistanceX - filedWidth, gameFiledBorderDistanceY, _level, _levelSpeed, _itemsEnabled)]
        self.gameInput = self.gameList[0]  # the local game
        self.screen = _screen
        self.level = _level
        self.itemsEnabled = _itemsEnabled

        # create font and text
        self.gameover_font = pygame.font.SysFont('DejaVu Sans', int(2.44 * configs.zoom), True, False)
        self.text_gameover = self.gameover_font.render("Game Over!", True, configs.clWhite)

        self.value_font = pygame.font.SysFont('DejaVu Sans', int(0.8 * configs.zoom), True, False)

        self.header_font = pygame.font.SysFont('DejaVu Sans', int(1.1 * configs.zoom), True, False)
        self.text_next = self.header_font.render("Next", True, configs.clWhite)
        self.text_score = self.header_font.render("Score", True, configs.clWhite)
        self.text_level = self.header_font.render("Level", True, configs.clWhite)

    def run(self, clock, windowWidth, windowHeight):
        gameMenu = menu.Menu((windowWidth - (gameMenuWidth + 1) * gameMenuScale) / 2, (windowHeight - 7.3 * gameMenuScale) / 2, (gameMenuWidth + 1) * gameMenuScale, 7.3 * gameMenuScale, gameMenuScale, gameMenuItemList, self.screen)
        gameMenu.enabled = False

        exitGame = False
        backToMenu = False # exit game mode
        while not backToMenu and not exitGame:
            #=======[ Game-Input - Begin ]========================
            for event in pygame.event.get():
                menuItem = gameMenu.updateInput(event)
                if menuItem == "resume":
                    gameMenu.enabled = False
                    self.gameInput.state = "running"
                    gameMenu.reset()
                elif menuItem == "main_menu":
                    backToMenu = True
                elif menuItem == "exit":
                    exitGame = True

                # exit application
                if event.type == pygame.QUIT:
                    exitGame = True

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and self.gameInput.state != "gameover":
                        if gameMenu.enabled:
                            gameMenu.enabled = False
                            self.gameInput.state = "running"
                            gameMenu.reset()
                        else:
                            gameMenu.enabled = True
                            self.gameInput.state = "paused"
                            gameMenu.reset()
                    if event.key == pygame.K_ESCAPE and self.gameInput.state == "gameover":
                        backToMenu = True

                self.gameInput.updateInput(event)

            if self.gameInput.state == "running":
                self.gameInput.updatePressedImput()
            #=======[ Game-Input - End ]==========================

            #=======[ Draw Game - Begin ]=========================
            self.screen.fill(color=configs.clBlack)  # "clear" the screen

            # draw next block box
            (xSize, ySize) = self.text_score.get_size()
            xRacPos = int(gameFiledBorderDistanceX * configs.zoom)
            yRacPos = int(gameFiledBorderDistanceY * configs.zoom) - 1
            xRacWidth = int(6 * configs.zoom)
            yRacHeight = int(3.2 * configs.zoom) + ySize
            pygame.draw.rect(self.screen, color=configs.clBlack, rect=[xRacPos, yRacPos, xRacWidth, yRacHeight])
            pygame.draw.rect(self.screen, color=configs.clWhite, rect=[xRacPos, yRacPos, xRacWidth, yRacHeight], width=1)

            # draw next block header
            xFontOffset = xRacPos
            yFontOffset = yRacPos + int(0.25 * configs.zoom)
            self.screen.blit(self.text_next, [xFontOffset + int((xRacWidth - xSize) / 2), yFontOffset])
            yFontOffset += ySize + 0.5 * configs.zoom
            # update next block
            _block = self.gameList[0].nextBlock
            blockSize = 0
            if 3 in _block.image() or 7 in _block.image() or 11 in _block.image() or 16 in _block.image():
                blockSize = 4
            elif 2 in _block.image() or 6 in _block.image() or 10 in _block.image() or 15 in _block.image():
                blockSize = 3
            else:
                blockSize = 2
            functions.DrawSingleBlock(self.screen, xFontOffset + int((xRacWidth - blockSize * configs.zoom) / 2), yFontOffset, _block)

            # draw score box
            (xSize, ySize) = self.text_level.get_size()
            yRacPos += int(0.5 * configs.zoom) + yRacHeight
            yRacHeight = int(1 * configs.zoom) + ySize + self.value_font.get_height()
            pygame.draw.rect(self.screen, color=configs.clBlack, rect=[xRacPos, yRacPos, xRacWidth, yRacHeight])
            pygame.draw.rect(self.screen, color=configs.clWhite, rect=[xRacPos, yRacPos, xRacWidth, yRacHeight], width=1)

            # draw score header
            yFontOffset = yRacPos + 0.25 * configs.zoom
            self.screen.blit(self.text_score, [xFontOffset + int((xRacWidth - xSize) / 2), yFontOffset])
            yFontOffset += ySize
            # update score
            scoreValueText = self.value_font.render(str(self.gameInput.score), True, configs.clWhite)
            (xSize, ySize) = scoreValueText.get_size()
            yFontOffset += 0.5 * configs.zoom
            self.screen.blit(scoreValueText, [xFontOffset + int((xRacWidth - xSize) / 2), yFontOffset])

            # draw level box
            yRacPos += int(0.5 * configs.zoom) + yRacHeight
            pygame.draw.rect(self.screen, color=configs.clBlack, rect=[xRacPos, yRacPos, xRacWidth, yRacHeight])
            pygame.draw.rect(self.screen, color=configs.clWhite, rect=[xRacPos, yRacPos, xRacWidth, yRacHeight], width=1)

            # draw level header
            (xSize, ySize) = self.text_level.get_size()
            yFontOffset = yRacPos + 0.25 * configs.zoom
            self.screen.blit(self.text_level, [xFontOffset + int((xRacWidth - xSize) / 2), yFontOffset])
            yFontOffset += ySize
            # update level
            levelUpdateText = self.value_font.render(str(self.gameInput.level), True, configs.clWhite)
            (xSize, ySize) = levelUpdateText.get_size()
            yFontOffset += 0.5 * configs.zoom
            self.screen.blit(levelUpdateText, [xFontOffset + int((xRacWidth - xSize) / 2), yFontOffset])

            # draw every field
            for game in self.gameList:
                # update current block - go to the ground
                if game.state == "running":
                    game.goDown()

                game.draw(self.screen)

                # draw game over screen
                if game.state == "gameover":
                    (xSize, ySize) = self.text_gameover.get_size()
                    xOffset = int((windowWidth * configs.zoom - xSize - configs.zoom * 0.5) / 2)
                    yOffset = int((windowHeight * configs.zoom - ySize - configs.zoom * 0.5) / 2)
                    pygame.draw.rect(self.screen, color=configs.clBlack, rect=[xOffset, int(9.175 * configs.zoom), int(17 * configs.zoom), int(3.25 * configs.zoom)])
                    pygame.draw.rect(self.screen, color=configs.clWhite, rect=[xOffset, int(9.175 * configs.zoom), int(17 * configs.zoom), int(3.25 * configs.zoom)], width=1)
                    self.screen.blit(self.text_gameover, [int((windowWidth * configs.zoom - xSize) / 2), int((windowHeight * configs.zoom - ySize) / 2)])

            gameMenu.drawMenu()
            pygame.display.flip()  # update screen
            #=======[ Draw Game - End ]===========================

            clock.tick(configs.fps)  # wait time to reach the fps

        return exitGame