import os
import sys
from Telas import MenuInicial as Menu
from Telas import Jogo as Game
from Telas import Universo as Universo

#Definições Visuais da Primeira Tela
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 660



    
def main():
    # Fazendo a Tela e inicializando o Relógio
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Resta Um')
    clock = pygame.time.Clock()


    while True:
        clock.tick(60)
        comando = Menu.Telas(screen).execute()
        if comando == "sair":
            sys.exit()
        elif comando == "universo":
            pass
        elif comando == "jogo":
            Game.Jogo(screen).execute()
        pygame.display.flip()


if __name__ == '__main__':
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    import pygame
    from pygame.locals import QUIT
    main()