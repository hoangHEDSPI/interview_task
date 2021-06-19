class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(i: int, temp_sum: int):
            if (i, temp_sum) not in cache:
                t = 0
                if i == len(nums):
                    if temp_sum == target:
                        t = 1
                else:
                    t = backtrack(i+1, temp_sum + nums[i]) + backtrack(i+1, temp_sum - nums[i])
                cache[(i, temp_sum)] = t
            return cache[(i, temp_sum)]
        cache = {}
        return backtrack(0, 0)
 
