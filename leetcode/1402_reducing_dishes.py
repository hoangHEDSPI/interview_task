from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        sa_len = len(satisfaction)
        if sa_len == 1:
            return satisfaction[0] if satisfaction[0] > 0 else 0
        
        first_sum = 0
        max_res = 0
        sa_sum = [0 for _ in range(sa_len + 1)]
        
        satisfaction.sort()
        
        # calculate the result if we start making dishes from the 
        # first dish
        for i in range(sa_len):
            first_sum += (i+1)*satisfaction[i]

        if max_res < first_sum:
            max_res = first_sum
            
        for i in range(sa_len-1, -1, -1):
            sa_sum[i] = sa_sum[i+1] + satisfaction[i]

        for i in range(sa_len):
            first_sum -= sa_sum[i]
            if max_res < first_sum:
                max_res = first_sum
        return max_res

def brilliantSolution( A):
        res = total = 0
        A.sort()
        while A and A[-1] + total > 0:
            total += A.pop()
            res += total
        return res

if __name__ == '__main__':
    satisfaction = [-1,-8,0,5,-9]
    sol = Solution()
    assert sol.maxSatisfaction(satisfaction) == 14
    satisfaction = [4,3,2]
    assert sol.maxSatisfaction(satisfaction) == 20
    satisfaction = [-1,-4,-5]
    assert sol.maxSatisfaction(satisfaction) == 0
