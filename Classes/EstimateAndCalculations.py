from itertools import permutations
import random as rand 

def Estimate(n):
    # calculating full size of tree
    nVals = [i for i in range(n, 0, -1)]
    fullSizeOfStateSpaceTree = calcStateSpace(nVals)

    # calculating random estimates  
    # estimates are of the length n - I estimated for full solutions. n queens on the NxN board      
    randomVals = []
    estimate = 0
    
    for val in range(10):
        board = [[0] * n for i in range(n)]
        cols = set()
        randomNum = 0
        colsLeft = []
        randomBreak = rand.randint((n // 2), (n * 2))
        if randomBreak < n:
            pass 
        else: 
            randomBreak = n
        for i in range(0, randomBreak):
            if n - len(cols) == 0:
                break 
            if i == 0:
                colsLeft.append(n)
                randomNum = rand.randint(0, (n - 1) // 2)
                board[i][randomNum] = 1
                if randomNum == 0:
                    cols.add(0)
                    cols.add(1)
                elif randomNum > 0 and randomNum < n - 1:
                    cols.add(randomNum)
                    cols.add(randomNum - 1)
                    cols.add(randomNum + 1)
                elif randomNum == n - 1:
                    cols.add(n - 1)
                    cols.add(n - 2)
            else:
                while True:   
                    randomNum = rand.randint(0, n - 1)
                    if randomNum in cols: 
                        continue 
                    else:
                        colsLeft.append(n - len(cols))
                        board[i][randomNum] = 1

                        colsWithQueen = []
                        for j in range(i):
                            for x in range(n):
                                if board[j][x] == 1:
                                    colsWithQueen.append(x)
                        cols = cols - (cols - set(colsWithQueen))
                        if randomNum == 0:
                            cols.add(0)
                            cols.add(1)
                        elif randomNum > 0 and randomNum < n - 1:
                            cols.add(randomNum)
                            cols.add(randomNum - 1)
                            cols.add(randomNum + 1)
                        elif randomNum == n - 1:
                            cols.add(n - 1)
                            cols.add(n - 2)
                        break 
        randomVals.append(colsLeft)
    for i in randomVals:
        estimate += calcStateSpace(i)
    estimate = (estimate // len(randomVals))
    return fullSizeOfStateSpaceTree, estimate

def calcStateSpace(vals):
    toSum = []    
    for j in range(1, len(vals) + 1):
        temp = 1
        for i in range(j):
            temp *= vals[i]
        toSum.append(temp)
    return 1 + sum(toSum)

def Perms(n):
    x = [[i + 1] for i in range(n)]
    return len(list(permutations(x)))