import pygame
import os

#Constantes Gerais
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 660
BACKGROUND_COLOR =  (0,0,0)


#Constantes Menu
TITULO_BACKGROUND_COLOR = (255,255,255)
TITULO_POSITION = (SCREEN_WIDTH/3, SCREEN_HEIGHT/10)
TITULO_SIZE = (SCREEN_WIDTH/3, SCREEN_HEIGHT/12)
TITULO_BUTTON_COLORS = [(245, 54, 63), (104, 99, 128),(79, 255, 100)]
TITULO_BUTTON_OFFSET = 100
TITULO_BUTTON_LEFT_P = SCREEN_WIDTH/2.5
TITULO_BUTTON_TOP_P = SCREEN_HEIGHT/1.5
TITULO_BUTTON_SIZE = (SCREEN_WIDTH/5, SCREEN_HEIGHT/10)
CODIGO_DAS_TELAS = ["sair", "universo", "jogo"]


class Telas():
    def __init__(self, surface):
        self.surface = surface
    
    def execute(self):
        botoes = self.tituloDraw()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "sair"
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, botao  in enumerate(botoes):
                        if botao.get_rect(topleft=(botao.get_offset())).collidepoint(mouse_pos):
                            return CODIGO_DAS_TELAS[i]
            pygame.display.flip()

    def tituloDraw(self):
        #Criando a Logo e Opções
        background = self.surface
        botoes_menu = []
        rect_titulo = pygame.Rect(TITULO_POSITION, TITULO_SIZE)
        pygame.draw.rect(background, TITULO_BACKGROUND_COLOR, rect_titulo)

        for  ite, color in enumerate(TITULO_BUTTON_COLORS):
                botao_opcao = background.subsurface(
                    (TITULO_BUTTON_LEFT_P,
                    TITULO_BUTTON_TOP_P-TITULO_BUTTON_OFFSET*ite),
                    TITULO_BUTTON_SIZE
                    )
                botao_opcao.fill(color)
                botoes_menu.append(botao_opcao)
        return botoes_menu
