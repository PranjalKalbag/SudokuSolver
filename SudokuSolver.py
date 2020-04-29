import numpy as np
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9],]



def solve(grid): 
    emp = empty(grid)
    if not emp:
         return True
    else:
        row, col = emp
    for x in range (1,10):
        if possible(row, col, x, grid):
            grid[row][col] = x
        if solve(grid):
            return True
        
        grid[row][col] = 0
    return False

def possible(x,y,n, grid):
     for i in range(0,9):
          if grid[x][i] == n and y!=i: 
               return False
          if grid[i][y] == n and x!=i:
               return False
     x0=(x//3)*3
     y0=(y//3)*3
     for i in range(y0*3,y0*3+3):
          for j in range(x0*3,x0*3+3):
               if grid[i][j] == n:
                    return False
     return True
 
    
def printer(grid):
    print(np.matrix(grid))

def empty(grid):
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                return(x,y)


printer(grid)
solve(grid)
print("Solved Sudoku is:")
printer(grid)
