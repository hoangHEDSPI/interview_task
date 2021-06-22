class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        checked_row = {}
        checked_column = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    checked_row[i] = True
                    checked_column[j] = True
        for i in list(checked_row.keys()):
            matrix[i] = [0 for _ in range(len(matrix[0]))]
        for j in list(checked_column.keys()):
            for i in range(len(matrix)):
                matrix[i][j] = 0
