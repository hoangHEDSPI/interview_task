from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # Handle corner cases
        dp[0][0] = grid[0][0]
        if m == 1 and n > 1:
            for i in range(1, n):
                dp[0][i] = dp[0][i-1] + grid[0][i]
            
        elif n == 1 and m > 1:
            for i in range(1, m):
                dp[i][0] = dp[i-1][0] + grid[i][0]

        elif n > 1 and m > 1:
            for i in range(1, n):
                dp[0][i] = dp[0][i-1] + grid[0][i]
            for i in range(1, m):
                dp[i][0] = dp[i-1][0] + grid[i][0]
            for i in range(1, m):
                for j in range(1,n):
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]

if __name__=="__main__":
    solution = Solution()
    grid = [[1,2,3],[4,5,6]]
    print(solution.minPathSum(grid=grid))