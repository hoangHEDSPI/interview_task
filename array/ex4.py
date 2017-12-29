from itertools import product

def sudoku2(grid):
    for i in range(len(grid[0])):
        for j in range(len(grid[0])-1):
            for k in range(j+1,len(grid[0])):
                if (grid[i][j] == grid[i][k] and grid[i][k] != '.'):
                    return False
    for i in range(len(grid[0])):
        for j in range(len(grid[0])-1):
            for k in range(j+1,len(grid[0])):
                if (grid[j][i] == grid[k][i] and grid[k][i] != '.'):
                    return False
    sub_grid = []

    return True

a = [[1,2,3], [1,5,6], [7,8,9]]
print sudoku2(a),'\n'