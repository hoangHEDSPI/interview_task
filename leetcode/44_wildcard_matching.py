class Solution:
    # This is a TLE solution
    def backtrack(self, s, p, start_s, start_p) -> bool:
        if start_s == len(s) and start_p == len(p):
            return True
        if start_p == len(p):
            return False
        if start_s == len(s):
            return p[start_p] == '*' and self.backtrack(s, p, start_s, start_p+1)
        if start_p == '*':
            return self.backtrack(s, p, start_s+1, start_p) or self.backtrack(s, p, start_s, start_p+1)
        if start_p == '?' or p[start_p]==s[start_s]:
            return self.backtrack(s, p, start_s+1, start_p+1)
        else:
            return False

    def isMatch(self, s: str, p: str) -> bool:
        return self.backtrack(s, p, 0, 0)

class DpSolution:
    # Come with Dynamic programming, a better version of the above brute-force solution
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            for j in range(len(p)+1):
                start_s, start_p = i-1, j-1
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = p[start_p] == '*' and dp[i][j-1]
                elif j == 0:
                    dp[i][j] = False
                elif p[start_p] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif s[start_s] == p[start_p] or p[start_p] == "?":
                    dp[i][j] = dp[i-1][j-1]
        return dp[len(s)][len(p)]


if __name__=="__main__":
    s = "acdcb"
    p = "a*c?b"
    solution = Solution()
    match = solution.isMatch(s, p)
    print(match)
                