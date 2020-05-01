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



def solve(): 
    global grid
    emp = empty()
    if not emp:
        return True
    else:
        row, col = emp
    for x in range (1,10):
        if possible(row, col, x):
            grid[row][col] = x
            if solve():
                return True	  
            grid[row][col] = 0      
    return False

def possible(x,y,n):
    global grid
    for i in range(0,9):
        if grid[x][i] == n: 
            return False
    for i in range(0,9):
        if grid[i][y] == n:
            return False
    x0=((x)//3)*3
    y0=((y)//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[x0+i][y0+j] == n:
                return False
    return True
 
    
def printer():
    global grid
    print(np.matrix(grid))

def empty():
    global grid
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                return x,y
  

printer()
solve()
print("Solved Sudoku is:")
printer()
