from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # A simple DP solution with O(len(s)^2)
        dp = [True] + [False] * len(s)
        for i in range(1, len(s)+1):
            for word in wordDict:
                if s[:i].endswith(word):
                    dp[i] |= dp[i-len(word)]
        return dp[-1]

if __name__=="__main__":
    s = "applepenapples"
    wordDict = ["apple","pen"]
    solution = Solution()
    print(solution.wordBreak(s, wordDict))
