class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        dp = []
        dp.append(nums[0])
        maxResult = dp[0]
        for i in range(1, len(nums)):
            if dp[i-1] > 0:
                dp.append(nums[i] + dp[i-1])
            else:
                dp.append(nums[i])
            maxResult = max(maxResult, dp[i])
        return maxResult