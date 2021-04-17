from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pass

if __name__ == '__name__':
    nums = [1,1,1,2,2,3], k = 2
    sol = Solution()
    assert sol.topKFrequent(nums, k) == [1,2]
    nums = [1], k = 1
    assert sol.topKFrequent(nums, k) == [1]