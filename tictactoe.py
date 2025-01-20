import pygame, sys
import numpy as np

pygame.init()
WIDTH=600
HEIGHT=600
LINE_WIDTH=15
BOARD_ROWS=3
BOARD_COLS=3
RADIUS=60
CIRC_WIDTH=15
X_WIDTH= 25
SPACE=55

BG_COLOR=(30,200,200)
RED=(255,0,0)
GRAY=(50,150,150)
CIRC_COLOR=(200,200,200)
X_COLOR=(70,70,70)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

#board
board= np.zeros((BOARD_ROWS, BOARD_COLS))
#print(board)

def mark_square(row, col, player):
     board[row][col] = player

def available_square(row, col):
    return board [row][col] == 0

def full_board():
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            if board[i][j]==0: #found an empty square
                return False
    return True

#winner
def winner(player):
    #vert win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            vert_line(col, player)
            return True
    #horz win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player  and board[row][2] == player:
            horz_line(row, player)
            return True
    #asc diag win check
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        asc_diag_line(player)
        return True
    #des diag win check
    if board[0][0]== player and board[1][1] == player and board[2][2] == player:
            des_diag_line(player)
            return True
    return False #no winner
  
#drawing lines
def vert_line(col, player):
    posX = col * 200 + 100
    if player == 1:
        color = CIRC_COLOR
    elif player == 2:
        color = X_COLOR
    pygame.draw.line(screen, color, (posX, 100), (posX, 500), LINE_WIDTH)
    
def horz_line(row, player):
    posY = row * 200 + 100
    if player == 1:
        color = CIRC_COLOR
    elif player == 2:
        color = X_COLOR
    pygame.draw.line(screen, color, (20, posY), (580, posY), LINE_WIDTH)
    
def asc_diag_line(player):
    if player == 1:
        color = CIRC_COLOR
    elif player == 2:
        color = X_COLOR
    pygame.draw.line(screen, color, (20, 580), (580, 20), LINE_WIDTH)

def des_diag_line(player):
    if player == 1:
        color = CIRC_COLOR
    elif player == 2:
        color = X_COLOR
    pygame.draw.line(screen, color, (20, 20), (580, 580), LINE_WIDTH)

def restart():
    screen.fill(BG_COLOR)
    draw_line()
    game_over = False
    player = 1
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            board[i][j] = 0
#drawing X,O
def draw_figures():
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            if board[i][j] == 1:
                pygame.draw.circle(screen, CIRC_COLOR, (int(j * 200 + 100), int(i * 200 + 100)), RADIUS, CIRC_WIDTH)
            elif board[i][j] == 2:
                pygame.draw.line(screen, X_COLOR, (j * 200 + SPACE, i * 200 + 200 - SPACE), (j * 200 + 200 - SPACE, i * 200 + SPACE), X_WIDTH)
                pygame.draw.line(screen, X_COLOR, (j * 200 + SPACE, i * 200 +  SPACE), (j * 200 + 200 - SPACE, i * 200 +200 - SPACE), X_WIDTH)
       
#drawing  board lines
def draw_line():
    #horizontal lines
    pygame.draw.line(screen, GRAY,(30,210), (570,210), LINE_WIDTH)
    pygame.draw.line(screen, GRAY,(30,390), (570,390), LINE_WIDTH)
    #vertical lines
    pygame.draw.line(screen, GRAY,(210,30), (210,570), LINE_WIDTH)
    pygame.draw.line(screen, GRAY,(390,30), (390,570), LINE_WIDTH)

draw_line()

player = 1
game_over = False
#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over: #cheking if you are clicking on screen
            
            mouseX = event.pos[0] #x
            mouseY = event.pos[1] #Y
            
            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)
            
            print(clicked_row)
            print(clicked_col)
            
            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if winner(player):
                        game_over = True
                    player = 2
                    
                elif player ==2:
                    mark_square(clicked_row, clicked_col, 2)
                    if winner(player):
                        game_over = True
                    player = 1
            draw_figures()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_over = False
                restart()
                
    pygame.display.update()

    #yfn