import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAY_SCREEN_WIDTH = SCREEN_WIDTH - 239
PLAY_SCREEN_HEIGHT = SCREEN_HEIGHT - 39
PLAY_SCREEN_POSITION = ((SCREEN_WIDTH-PLAY_SCREEN_WIDTH)/2, (SCREEN_HEIGHT-PLAY_SCREEN_HEIGHT)/2)
SQUARE_SIZE = 78
BOX_SIZE = SQUARE_SIZE+2
BACKGROUND_COLOR = (50, 50, 50)
PIECE_COLOR = (200,200,200)

AMOUNT_OF_LINES = 7
AMOUNT_OF_COLLUMNS = 7


class Piece():
    def __init__(self, ppx, ppy, gb, index):
        self.rect = pygame.Surface((SQUARE_SIZE,SQUARE_SIZE)).get_rect(topleft=(ppx,ppy))
        self.gb = gb
        self.surface = self.gb.subsurface(self.rect)
        self.surface.fill((200,200,200))
        self.active = True
        self.index = index

    def change_bool(self):
        if (self.active == True):
            self.surface.fill((BACKGROUND_COLOR))
            self.active = False
        else:
            self.surface.fill(PIECE_COLOR)
            self.active = True
    
    def click(self, pos, list, state):
        if (self.rect.collidepoint(pos)):
           if state[0] == True:
                return [self.verify_neighboors(list), self.index]
           if state[0] == False:
                self.change_neighboors(list, state)
                return True
    
    def change_neighboors(self, list, state):
        li, lc = self.index
        if state[1][0][0] == True:
            if state[1][1][1] == lc-2:
                self.change_bool()
                list[li][lc-1].change_bool()
                list[li][lc-2].change_bool()
        if state[1][0][1] == True:
            if state[1][1][1] == lc+2:
                self.change_bool()
                list[li][lc+1].change_bool()
                list[li][lc+2].change_bool()
        if state[1][0][2] == True:
            if state[1][1][0] == li+2:
                self.change_bool()
                list[li+1][lc].change_bool()
                list[li+2][lc].change_bool()
        if state[1][0][3] == True:
            if state[1][1][0] == li-2:
                self.change_bool()
                list[li-2][lc].change_bool()
                list[li-1][lc].change_bool()
                
            
    def verify_neighboors(self, list):
        pp = [False,False,False,False]
        li, lc = self.index
        #verificação pela direita
        if lc+2 <=6:
            if (list[li][lc+1] != None and list[li][lc+2] != None):
                if (list[li][lc+2].active == False):
                    if (list[li][lc+1].active == True):
                        list[li][lc+2].selectable()
                        pp[0] = True
        #verificação pela esquerda
        if lc-2 >= 0:
            if (list[li][lc-1] != None and list[li][lc-2] != None):
                if (list[li][lc-2].active == False):
                    if (list[li][lc-1].active == True):
                        list[li][lc-2].selectable()
                        pp[1] = True
        #verificação por cima
        if li-2 >= 0:
            if (list[li-1][lc] != None and list[li-2][lc] != None):
                if (list[li-2][lc].active == False):
                    if (list[li-1][lc].active == True):
                        list[li-2][lc].selectable()
                        pp[2] = True
        #verificação por baixo
        if li+2 <= 6:
            if (list[li+1][lc] != None and list[li+2][lc] != None):
                if (list[li+2][lc].active == False):
                    if (list[li+1][lc].active == True):
                        list[li+2][lc].selectable()
                        pp[3] = True
        return pp
    
    def selectable(self):
        self.surface.fill((0,200,0))
        

        

def main():
    # Fazendo a Tela e inicializando o Relógio
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('O jogo da vida')
    clock = pygame.time.Clock()
    num_of_cycles = 0

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BACKGROUND_COLOR)
    game_box = background.subsurface((PLAY_SCREEN_POSITION),
                                     (PLAY_SCREEN_WIDTH,PLAY_SCREEN_HEIGHT))
    draw_horizontal_lines(game_box)
    draw_vertical_lines(game_box)
    l_list = populate_list(game_box)
    l_list[3][3].change_bool()
    game_state = [True, []]
    

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == MOUSEBUTTONDOWN:
                px, py = event.pos
                apx, apy = PLAY_SCREEN_POSITION
                if game_box.get_rect(topleft = PLAY_SCREEN_POSITION).collidepoint(px,py):
                    for line in l_list:
                        if line == None:
                                continue
                        for collumn in line:
                            if collumn == None:
                                continue
                            if game_state[0] == True:
                                if(collumn.click((px-apx,py-apy), l_list, game_state) != None):
                                    t_list = collumn.click((px-apx,py-apy), l_list, game_state)
                                    if t_list[0].count(True) >= 1:
                                        game_state[0] = False
                                        game_state[1] = t_list
                                        continue
                            if game_state[0] == False:
                                if(collumn.click((px-apx,py-apy), l_list, game_state) != None):
                                    collumn.click((px-apx,py-apy), l_list, game_state) 
                                    game_state[0] = collumn.click((px-apx,py-apy), l_list, game_state) 
                                


        screen.blit(background, (0, 0))
        pygame.display.flip()

def draw_horizontal_lines(background):
     width_incre = 0
     while width_incre <= PLAY_SCREEN_WIDTH:
        if (width_incre < PLAY_SCREEN_WIDTH//7*2 or width_incre > PLAY_SCREEN_WIDTH//7*5):
            pygame.draw.lines(background, (180, 180, 180), True,
                          ((width_incre,PLAY_SCREEN_HEIGHT//7*2),
                           (width_incre, PLAY_SCREEN_HEIGHT//7*5)))
        else:
            pygame.draw.lines(background, (180, 180, 180), True,
                          ((width_incre,0),
                           (width_incre, PLAY_SCREEN_HEIGHT)))
        width_incre += BOX_SIZE

def draw_vertical_lines(background):
    height_incre = 0
    while height_incre <= PLAY_SCREEN_HEIGHT:
        if (height_incre < PLAY_SCREEN_HEIGHT//7*2 or height_incre > PLAY_SCREEN_HEIGHT//7*5):
            pygame.draw.lines(background, (180, 180, 180), True,
                            ((PLAY_SCREEN_WIDTH//7*2, height_incre),
                            (PLAY_SCREEN_WIDTH//7*5, height_incre)))
        else:
            pygame.draw.lines(background, (180, 180, 180), True,
                            ((0, height_incre),
                            (PLAY_SCREEN_WIDTH, height_incre)))
        height_incre += BOX_SIZE

def populate_list(background):
    px, py = 1, 1
    l_list = []
    c_list = []
    for line in range(AMOUNT_OF_LINES):
        for unid in range(AMOUNT_OF_COLLUMNS):
            if (py > PLAY_SCREEN_HEIGHT//7*2 and py < PLAY_SCREEN_HEIGHT//7*5):
                piece = Piece(px, py, background,(line, unid))
            else:
                if (px > PLAY_SCREEN_WIDTH//7*2 and px < PLAY_SCREEN_WIDTH//7*5):
                    piece = Piece(px, py, background, (line, unid))
                else:
                    if px <= PLAY_SCREEN_WIDTH:
                        px += BOX_SIZE
                    c_list.append(None)
                    continue
            c_list.append(piece)
            if px <= PLAY_SCREEN_WIDTH:
                px += BOX_SIZE
        else:
            l_list.append(c_list)
            c_list = []
        px = 1
        py += BOX_SIZE
    return l_list

if __name__ == '__main__':
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    import pygame
    from pygame.locals import QUIT, MOUSEBUTTONDOWN

    main()