from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        if m == 1:
            for i in range(n):
                if obstacleGrid[0][i] == 1:
                    return 0
            return 1
        if n == 1:
            for i in range(m):
                if obstacleGrid[i][0] == 1:
                    return 0
            return 1
        # If both m and n are greater than 1
        dp = [[0 for _ in range(n)] for _ in range(m)] 
        dp[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] * (1 -  obstacleGrid[i][0])
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] * (1 - obstacleGrid[0][i]) 
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) * (1 - obstacleGrid[i][j])
        return dp[-1][-1]

if __name__=="__main__":
    obstacleGrid = [[0,0],[1,1],[0,0]]
    solution = Solution()
    print(solution.uniquePathsWithObstacles(obstacleGrid=obstacleGrid))