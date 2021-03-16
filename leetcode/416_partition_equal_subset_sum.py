from typing import List

class Solution:
    def recursive(self, nums: List[int], remain: int, index: int):
        if index == len(nums):
            return False
        if remain - nums[index] == 0:
            return True
        if remain - nums[index] < 0:
            return False
        return self.recursive(nums, remain - nums[index], index + 1) or self.recursive(nums, remain, index + 1)
        
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False
        half_sum = sum_nums // 2
        nums.sort()
        return self.recursive(nums, half_sum, 0)


class DFSSolution:
    def canPartition(self, nums: List[int]) -> bool:
        s, n, memo = sum(nums), len(nums), {0: True}
        if s%2:
            return False
        nums.sort(reverse=True)
        def dfs(i, x):
            if x not in memo:
                memo[x] = False
                if x > 0:
                    for j in range(i, n):
                        if dfs(j+1, x-nums[j]):
                            memo[x] = True
                            break
            return memo[x]


class DPSolution:
    def canPartition(self, nums: List[int]) -> bool:
        target, n = sum(nums), len(nums)
        if target & 1:
            return False
        target >>= 1
        dp = [True] + [False] * target
        for x in nums:
            dp = [dp[s] or (s >= x and dp[s-x]) for s in range(target + 1)]
            if dp[target]:
                return True
        return False
            


if __name__ == '__main__':
    nums = [14,9,8,4,3,2]
    sol = Solution()
    print(sol.canPartition(nums=nums))
