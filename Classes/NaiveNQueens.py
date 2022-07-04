naiveNodesVisited = 0 

def NaiveNQueens(n):
    
    finalBoard = []
    board = [[0] * n for i in range(n)]
    global naiveNodesVisited
    naiveNodesVisited = 0
    def place(row, col):
        global naiveNodesVisited
        (i, j), (x, y) = (row, col), (row, col)
        for a in range(row):
            naiveNodesVisited += 1
            if board[a][col] == 1: return False 
        while i >= 0 and j >= 0:
            naiveNodesVisited += 1
            if board[i][j] == 1: return False 
            i -= 1
            j -= 1
        while x >= 0 and y < len(board):
            naiveNodesVisited += 1
            if board[x][y] == 1: return False 
            x -= 1
            y += 1
        return True 

    def backtrack(board, row):
        if row == len(board): 
            copy = [[x for x in row] for row in board]
            finalBoard.append(copy)
        for i in range(n):
            if place(row, i) == True: 
                board[row][i] = 1    
                backtrack(board, row + 1)
                board[row][i] = 0
    backtrack(board, 0)
    return finalBoard, naiveNodesVisited