import os
import pygame
import sys

class Jogo():
    def __init__(self, surface):
        self.surface = surface
    
    def execute(self):
        self.jogoDraw()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()

    def jogoDraw(self):
        self.surface.fill((255,0,0))