import math
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zero = nums.count(0)
        if num_zero > 1:
            return [0 for _ in range(len(nums))]
        if num_zero == 0:
            prod_nums = math.prod(nums)
            return [(prod_nums // nums[i]) for i in range(len(nums))]
        # In case there is one zero in nums
        zero_index = 0
        zero_index_prod = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_index = i
            else:
                zero_index_prod *= nums[i]
        return [0 for _ in range(0, zero_index)] + [zero_index_prod] + [0 for _ in range(zero_index+1,len(nums))]


if __name__ == "__main__":
    nums=[-1,1,0,-3,3]
    sol = Solution()
    assert sol.productExceptSelf(nums=nums) == [0,0,9,0,0]