N = 9

#Function to check if a number is safe to put in a cell
def isSafe(sudoku,row,col,num):
    #checking if same number appears in the same row
    for i in range(9):
        if sudoku[row][i]==num:
            return False
    
    #checking if same number appears in the same column
    for i in range(9):
        if sudoku[i][col] == num:
            return False
    
    #checking if same number appears in the same 3x3 Grid
    startRow = row - row%3
    startCol = col - col%3
    for i in range(3):
        for j in range(3):
            if sudoku[startRow+i][startCol+j] == num:
                return False
    
    #if None of the above conditions are satisfied
    return True

def solveSudoku(sudoku,row,col):
    #Base condition (for recurssion)
    if row ==N-1 and col == N:
        return True
    
    if col == N:
        row += 1
        col = 0

    if sudoku[row][col]>0:
        return solveSudoku(sudoku,row,col+1)
    
    for num in range(1,N+1):
        if isSafe(sudoku,row,col,num):
            sudoku[row][col] = num

            if solveSudoku(sudoku,row,col+1):
                return True
            
        sudoku[row][col] = 0

    return False

def solver(sudoku):
    if solveSudoku(sudoku,0,0):
        return sudoku
    else:
        return "No"