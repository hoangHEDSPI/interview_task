from math import sqrt
from typing import List

class Solution:
    @staticmethod
    def isSquare(num: int) -> bool:
        return True if int(sqrt(num)) ** 2 == num else False
    
    @staticmethod
    def backtrack(A: List[int], squareful: List[int], res: List[List[int]]) -> int:
        if not A:
            res.append(squareful)
        for i in range(len(A)):
            if i > 0 and A[i] == A[i-1]:
                continue
            if squareful and not Solution.isSquare(squareful[-1]+A[i]):
                continue # backtracking without going further 
            Solution.backtrack(A[:i]+A[i+1:], squareful+[A[i]], res)
        
    def numSquarefulPerms(self, A: List[int]) -> int:
        A.sort()
        res = []
        Solution.backtrack(A, [], res)
        return len(res)

if __name__ == '__main__':
    sol = Solution()
    A = [1,17,8]
    assert sol.numSquarefulPerms(A) == 2

