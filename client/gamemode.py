import configs
import game
import pygame
import menu


gameMenuScale = 1
gameMenuWidth = 8

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

    gameover_font = None
    text_gameover = None

    def __init__(self, _screen, level):
        self.gameList = [game.Tetris(10, 20, 4, 1)]
        self.gameInput = self.gameList[0]  # the local game
        self.gameList[0].newBlock()
        self.screen = _screen

        # create font and text
        self.gameover_font = pygame.font.SysFont('DejaVu Sans', int(2.44 * configs.zoom), True, False)
        self.text_gameover = self.gameover_font.render("Game Over!", True, (255, 255, 255))

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
                    if event.key == pygame.K_ESCAPE:
                        if gameMenu.enabled:
                            gameMenu.enabled = False
                            self.gameInput.state = "running"
                            gameMenu.reset()
                        else:
                            gameMenu.enabled = True
                            self.gameInput.state = "paused"
                            gameMenu.reset()

                self.gameInput.updateInput(event)

            if self.gameInput.state == "running":
                self.gameInput.updatePressedImput()
            #=======[ Game-Input - End ]==========================

            #=======[ Draw Game - Begin ]=========================
            self.screen.fill(color=configs.clBlack)  # "clear" the screen
            # draw every field
            for game in self.gameList:
                # update current block - go to the ground
                if game.state == "running":
                    game.goDown()

                game.draw(self.screen)

                # draw game over screen
                if game.state == "gameover":
                    pygame.draw.rect(self.screen, color=configs.clBlack, rect=[int(0.5 * configs.zoom), int(9.175 * configs.zoom), int(17 * configs.zoom), int(3.25 * configs.zoom)])
                    pygame.draw.rect(self.screen, color=configs.clWhite, rect=[int(0.5 * configs.zoom), int(9.175 * configs.zoom), int(17 * configs.zoom), int(3.25 * configs.zoom)], width=1)
                    self.screen.blit(self.text_gameover, [int(0.9 * configs.zoom), int(9.375 * configs.zoom)])

            gameMenu.drawMenu()
            pygame.display.flip()  # update screen
            #=======[ Draw Game - End ]===========================

            clock.tick(configs.fps)  # wait time to reach the fps

        return exitGame