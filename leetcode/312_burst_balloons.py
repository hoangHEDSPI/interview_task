from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        newNums = [1] + [i for i in nums if i > 0] + [1]
        n = len(newNums)
        dp = [[0]*n for _ in range(n)]

        for k in range(2, n):
            for left in range(0, n-k):
                right = left + k
                for i in range(left+1, right):
                    dp[left][right] = max(dp[left][right],
                    newNums[left] * newNums[i] * newNums[right] + dp[left][i] + dp[i][right])
        return dp[0][n-1]