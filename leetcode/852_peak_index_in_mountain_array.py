class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def binarySearchPeak(l, r):
            # Because there is alway a peak value so we do not need to handle None cases
            mid = (l + r) // 2
            val = arr[mid]
            prev_val = arr[mid-1]
            next_val = arr[mid+1]
            if prev_val < val and next_val < val:
                # return the index of the peak
                return mid
            elif prev_val > val:
                return binarySearchPeak(l, mid-1)
            elif next_val > val:
                return binarySearchPeak(mid+1, r)
        return binarySearchPeak(0, len(arr)-1)
      
