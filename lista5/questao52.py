def collecting_robot(board, n, m):
    path = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(None)
        path.append(row)
    
    path[0][0] = board[0][0]
    
    for j in range(1, m):
        path[0][j] = path[0][j - 1] + board[0][j]
    for i in range(1, n):
        path[i][0] = path[i - 1][0] + board[i][0]
        for j in range (1, m):
            path[i][j] = max(path[i - 1][j], path[i][j-1]) + board[i][j]

    print('Path:', path)
    return path[n - 1][m - 1]


board = [[0, 0, 0, 0, 1, 0],
             [0, 1, 0, 1, 0, 0],
             [0, 0, 0, 1, 0, 1],
             [0, 0, 1, 0, 0, 1],
             [1, 0, 0, 0, 1, 0]    
        ]
print('Maximum:', collecting_robot(board, len(board), len(board[0])))