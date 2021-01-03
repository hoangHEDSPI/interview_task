class Solution:
    def climbStairs(self, n: int) -> int:
        # DP solution
        if n <= 2:
            return n
        
        # if n >= 3
        dp = [0 for _ in range(n+1)]
        # dp[0] = 0
        # dp[1] = 1 -> there is ony one way to take step to 1 (1)
        # dp[2] = 2 -> there is two way to take step to 2 (1->1 or 2)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# Fibonacci solution / faster than DP solution
class FibonacciSolution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        # if n >= 3
        
        first, second = 1, 2
        
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
        return second

if __name__=="__main__":
    n = 3
    solution = Solution()
    print(solution.climbStairs(3))