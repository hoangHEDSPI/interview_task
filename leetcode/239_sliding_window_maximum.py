from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # This naive solution will lead to TLE error
        # res = []
        # for i in range(0, len(nums) - k+1):
        #     res.append(max(nums[i:i+k]))
        # return res
        from collections import deque
        res = []
        q = deque()
        for i in range(len(nums)):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            if q[0] == i-k:
                q.popleft()
            # If a window has k elements, add to result
            if i >= k-1: # we need this condition because first k-1 windows have < k elements
                res.append(nums[q[0]])
        return res
        
if __name__ == '__main__':
    sol = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    assert sol.maxSlidingWindow(nums, k) == [3,3,5,5,6,7]