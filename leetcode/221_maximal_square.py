from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) < 1:
            return 0
        num_cols = len(matrix[0])
        num_rows = len(matrix)
        dp = [[0]*(num_cols+1) for _ in range(num_rows+1)]
        max_side = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if matrix[i][j] == "1":
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i][j], dp[i+1][j]) + 1
                    max_side = max(max_side, dp[i+1][j+1])
        return max_side * max_side