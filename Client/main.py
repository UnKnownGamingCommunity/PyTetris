import pygame
import menu
import configs
import gamemode


#===========[ Create Window - Begin ]=====================
pygame.init()
windowWidth = 18
windowHeight = 22
screen = pygame.display.set_mode((windowWidth * configs.zoom, windowHeight * configs.zoom))
pygame.display.set_caption("Tetris")
#===========[ Create Window - End ]=======================

#===========[ Main-Loop - Begin ]=========================
mainMenuScale = 1
menuMenuWidth = 10
menuItemList = [[
    menu.Button("Singleplayer", 1, mainMenuScale, menuMenuWidth, True, "singleplayer", True),
    menu.Button("Coop", 1, mainMenuScale, menuMenuWidth, True, "coop", False),
    menu.Button("Coop 2 vs 2", 1, mainMenuScale, menuMenuWidth, True, "coop_2vs2", False),
    menu.Button("2 vs 2", 1, mainMenuScale, menuMenuWidth, True, "2vs2", False),
    menu.Button("Death Match", 1, mainMenuScale, menuMenuWidth, True, "deathmatch", False),
    menu.Button("Options", 1, mainMenuScale, menuMenuWidth, True, "options", False),
    menu.Button("Exit", 1, mainMenuScale, menuMenuWidth, True, "exit", True)
]]

mainMenu = menu.Menu(int((windowWidth - (menuMenuWidth + 1) * mainMenuScale) / 2), int((windowHeight - 15 * mainMenuScale) / 2), (menuMenuWidth + 1) * mainMenuScale, 15 * mainMenuScale, mainMenuScale, menuItemList, screen)
clock = pygame.time.Clock()

exitGame = False
menuItem = "none"
while not exitGame:
    (menuItem, exitGame) = mainMenu.updateInput()

    screen.fill(color=configs.clBlack)  # "clear" the screen
    mainMenu.drawMenu()
    pygame.display.flip()  # update screen

    if menuItem == "singleplayer":
        myGame = gamemode.SinglePlayer(screen)
        exitGame = myGame.run(clock)
    elif menuItem == "coop":
        pass
    elif menuItem == "coop_2vs2":
        pass
    elif menuItem == "2vs2":
        pass
    elif menuItem == "deathmatch":
        pass
    elif menuItem == "options":
        pass
    elif menuItem == "exit":
        exitGame = True

    clock.tick(configs.fps)  # wait time to reach the fps

pygame.quit()
#===========[ Main-Loop - End ]===========================