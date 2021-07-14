class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(l, r):
            if r >= l:
                mid = (l+r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return binarySearch(mid+1, r)
                else:
                    return binarySearch(l, mid-1)
            else:
                return -1
        targetIndex = binarySearch(0, len(nums)-1)
        if targetIndex == -1: 
            return [-1, -1]
        firstIndex = targetIndex
        lastIndex = targetIndex
        while firstIndex > 0 and nums[firstIndex-1] == target:
            firstIndex -= 1
        while lastIndex < len(nums)-1 and nums[lastIndex+1] == target:
            lastIndex += 1
        return [firstIndex, lastIndex]
    
