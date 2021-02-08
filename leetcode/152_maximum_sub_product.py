from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod, min_prod, ans = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            x = max(nums[i], max_prod*nums[i], min_prod*nums[i])
            y = min(nums[i], min_prod*nums[i], max_prod*nums[i])
            max_prod, min_prod = x, y
            ans = max(max_prod, ans)
        return ans
            
if __name__=="__main__":
    sol = Solution()
    nums = [-3, -1, -24]
    print(sol.maxProduct(nums))