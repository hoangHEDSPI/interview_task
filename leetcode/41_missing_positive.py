from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1
        if len(nums) == 1:
            if nums[0] == 1:
                return 2
            return 1
        max_num = max(nums)
        if max_num <= 0:
            return 1
        # Form a dictionary to save positve element of nums
        positive_dict = {}
        for i in nums:
            positive_dict[i] = True
        for i in range(1, max_num + 1):
            if i not in positive_dict:
                return i
        return max_num+1


if __name__=="__main__":
    nums = [0,2,3,4]
    sol = Solution()
    print(sol.firstMissingPositive(nums))
        