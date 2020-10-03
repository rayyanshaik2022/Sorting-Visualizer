import pygame
from settings import *

class Button(pygame.sprite.Sprite):
    
    def __init__(self, rect, colors, group, return_value, text=None):

        self.groups = group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.colors = colors
        self.color = self.colors[0]
        self.return_value = return_value
        self.text = text

        self.clicked = False

        self.image = pygame.Surface((rect[2], rect[3]))
        self.recolor()
        self.rect = self.image.get_rect()
        self.rect.x = rect[0]
        self.rect.y = rect[1]

    def recolor(self):
        self.image.fill((self.color))