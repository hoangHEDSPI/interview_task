class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        def findMin(target, nums):
            if not nums or len(nums) == 0:
                return -1
            if nums[len(nums) - 1] <= target:
                return target - nums[len(nums) - 1]
            if nums[0] >= target:
                return nums[0] - target
            l, r = 0, len(nums) - 1
            while l < r:
                mid = (l+r) // 2;
                if nums[mid] > target:
                    if mid > 0 and nums[mid-1] < target:
                        return min(abs(nums[mid]- target), abs(nums[mid-1] - target))
                    r = mid
                elif nums[mid] < target:
                    if mid < len(nums)-1 and nums[mid+1] > target:
                        return min(abs(nums[mid] - target), abs(nums[mid+1] - target))
                    l = mid+1
                else:
                    return 0
                    
        one, two, three = [], [], []
        for i in range(len(colors)):
            if colors[i] == 1:
                one.append(i)
            elif colors[i] == 2:
                two.append(i)
            elif colors[i] == 3:
                three.append(i)
        queryResults = []
        for (i, c) in queries:
            if c == 1:
                res = findMin(i, one)
            elif c == 2:
                res = findMin(i, two)
            elif c == 3:
                res = findMin(i, three)
            queryResults.append(res)
        return queryResults
     
