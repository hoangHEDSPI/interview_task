from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounter = Counter(nums)
        res = []
        sortedNumCounter = {k:v for k, v in sorted(numCounter.items(), key=lambda item: item[1], reverse=True)}
        i = 0
        for num in sortedNumCounter:
            res.append(num)
            i += 1
            if i == k:
                break
        return res

if __name__ == '__name__':
    nums = [1,1,1,2,2,3], k = 2
    sol = Solution()
    assert sol.topKFrequent(nums, k) == [1,2]
    nums = [1], k = 1
    assert sol.topKFrequent(nums, k) == [1]