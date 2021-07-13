class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[len(nums) - 1] > nums[len(nums) - 2]:
            return len(nums) - 1
        l, r = 1, len(nums) - 2
        while l <= r:
            if nums[l] > nums[l-1] and nums[l] > nums[l+1]:
                return l
            else:
                l += 1
            if nums[r] > nums[r+1] and nums[r] > nums[r-1]:
                return r
            else:
                r -= 1
                
