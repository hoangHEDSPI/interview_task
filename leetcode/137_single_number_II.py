from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # use hash table to solve this problem
        hashTable = {}
        for i in range(len(nums)):
            if nums[i] not in hashTable:
                hashTable[nums[i]] = False
            else:
                hashTable[nums[i]] = True
        for key, value in hashTable.items():
            if not value:
                return key


if __name__=="__main__":
    nums = [3,3,3,2,2,2,1,4,4,4]
    sol = Solution()
    print(sol.singleNumber(nums=nums))