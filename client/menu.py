import pygame
import configs

spaceBetweenMenuItems = 0.7

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
        self.fontSize = int(_fontSize * configs.zoom * _scale)
        self.scale = _scale
        self.maxWidth = int(_maxWidth * configs.zoom * _scale)
        self.center = _center
        self.buttonID = _id
        self.enabled = _enabled

        # create font and text
        self.caption_font = pygame.font.SysFont('DejaVu Sans', self.fontSize, True, False)
        self.text_caption = self.caption_font.render(self.caption, True, configs.clMenuTextUnselected)
        (self.text_width, self.text_height) = self.text_caption.get_size()

        self.height = self.text_height + int(spaceBetweenMenuItems * configs.zoom * self.scale)

    def draw(self, screen, x, y, selected):
        clText = configs.clMenuTextUnselected
        if not self.enabled:
            clText = configs.clMenuTextDisabled
        elif selected:
            clText = configs.clMenuTextSelected
            pygame.draw.rect(screen, color=configs.clMenuBackgroundSelected, rect=[x, y - int(spaceBetweenMenuItems / 2 * configs.zoom * self.scale), self.maxWidth, self.height])
            pygame.draw.rect(screen, color=configs.clMenuTextSelected, rect=[x, y - int(spaceBetweenMenuItems / 2 * configs.zoom * self.scale), self.maxWidth, self.height], width=1)
        self.text_caption = self.caption_font.render(self.caption, True, clText)
        captionPosX = 0
        if self.center:
            captionPosX = (self.maxWidth - self.text_width) / 2
        screen.blit(self.text_caption, [x + captionPosX, y])
#===========[ Menu-Button - End ]=========================

#===========[ Menu-Selectbox horizontal - Begin ]=========
#===========[ Menu-Selectbox horizontal - End ]===========

#===========[ Menu-Selectbox vertical - Begin ]===========
class SelectBoxVertical:
    fontSize = 0
    scale = 1
    maxValueWidth = 0
    enabled = True
    caption = ""
    height = 0
    values = []
    selectedValue = 0
    maxCaptionWidth = 0
    maxWidth = 0
    isEdit = False
    id = ""

    caption_font = None
    value_font = None
    text_caption = None

    def __init__(self, _caption, _values, _fontSize, _scale, _maxValueWidth, _enabled, _maxCaptionWidth, _id):
        # "_values" = [[display name, id] value]
        self.caption = _caption
        self.fontSize = int(_fontSize * configs.zoom * _scale)
        self.scale = _scale
        self.maxValueWidth = _maxValueWidth * configs.zoom * _scale
        self.enabled = _enabled
        self.selectedValue = 0
        self.values = _values
        self.maxCaptionWidth = _maxCaptionWidth * configs.zoom * _scale
        self.maxWidth = self.maxCaptionWidth + self.maxValueWidth
        self.isEdit = False
        self.id = _id

        self.caption_font = pygame.font.SysFont('DejaVu Sans', self.fontSize, True, False)
        self.text_caption = self.caption_font.render(self.caption, True, configs.clMenuTextUnselected)

        self.value_font = pygame.font.SysFont('DejaVu Sans', self.fontSize, True, False)

        (text_width, self.text_height) = self.text_caption.get_size()
        self.height = self.text_height * 3 + int(spaceBetweenMenuItems * configs.zoom * self.scale) * 3

    def draw(self, screen, x, y, selected):
        textInMiddle = self.text_height + int(spaceBetweenMenuItems * configs.zoom * self.scale)

        clText = configs.clMenuTextUnselected
        if not self.enabled:
            clText = configs.clMenuTextDisabled
        elif selected:
            clText = configs.clMenuTextSelected
            if self.isEdit:
                pygame.draw.rect(screen, color=configs.clMenuBackgroundSelected, rect=[x + self.maxCaptionWidth, y + self.text_height + int(spaceBetweenMenuItems / 2 * configs.zoom * self.scale), self.maxValueWidth, textInMiddle])

        pygame.draw.rect(screen, color=clText, rect=[x + self.maxCaptionWidth, y + self.text_height + int(spaceBetweenMenuItems / 2 * configs.zoom * self.scale), self.maxValueWidth, textInMiddle], width=1)
        self.text_caption = self.caption_font.render(self.caption, True, clText)
        screen.blit(self.text_caption, [x, y + textInMiddle])

        if self.selectedValue > 0:
            outputText = self.value_font.render(self.values[self.selectedValue - 1][0], True, configs.clMenuTextUnselected)
            (xSize, ySize) = outputText.get_size()
            screen.blit(outputText, [x + self.maxCaptionWidth + (self.maxValueWidth - xSize) / 2, y + int(spaceBetweenMenuItems * configs.zoom * self.scale * 0.5)])
        if self.selectedValue < len(self.values) - 1:
            outputText = self.value_font.render(self.values[self.selectedValue + 1][0], True, configs.clMenuTextUnselected)
            (xSize, ySize) = outputText.get_size()
            screen.blit(outputText, [x + self.maxCaptionWidth + (self.maxValueWidth - xSize) / 2, y + textInMiddle + self.text_height + int(spaceBetweenMenuItems * configs.zoom * self.scale * 0.5)])


        outputText = self.value_font.render(self.values[self.selectedValue][0], True, clText)
        (xSize, ySize) = outputText.get_size()
        screen.blit(outputText, [x + self.maxCaptionWidth + (self.maxValueWidth - xSize) / 2, y + textInMiddle])

    def newItemSelection(self, delta):
        self.selectedValue = (self.selectedValue + delta) % len(self.values)

    def reset(self):
        self.selectedValue = 0
        self.isEdit = False

    def getValue(self):
        return self.values[self.selectedValue][1]
#===========[ Menu-Selectbox vertical - End ]=============

#===========[ Menu-CheckBox horizontal - Begin ]==========
class CheckBox:
    fontSize = 0
    scale = 1
    maxValueWidth = 0
    enabled = True
    caption = ""
    height = 0
    maxCaptionWidth = 0
    defaultValue = False
    value = False
    text_height = 0
    maxWidth = 0
    id = ""

    caption_font = None
    value_font = None
    text_caption = None

    def __init__(self, _caption, _defaultValue, _fontSize, _scale, _maxValueWidth, _enabled, _maxCaptionWidth, _id):
        self.fontSize = int(_fontSize * configs.zoom * _scale)
        self.scale = _scale
        self.maxValueWidth = _maxValueWidth * configs.zoom * _scale
        self.enabled = _enabled
        self.caption = _caption
        self.maxCaptionWidth = _maxCaptionWidth * configs.zoom * _scale
        self.defaultValue = _defaultValue
        self.value = _defaultValue
        self.maxWidth = self.maxCaptionWidth + self.maxValueWidth
        self.id = _id

        self.caption_font = pygame.font.SysFont('DejaVu Sans', self.fontSize, True, False)
        self.text_caption = self.caption_font.render(self.caption, True, configs.clMenuTextUnselected)

        self.value_font = pygame.font.SysFont('DejaVu Sans', self.fontSize, True, False)

        (text_width, self.text_height) = self.text_caption.get_size()
        self.height = self.text_height + int(spaceBetweenMenuItems * configs.zoom * self.scale)

    def draw(self, screen, x, y, selected):
        clText = configs.clMenuTextUnselected
        if not self.enabled:
            clText = configs.clMenuTextDisabled
        elif selected:
            clText = configs.clMenuTextSelected
            pygame.draw.rect(screen, color=configs.clMenuBackgroundSelected, rect=[x + self.maxCaptionWidth, y - int(spaceBetweenMenuItems / 2 * configs.zoom * self.scale), self.maxValueWidth, self.height])
            pygame.draw.rect(screen, color=clText, rect=[x + self.maxCaptionWidth, y - int(spaceBetweenMenuItems / 2 * configs.zoom * self.scale), self.maxValueWidth, self.height], width=1)

        self.text_caption = self.caption_font.render(self.caption, True, clText)
        screen.blit(self.text_caption, [x, y])

        text = "Off"
        clValue = configs.clChckeBoxOffUnselected
        if self.value:
            text = "On"
            if selected:
                clValue = configs.clChckeBoxOnSelected
            else:
                clValue = configs.clChckeBoxOnUnselected
        elif selected:
            clValue = configs.clChckeBoxOffSelected
        outputText = self.value_font.render(text, True, clValue)
        (xSize, ySize) = outputText.get_size()
        screen.blit(outputText, [x + self.maxCaptionWidth + (self.maxValueWidth - xSize) / 2, y])

    def toggleValue(self):
        self.value = not self.value

    def reset(self):
        self.value = self.defaultValue

    def getValue(self):
        return self.value
#===========[ Menu-CheckBox horizontal - End ]============

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
    enabled = True

    # set the default values for this menu
    def __init__(self, x_coord, y_coord, _width, _height, _scale, _menuItems, _screen):
        # "menuItems" = [[vertical menu, menu items ...] menu areas]
        self.x = x_coord
        self.y = y_coord
        self.width = int(_width * _scale)
        self.height = int(_height * _scale)
        self.scale = _scale
        self.menuItems = _menuItems
        self.selectedArea = 0
        self.selectedItem = 0
        self.screen = _screen
        self.enabled = True

        self.newItemSelection(+1)

    def newItemSelection(self, delta):
        self.selectedItem = (self.selectedItem - 1 + delta) % (len(self.menuItems[self.selectedArea]) - 1) + 1
        i = 0
        while self.selectedItem == 0 or (not self.menuItems[self.selectedArea][self.selectedItem].enabled and i <= len(self.menuItems[self.selectedArea]) - 1):
            self.selectedItem = (self.selectedItem - 1 + delta) % (len(self.menuItems[self.selectedArea]) - 1) + 1
            i += 1

    def drawMenu(self):
        if self.enabled:
            pygame.draw.rect(self.screen, color=configs.clMenuBackground, rect=[int(self.x * configs.zoom), int(self.y * configs.zoom), int(self.width * self.scale * configs.zoom), int(self.height * self.scale * configs.zoom)])
            pygame.draw.rect(self.screen, color=configs.clMenuBorder, rect=[int(self.x * configs.zoom), int(self.y * configs.zoom), int(self.width * self.scale * configs.zoom), int(self.height * self.scale * configs.zoom)], width=1)

            yOffset = 0
            for area in range(len(self.menuItems)):
                yOffset += int(spaceBetweenMenuItems * configs.zoom * self.scale)
                if area > 0:
                    yOffset += int(spaceBetweenMenuItems * configs.zoom * self.scale / 2)
                    pygame.draw.line(self.screen, color=configs.clMenuBorder, start_pos=[int(self.x * configs.zoom), int(self.y * self.scale * configs.zoom + yOffset)], end_pos=[int((self.x + self.width * self.scale) * configs.zoom), int(self.y * configs.zoom + yOffset)], width=1)
                    yOffset += int(spaceBetweenMenuItems * configs.zoom * self.scale)
                xOffset = 0
                verticalMenu = self.menuItems[area][0]
                for item in range(len(self.menuItems[area])):
                    if not isinstance(self.menuItems[area][item], bool):
                        selected = False
                        if (area == self.selectedArea and item == self.selectedItem):
                            selected = True
                        self.menuItems[area][item].draw(self.screen, int((self.x + 0.5) * configs.zoom) + xOffset, int((self.y + 0.5) * configs.zoom) + yOffset, selected)
                        if verticalMenu:
                            yOffset += self.menuItems[area][item].height
                        else:
                            xOffset += self.menuItems[area][item].maxWidth


    def updateInput(self, event):
        # update key-events
        usedButton = "none"
        if self.enabled:
            if event.type == pygame.KEYDOWN:
                if isinstance(self.menuItems[self.selectedArea][self.selectedItem], SelectBoxVertical) and self.menuItems[self.selectedArea][self.selectedItem].isEdit:
                    if event.key == pygame.K_UP:
                        self.menuItems[self.selectedArea][self.selectedItem].newItemSelection(-1)
                    elif event.key == pygame.K_DOWN:
                        self.menuItems[self.selectedArea][self.selectedItem].newItemSelection(1)
                    elif event.key == pygame.K_RETURN:
                            self.menuItems[self.selectedArea][self.selectedItem].isEdit = False
                else:
                    if event.key == pygame.K_UP:
                        self.newItemSelection(-1)
                    elif event.key == pygame.K_DOWN:
                        self.newItemSelection(1)
                    elif event.key == pygame.K_RIGHT:
                        if not isinstance(self.menuItems[self.selectedArea][self.selectedItem], SelectBoxVertical):
                            self.newItemSelection(-1)
                    elif event.key == pygame.K_LEFT:
                        if not isinstance(self.menuItems[self.selectedArea][self.selectedItem], SelectBoxVertical):
                            self.newItemSelection(1)
                    elif event.key == pygame.K_TAB:
                        self.selectedArea = (self.selectedArea + 1) % len(self.menuItems)
                        self.selectedItem = 0
                        self.newItemSelection(+1)
                    elif event.key == pygame.K_RETURN and isinstance(self.menuItems[self.selectedArea][self.selectedItem], Button):
                        usedButton = self.menuItems[self.selectedArea][self.selectedItem].buttonID
                    elif event.key == pygame.K_RETURN and isinstance(self.menuItems[self.selectedArea][self.selectedItem], SelectBoxVertical):
                        self.menuItems[self.selectedArea][self.selectedItem].isEdit = True
                    elif event.key == pygame.K_RETURN and isinstance(self.menuItems[self.selectedArea][self.selectedItem], CheckBox):
                        self.menuItems[self.selectedArea][self.selectedItem].toggleValue()
        return usedButton

    def reset(self):
        self.selectedItem = 0
        self.selectedArea = 0
        self.newItemSelection(+1)
        for area in range(len(self.menuItems)):
            for item in range(len(self.menuItems[area])):
                if not isinstance(self.menuItems[self.selectedArea][self.selectedItem], Button):
                    self.menuItems[self.selectedArea][self.selectedItem].reset()

    def getValue(self, _id):
        for area in range(len(self.menuItems)):
            for item in range(len(self.menuItems[area])):
                if not isinstance(self.menuItems[area][item], Button) and  not isinstance(self.menuItems[area][item], bool):
                    if self.menuItems[area][item].id == _id:
                        return self.menuItems[area][item].getValue()
        return None
#===========[ Menu-Class - End ]==========================