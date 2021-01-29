from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        zero_positions = []
        for i in range(len_nums):
            if nums[i] == 0:
                nums.append(0)
                zero_positions.append(i)
        for i in range(len(zero_positions)):
            nums.pop(zero_positions[i] - len_nums - len(zero_positions))
        print(nums)

if __name__=="__main__":
    nums = [0,1,0,3,12]
    sol = Solution()
    sol.moveZeroes(nums=nums)

