class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        import bisect
        def lengthOfLIS(nums):
            dp = [10**10] * (len(nums) + 1)
            for elem in nums: 
                dp[bisect.bisect_left(dp, elem)] = elem  
            return dp.index(10**10)
        
        n = len(nums)
        maxIncresedLength = 0
        for i in range(1, n-1):
            left = nums[:i+1]
            right = nums[i:len(nums)][::-1]
            a, b = lengthOfLIS(left), lengthOfLIS(right)
            if a>=2 and b>=2:
                maxIncresedLength = max(maxIncresedLength, a+b-1)
        return n-maxIncresedLength
      
