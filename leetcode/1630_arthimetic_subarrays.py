from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for period in zip(l, r):
            subNums = sorted(nums[period[0]:period[1]+1])
            if len(subNums) == 1:
                res.append(True)
            else:
                diff = subNums[1] - subNums[0]
                i = 2
                while i < len(subNums) and (subNums[i] - subNums[i-1] == diff):
                    i += 1
                if i == len(subNums):
                    res.append(True)
                else:
                    res.append(False)
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [4,6,5,9,3,7]
    l = [0,0,2] 
    r = [2,3,5]
    assert sol.checkArithmeticSubarrays(nums, l, r) == [True, False, True]  
    nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
    l = [0,1,6,4,8,7]
    r = [4,4,9,7,9,10]
    assert sol.checkArithmeticSubarrays(nums, l, r) == [False, True, False, False, True, True]