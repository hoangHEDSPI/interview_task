from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        longest_streak = 0
        num_set = set(nums)
        
        for num in num_set:
            if num-1 not in num_set:
                current_num = num
                current_streak = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak

if __name__=="__main__":
    sol = Solution()
    nums = [100,4,200,1,3,2]
    print(sol.longestConsecutive(nums=nums))
