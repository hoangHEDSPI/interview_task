class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        encoded_grid = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row_encoded = '(' + str(board[i][j]) + ')' + str(i)
                    column_encoded = str(j) + '(' + str(board[i][j]) + ')'
                    sub_grid_encoded = str(i//3) + '(' + str(board[i][j]) + ')' + str(j//3)
                    if encoded_grid.get(row_encoded) or encoded_grid.get(column_encoded) or encoded_grid.get(sub_grid_encoded):
                        return False
                    encoded_grid[row_encoded] = True
                    encoded_grid[column_encoded] = True
                    encoded_grid[sub_grid_encoded] = True
        return True
