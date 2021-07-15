class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        converted_1d_matrix = []
        for i in range(len(matrix)-1, -1, -1):
            converted_1d_matrix.extend(matrix[i])
        i = 0
        while i < len(matrix):
            row = [converted_1d_matrix[j] for j in range(i, len(converted_1d_matrix), len(matrix))]
            # print(row)
            matrix[i] = row
            i += 1
            
