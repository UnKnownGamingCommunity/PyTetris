import pygame
import menu
import configs
import gamemode


#===========[ Create Window - Begin ]=====================
pygame.init()
screen = pygame.display.set_mode((18 * configs.zoom, 22 * configs.zoom))
pygame.display.set_caption("Tetris")
#===========[ Create Window - End ]=======================

#===========[ Main-Loop - Begin ]=========================
myGame = gamemode.SinglePlayer(screen)
clock = pygame.time.Clock()
myGame.run(clock)

pygame.quit()
#===========[ Main-Loop - End ]===========================