# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        lenMtArr = mountain_arr.length()
        
        # Binary search to find the peak
        def binarySearchPeak(l, r):
            nonlocal lenMtArr
            # Because there is alway a peak value so we do not need to handle None cases
            mid = (l + r) // 2
            val = mountain_arr.get(mid)
            if mid == 0 or mid == lenMtArr - 1:
                return mid
            
            prev_val = mountain_arr.get(mid-1)
            next_val = mountain_arr.get(mid+1)
            if prev_val < val and next_val < val:
                # return the index of the peak
                return mid
            elif prev_val > val:
                return binarySearchPeak(l, mid-1)
            elif next_val > val:
                return binarySearchPeak(mid+1, r)
        
        def binarySearchLeft(l, r):
            if r >= l:
                mid = (l+r) // 2
                val = mountain_arr.get(mid)
                if val == target:
                    return mid
                elif val > target:
                    return binarySearchLeft(l, mid-1)
                elif val < target:
                    return binarySearchLeft(mid+1, r)
            else:
                return -1
        
        def binarySearchRight(l, r):
            if r >= l:
                mid = (l+r) // 2
                val = mountain_arr.get(mid)
                if val == target:
                    return mid
                elif val > target:
                    return binarySearchRight(mid+1, r)
                elif val < target:
                    return binarySearchRight(l, mid-1)
            else:
                return -1
            
        peakIndex = binarySearchPeak(0, lenMtArr-1)
        if target == mountain_arr.get(peakIndex):
            return peakIndex
        
        leftRes = binarySearchLeft(0, peakIndex+1)
        if leftRes != -1:
            return leftRes
        
        
        rightRes = binarySearchRight(peakIndex, lenMtArr-1)
        if rightRes != -1:
            return rightRes
        
        return -1
        
