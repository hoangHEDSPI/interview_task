from math import log
from typing import List

"""
    DP solution: dp[i] = dp[i-offset] + 1
    offset * 2 == i => offset *= 2
"""
class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        countList = [0 for _ in range(num+1)]
        offset = 1
        for i in range(1, num+1):
            if offset << 1 == i:
                offset <<= 1
            countList[i] = countList[i - offset] + 1
        return countList
        
if __name__=="__main__":
    num = 16
    sol = Solution()
    print(sol.countBits(num))