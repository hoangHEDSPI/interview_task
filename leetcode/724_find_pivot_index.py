class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if sum(nums[1:]) == 0:
            return 0
        sumNums = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            if leftSum == sumNums - leftSum - nums[i]:
                return i
            leftSum += nums[i]
        return -1
      
