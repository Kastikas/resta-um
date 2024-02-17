import os


#Definições Visuais da Primeira Tela
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


    
def main():
    # Fazendo a Tela e inicializando o Relógio
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Resta Um')
    clock = pygame.time.Clock()
    tela_atual = "Titulo"

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BACKGROUND_COLOR)

    tituloDraw(background)
           

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tela_atual == "Titulo":
                    mouse_pos = pygame.mouse.get_pos()
                    
            
            
        # No final tudo, sendo renderizado novamente, por segurança.
        screen.blit(background, (0, 0))
        pygame.display.flip()


def tituloDraw(background):
    #Criando a Logo e Opções
    rect_titulo = pygame.Rect(TITULO_POSITION, TITULO_SIZE)
    pygame.draw.rect(background, TITULO_BACKGROUND_COLOR, rect_titulo)

    for  ite, color in enumerate(TITULO_BUTTON_COLORS):
            botao_opcao = background.subsurface(
                 (TITULO_BUTTON_LEFT_P,
                  TITULO_BUTTON_TOP_P-TITULO_BUTTON_OFFSET*ite),
                  TITULO_BUTTON_SIZE
                  )
            botao_opcao.fill(color)



if __name__ == '__main__':
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    import pygame
    from pygame.locals import QUIT
    main()