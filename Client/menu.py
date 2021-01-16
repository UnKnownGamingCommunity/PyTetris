import pygame
import configs

#===========[ Menu-Button - Begin ]=======================
class Button:
    caption = ""
    fontSize = 0
    scale = 1
    maxWidth = 0
    center = False
    height = 0
    buttonID = ""
    enabled = True

    caption_font = None
    text_caption = None
    text_height = 0
    text_width = 0

    def __init__(self, _caption, _fontSize, _scale, _maxWidth, _center, _id, _enabled):
        self.caption = _caption
        self.fontSize = _fontSize
        self.scale = _scale
        self.maxWidth = _maxWidth * configs.zoom * _scale
        self.center = _center
        self.buttonID = _id
        self.enabled = _enabled

        # create font and text
        self.caption_font = pygame.font.SysFont('DejaVu Sans', int(_fontSize * configs.zoom * self.scale), True, False)
        self.text_caption = self.caption_font.render(self.caption, True, configs.clMenuTextUnselected)
        (self.text_width, self.text_height) = self.text_caption.get_size()

        self.height = self.text_height

    def draw(self, screen, x, y, selected):
        clText = configs.clMenuTextUnselected
        if not self.enabled:
            clText = configs.clMenuTextDisabled
        elif selected:
            clText = configs.clMenuTextSelected
            pygame.draw.rect(screen, color=configs.clMenuBackgroundSelected, rect=[x, y - int(0.35 * configs.zoom * self.scale), self.maxWidth, self.text_height + int(0.7 * configs.zoom * self.scale)])
            pygame.draw.rect(screen, color=configs.clMenuTextSelected, rect=[x, y - int(0.35 * configs.zoom * self.scale), self.maxWidth, self.text_height + int(0.7 * configs.zoom * self.scale)], width=1)
        self.text_caption = self.caption_font.render(self.caption, True, clText)
        screen.blit(self.text_caption, [x + (self.maxWidth - self.text_width) / 2, y])
#===========[ Menu-Button - End ]=========================

#===========[ Menu-Selectbox - Begin ]====================
#===========[ Menu-Selectbox - End ]======================

#===========[ Menu-Class - Begin ]========================
class Menu:
    x = 0
    y = 0
    width = 0
    height = 0
    scale = 1
    menuItems = []
    selectedArea = 0
    selectedItem = 0
    screen = None

    # set the default values for this menu
    def __init__(self, x_coord, y_coord, _width, _height, _scale, _menuItems, _screen):
        self.x = x_coord
        self.y = y_coord
        self.width = _width
        self.height = _height
        self.scale = _scale
        self.menuItems = _menuItems
        self.selectedArea = 0
        self.selectedItem = 0
        self.screen = _screen

    def newItemSelection(self, delta):
        self.selectedItem = (self.selectedItem + delta) % len(self.menuItems[self.selectedArea])
        i = 0
        while not self.menuItems[self.selectedArea][self.selectedItem].enabled and i <= len(self.menuItems[self.selectedArea]):
            self.selectedItem = (self.selectedItem + delta) % len(self.menuItems[self.selectedArea])
            i += 1

    def drawMenu(self):
        pygame.draw.rect(self.screen, color=configs.clMenuBackground, rect=[int(self.x * configs.zoom), int(self.y * configs.zoom), int(self.width * self.scale * configs.zoom), int(self.height * self.scale * configs.zoom)])
        pygame.draw.rect(self.screen, color=configs.clMenuBorder, rect=[int(self.x * configs.zoom), int(self.y * configs.zoom), int(self.width * self.scale * configs.zoom), int(self.height * self.scale * configs.zoom)], width=1)
        for area in range(len(self.menuItems)):
            yOffset = int(0.7 * configs.zoom * self.scale)
            for item in range(len(self.menuItems[area])):
                selected = False
                if (area == self.selectedArea and item == self.selectedItem):
                    selected = True
                self.menuItems[area][item].draw(self.screen, int((self.x + 0.5) * configs.zoom), int((self.y + 0.5) * configs.zoom) + yOffset, selected)
                yOffset += self.menuItems[area][item].height + int(0.7 * configs.zoom * self.scale)

    def updateInput(self):
        usedButton = "none"
        exitGame = False
        for event in pygame.event.get():
            # exit application
            if event.type == pygame.QUIT:
                exitGame = True

            # update key-events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.newItemSelection(-1)
                elif event.key == pygame.K_DOWN:
                    self.newItemSelection(1)
                elif event.key == pygame.K_RIGHT:
                    self.newItemSelection(-1)
                elif event.key == pygame.K_LEFT:
                    self.newItemSelection(1)
                elif event.key == pygame.K_TAB:
                    self.selectedArea = (self.selectedArea + 1) % len(self.menuItems)
                elif event.key == pygame.K_RETURN and isinstance(self.menuItems[self.selectedArea][self.selectedItem], Button):
                    usedButton = self.menuItems[self.selectedArea][self.selectedItem].buttonID
                elif event.key == pygame.K_ESCAPE:
                    exitGame = True
        return (usedButton, exitGame)
#===========[ Menu-Class - End ]==========================