improvedNodesVisited = 0

def NQueens(n):
    
    column, posDiag, negDiag = set(), set(), set()
    finalBoard = []
    board = [[0] * n for i in range(n)]
    global improvedNodesVisited
    improvedNodesVisited = 0
    def backtrack(row):
        global improvedNodesVisited
        if row == n:
            copy = [[x for x in row] for row in board]
            finalBoard.append(copy)
            return 
        for col in range(n):
            if col in column or (row + col) in posDiag or (row - col) in negDiag: 
                improvedNodesVisited += 1
                continue 
            else:
                column.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)
                board[row][col] = 1
                backtrack(row + 1)
                column.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)
                board[row][col] = 0
    backtrack(0)
    return finalBoard, improvedNodesVisited