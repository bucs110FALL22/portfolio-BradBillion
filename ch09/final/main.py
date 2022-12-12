import controller
import proxy
import pygame
from colors import colorList

def main():
    pygame.init()
    screen = pygame.display.set_mode()
    screenSize = pygame.display.get_window_size()
    textFont = pygame.font.SysFont("gill sans",
                                   int(screenSize[0] * 0.05),
                                   bold=True)
    controller.Controller(pygame, proxy, colorList, textFont, screen,
                          screenSize)


main()
