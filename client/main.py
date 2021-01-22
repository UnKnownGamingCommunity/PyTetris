import pygame
import configs


#===========[ Create Window - Begin ]=====================
pygame.init()
windowWidth = 18
windowHeight = 22
screen = pygame.display.set_mode((windowWidth * configs.zoom, windowHeight * configs.zoom))
pygame.display.set_caption("Tetris")
#===========[ Create Window - End ]=======================

import menu
import gamemode

mainMenuScale = 1
menuMenuWidth = 10

# "mainMenuItemList" = [[vertical menu, menu items ...] menu areas]
mainMenuItemList = [[
    True,
    menu.Button("Singleplayer", 1, mainMenuScale, menuMenuWidth, True, "singleplayer", True),
    menu.Button("Coop", 1, mainMenuScale, menuMenuWidth, True, "coop", False),
    menu.Button("Coop 2 vs 2", 1, mainMenuScale, menuMenuWidth, True, "coop_2vs2", False),
    menu.Button("2 vs 2", 1, mainMenuScale, menuMenuWidth, True, "2vs2", False),
    menu.Button("Death Match", 1, mainMenuScale, menuMenuWidth, True, "deathmatch", False),
    menu.Button("Options", 1, mainMenuScale, menuMenuWidth, True, "options", False),
    menu.Button("Exit", 1, mainMenuScale, menuMenuWidth, True, "exit", True)
]]

singleplayerMenuScale = 1
singleplayerMenuWidth = 9
singleplayerMenuValueWidth = 3

# "_values" = [[display name, id] value]
gameLevel = [
    ["1", 1],
    ["2", 2],
    ["3", 4],
    ["4", 4],
    ["5", 5],
    ["6", 6],
    ["7", 7],
    ["8", 8],
    ["9", 9],
    ["10", 10],
    ["11", 11],
    ["12", 12],
    ["13", 13],
    ["14", 14],
    ["15", 15],
    ["16", 16],
    ["17", 17],
    ["18", 18]
]

# "singleplayerMenuItemList" = [[vertical menu, menu items ...] menu areas]
singleplayerMenuItemList = [[
    True,
    menu.SelectBoxVertical("Level", gameLevel, 1, singleplayerMenuScale, singleplayerMenuValueWidth, True, singleplayerMenuWidth - singleplayerMenuValueWidth),
    menu.CheckBox("Items", False, 1, singleplayerMenuScale, singleplayerMenuValueWidth, True, singleplayerMenuWidth - singleplayerMenuValueWidth)
],
[
    False,
    menu.Button("Back", 1, singleplayerMenuScale, singleplayerMenuWidth / 2, True, "back", True),
    menu.Button("Start", 1, singleplayerMenuScale, singleplayerMenuWidth / 2, True, "start", True)
]]

mainMenu = menu.Menu(int((windowWidth - (menuMenuWidth + 1) * mainMenuScale) / 2), int((windowHeight - 15 * mainMenuScale) / 2), menuMenuWidth + 1, 15, mainMenuScale, mainMenuItemList, screen)
singleplayerMenu = menu.Menu(int((windowWidth - (singleplayerMenuWidth + 1) * singleplayerMenuScale) / 2), int((windowHeight - 12 * singleplayerMenuScale) / 2), singleplayerMenuWidth + 1, 13, singleplayerMenuScale, singleplayerMenuItemList, screen)

#===========[ Main-Loop - Begin ]=========================
clock = pygame.time.Clock()
exitGame = False
menuItem = "none"
while not exitGame:
    for event in pygame.event.get():
        # exit application
        if event.type == pygame.QUIT:
            exitGame = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exitGame = True

        menuItem = mainMenu.updateInput(event)

    screen.fill(color=configs.clBlack)  # "clear" the screen
    mainMenu.drawMenu()
    pygame.display.flip()  # update screen

    if menuItem == "singleplayer":
        backToMainMenu = False
        while not backToMainMenu and not exitGame:
            for event in pygame.event.get():
                # exit application
                if event.type == pygame.QUIT:
                    exitGame = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menuItem = "none"
                        backToMainMenu = True

                menuItem = singleplayerMenu.updateInput(event)

            screen.fill(color=configs.clBlack)  # "clear" the screen
            singleplayerMenu.drawMenu()
            pygame.display.flip()  # update screen

            if menuItem == "start":
                myGame = gamemode.SinglePlayer(screen, 1)
                exitGame = myGame.run(clock, windowWidth, windowHeight)
                backToMainMenu = True
            elif menuItem == "back":
                menuItem = "none"
                backToMainMenu = True

        menuItem = "none"
        singleplayerMenu.reset()
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