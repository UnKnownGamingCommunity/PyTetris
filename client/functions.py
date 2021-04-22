import pygame
import configs

def DrawSingleBlock(screen, xPos, yPos, _block):
    for x in range(4):
        for y in range(4):
            position = x + y * 4
            if position in _block.image():
                clBlock = configs.clWhite
                clBorder = configs.clWhite
                if not configs.multiColorBlock:
                    clBlock = configs.clActiveBlock
                    clBorder = configs.clActiveBlockBorder
                elif _block.type > len(configs.clBlockColors):
                    clBlock = configs.clBlockColors[7]
                    clBorder = configs.clBlockBorderColors[7]
                elif _block.type <= len(configs.clBlockColors):
                    clBlock = configs.clBlockColors[_block.type]
                    clBorder = configs.clBlockBorderColors[_block.type]

                pygame.draw.rect(screen, color=clBlock, rect=[xPos + x * configs.zoom, yPos + y * configs.zoom, configs.zoom, configs.zoom])
                pygame.draw.rect(screen, color=clBorder, rect=[xPos + x * configs.zoom, yPos + y * configs.zoom, configs.zoom, configs.zoom], width=1)