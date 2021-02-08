from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # O(nlogk) time complexity, O(k) space complexity
        priorityQueue = nums[:k]
        heapq.heapify(priorityQueue)
        for x in nums[:k]:
            heapq.heappush(priorityQueue, x)
            heapq.heappop(priorityQueue)
        return priorityQueue[0]
