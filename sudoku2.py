def sudoku2(grid):
    for row in range(9):
        if validRow(grid,row) ==False:
            return False
    for col in range(9):
        if validCol(grid,col) == False:
            return False
          
    for row in range(0,9,3):
        for col in range(0,9,3):
            if validBox(grid,row,col) ==False:
                return False
    return True  
    
def validRow(grid,row):
    checkList = []
    for i in range(9):
        if grid[row][i] in checkList:
            return False
        elif grid[row][i] !='.':
            checkList.append(grid[row][i])
    return True
    
def validCol(grid,col):
    checkList =[]
    for i in range(9):
        if grid[i][col] in checkList:
            return False
        elif grid[i][col] !='.':
            checkList.append(grid[i][col])
    return True
    
def validBox(grid,startRow,startCol):
    checkList = []
    for row in range(3):
        for col in range(3):
            boxVal = grid[startRow+row][startCol+col]
            if boxVal in checkList:
                return False
            elif boxVal != '.':
                checkList.append(boxVal)
    return True
