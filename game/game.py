import pygame
import sys
import random
import time

# 定義棋盤大小和格子大小
BOARD_SIZE = 15
CELL_SIZE = 40
WINDOW_SIZE = BOARD_SIZE * CELL_SIZE

# 定義顏色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# 初始化pygame
pygame.init()

# 建立視窗
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

# 建立棋盤
board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# 玩家的顏色
player = GREEN

TIME_LIMIT = 1.0

def iterative_deepening(board, depth, alpha, beta, isMaximizing):
    start_time = time.time()
    bestMove = {'score': -2, 'position': None} if isMaximizing else {'score': 2, 'position': None}

    for d in range(1, depth + 1):
        move = minimax(board, d, alpha, beta, isMaximizing)
        if time.time() - start_time > TIME_LIMIT:
            break
        bestMove = move

    return bestMove

def draw_board():
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            pygame.draw.rect(screen, WHITE, pygame.Rect(i*CELL_SIZE, j*CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
            if board[i][j] != 0:
                pygame.draw.circle(screen, board[i][j], (i*CELL_SIZE+CELL_SIZE//2, j*CELL_SIZE+CELL_SIZE//2), CELL_SIZE//2-5)

def check_win():
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] != 0:
                # 檢查行
                if i < BOARD_SIZE - 4 and all(board[i+k][j] == board[i][j] for k in range(5)):
                    return True
                # 檢查列
                if j < BOARD_SIZE - 4 and all(board[i][j+k] == board[i][j] for k in range(5)):
                    return True
                # 檢查對角線
                if i < BOARD_SIZE - 4 and j < BOARD_SIZE - 4 and all(board[i+k][j+k] == board[i][j] for k in range(5)):
                    return True
    return False

def minimax(board, depth, alpha, beta, isMaximizing):
    if check_win():
        if isMaximizing:
            return {'score': -1, 'position': None}
        else:
            return {'score': 1, 'position': None}

    if depth == 0:
        return {'score': 0, 'position': None}

    bestMove = {'score': -2, 'position': None} if isMaximizing else {'score': 2, 'position': None}

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 0:
                board[i][j] = GREEN if isMaximizing else WHITE
                move = minimax(board, depth - 1, alpha, beta, not isMaximizing)
                board[i][j] = 0
                move['position'] = (i, j)

                if isMaximizing:
                    if move['score'] > bestMove['score']:
                        bestMove = move
                    alpha = max(alpha, bestMove['score'])
                    if beta <= alpha:
                        return bestMove
                else:
                    if move['score'] < bestMove['score']:
                        bestMove = move
                    beta = min(beta, bestMove['score'])
                    if beta <= alpha:
                        return bestMove

    return bestMove

# ...

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            i, j = x // CELL_SIZE, y // CELL_SIZE
            if board[i][j] == 0:
                board[i][j] = player
                if check_win():
                    print("Player wins!")
                    pygame.quit()
                    sys.exit()
                player = WHITE if player == GREEN else GREEN

                # 電腦使用迭代深化的minimax演算法選擇一個空格下棋，深度設為3
                move = iterative_deepening(board, 10, float('-inf'), float('inf'), True)
                if move['position'] is not None:
                    i, j = move['position']
                    board[i][j] = player
                    if check_win():
                        print("Computer wins!")
                        pygame.quit()
                        sys.exit()
                    player = GREEN if player == WHITE else WHITE

    screen.fill((0, 0, 0))
    draw_board()
    pygame.display.flip()