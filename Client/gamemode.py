import configs
import game
import pygame

class SinglePlayer:
    gameList = []      # the list of all needed games
    gameInput = None   # the local game
    backToMenu = False # exit game mode
    screen = None

    # create font and text
    gameover_font = None
    text_gameover = None

    def __init__(self, _screen):
        self.gameList = [game.Tetris(10, 20, 4, 1)]
        self.gameInput = self.gameList[0]  # the local game
        self.gameList[0].newBlock()
        self.screen = _screen
        self.gameover_font = pygame.font.SysFont('DejaVu Sans', int(2.44 * configs.zoom), True, False)
        self.text_gameover = self.gameover_font.render("Game Over!", True, (255, 255, 255))

    def run(self, clock):
        while not self.backToMenu:
            #=======[ Game-Input - Begin ]========================
            self.backToMenu = self.gameInput.updateInput()
            #=======[ Game-Input - End ]==========================

            #=======[ Draw Game - Begin ]=========================
            self.screen.fill(color=configs.clBlack)  # "clear" the screen
            # draw every field
            for game in self.gameList:
                # update current block - go to the ground
                if game.state != "gameover":
                    game.goDown()

                game.draw(self.screen)

                # draw game over screen
                if game.state == "gameover":
                    pygame.draw.rect(self.screen, color=configs.clBlack, rect=[int(0.5 * configs.zoom), int(9.175 * configs.zoom), int(17 * configs.zoom), int(3.25 * configs.zoom)])
                    pygame.draw.rect(self.screen, color=configs.clWhite, rect=[int(0.5 * configs.zoom), int(9.175 * configs.zoom), int(17 * configs.zoom), int(3.25 * configs.zoom)], width=1)
                    self.screen.blit(self.text_gameover, [int(0.9 * configs.zoom), int(9.375 * configs.zoom)])

            pygame.display.flip()  # update screen
            #=======[ Draw Game - End ]===========================

            clock.tick(configs.fps)  # wait time to reach the fps