def is_valid(x, y, board):
    if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
        return True
    return False

def solution(n, board, x, y, x_move, y_move, position):
    if position == n**2:
        return True
    
    for i in range(n):
        new_x = x + x_move[i]
        new_y = y + y_move[i]
        if is_valid(new_x, new_y, board):
            board[new_x][new_y] = position
            if solution(n, board, new_x, new_y, x_move, y_move, position + 1):
                return True
            
            board[new_x][new_y] = -1

    return False

def knights_problem_solution(n):
    board = [[-1 for i in range(n)] for i in range(n)]

    x_move = [2, 1, -1, -2, -2, -1, 1, 2]
    y_move = [1, 2, 2, 1, -1, -2, -2, -1]

    board[0][0] = 0

    position = 1

    if not solution(n, board, 0, 0, x_move, y_move, position):
        print('There is no solution for the problem')
    else:
        for i in range(n):
            for j in range(n):
                print(board[i][j], end = ' ')
            print()   

n = 8
knights_problem_solution(n)