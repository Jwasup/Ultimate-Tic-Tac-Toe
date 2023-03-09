import pygame
from math import trunc
import os
from time import sleep

WIDTH, HEIGHT = 675, 675
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ultimate Tic-Tac-Toe")
greenTint = pygame.image.load(os.path.join('Assets', 'greenTint.png'))
blackTint = pygame.image.load(os.path.join('Assets', 'blackTint.png'))
verticalLine1px = pygame.image.load(os.path.join('Assets', 'verticalLine1px.png'))
verticalLine2px = pygame.image.load(os.path.join('Assets', 'verticalLine2px.png'))
horizontalLine1px = pygame.image.load(os.path.join('Assets', 'horizontalLine1px.png'))
horizontalLine2px = pygame.image.load(os.path.join('Assets', 'horizontalLine2px.png'))
x = pygame.image.load(os.path.join('Assets', 'x.png'))
o = pygame.image.load(os.path.join('Assets', 'o.png'))
bigX = pygame.transform.scale(x, (225, 225))
bigO = pygame.transform.scale(o, (225, 225))
BLACK = (0, 0, 0)
FPS = 60

def printBoard(board, masterBoard, allowedBoards):
    WIN.fill(BLACK)
    for i in range(3):
        for j in range(3):
            if (j + 3 * i) in allowedBoards:
                WIN.blit(greenTint, (225 * j, 225 * i))
    for i in range(1, 9):
        WIN.blit(verticalLine1px, (75 * i, 0))
        WIN.blit(horizontalLine1px, (0, 75 * i))
    for i in range(9):
        for j in range(3):
            for k in range(3):
                if board[i][j][k] == 'X':
                    WIN.blit(x, (75 * (k + 3 * (i % 3)), 75 * (j + 3 * trunc(i / 3))))
                elif board[i][j][k] == 'O':
                    WIN.blit(o, (75 * (k + 3 * (i % 3)), 75 * (j + 3 * trunc(i / 3))))
    for i in range(3):
        for j in range(3):
            if masterBoard[i][j] == 'X':
                WIN.blit(blackTint, (225 * j, 225 * i))
                WIN.blit(bigX, (225 * j, 225 * i))
            elif masterBoard[i][j] == 'O':
                WIN.blit(blackTint, (225 * j, 225 * i))
                WIN.blit(bigO, (225 * j, 225 * i))
    for i in range(1, 9):
        if i % 3 == 0:
            WIN.blit(verticalLine2px, (75 * i, 0))
            WIN.blit(horizontalLine2px, (0, 75 * i))
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    board = [[['', '', ''], ['', '', ''], ['', '', '']] for i in range(9)]
    print(len(board))
    currentMove = 'X'
    nextMove = 'O'
    allowedBoards = range(9)
    masterBoard = [['']*3 for i in range(3)]
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                mouseX = trunc(mouseX / 75)
                mouseY = trunc(mouseY / 75)
                miniBoard = trunc(mouseX / 3) + 3 * trunc(mouseY / 3)
                print(str(miniBoard) + ' ' + str(mouseY) + ' ' + str(mouseX))
                mouseX = mouseX % 3
                mouseY = mouseY % 3
                if board[miniBoard][mouseY][mouseX] == '' and miniBoard in allowedBoards:
                    board[miniBoard][mouseY][mouseX] = currentMove
                    if masterBoard[mouseY][mouseX] == '':
                        allowedBoards = [3 * mouseY + mouseX]
                    else:
                        for i in range(9):
                            if masterBoard[trunc(i / 3)][i % 3] == '':
                                allowedBoards += [i]
                    for i in range(3):
                        if board[miniBoard][i][0] == board[miniBoard][i][1] == board[miniBoard][i][2] == currentMove or board[miniBoard][0][i] == board[miniBoard][1][i] == board[miniBoard][2][i] == currentMove or board[miniBoard][0][0] == board[miniBoard][1][1] == board[miniBoard][2][2] == currentMove or board[miniBoard][0][2] == board[miniBoard][1][1] == board[miniBoard][2][0] == currentMove:
                            masterBoard[trunc(miniBoard / 3)][miniBoard % 3] = currentMove
                            for i in range(3):
                                for j in range(3):
                                    board[miniBoard][i][j] = ''
                            for i in range(3):
                                for j in range(3):
                                    if masterBoard[i][0] == masterBoard[i][1] == masterBoard[i][2] == currentMove or masterBoard[0][i] == masterBoard[1][i] == masterBoard[2][i] == currentMove or masterBoard[0][0] == masterBoard[1][1] == masterBoard[2][2] == currentMove or masterBoard[0][2] == masterBoard[1][1] == masterBoard[2][0] == currentMove:
                                        winner = currentMove
                                        run = False
                    print(board)
                    currentMove, nextMove = nextMove, currentMove
        printBoard(board, masterBoard, allowedBoards)        
    sleep(1)
    
if __name__ == '__main__':
    main()