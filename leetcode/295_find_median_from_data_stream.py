import bisect

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.arr, num)
        
    def findMedian(self) -> float:
        n = len(self.arr)
        if n == 0:
            return None
        if n % 2 == 0:
            return (self.arr[n//2 - 1] + self.arr[n//2])/2
        return self.arr[n // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()