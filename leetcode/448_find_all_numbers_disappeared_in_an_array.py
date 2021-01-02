class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return None
        orderArr = [i for i in range(1, len(nums)+1)]
        for i in range(len(nums)):
            if orderArr[nums[i]-1]:
                orderArr[nums[i]-1] = 0
        return [orderArr[i] for i in range(len(orderArr)) if orderArr[i]]