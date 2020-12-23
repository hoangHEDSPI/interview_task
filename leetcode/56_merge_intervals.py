from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        results = []
        intervals = sorted(intervals, key=lambda i: i[0])
        for i in intervals:
            if results and i[0] <= results[-1][1]:
                results[-1][1] = max(results[-1][1], i[1])
            else:
                results.append(i)
        return results

if __name__=="__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    solution = Solution()
    solution.merge(intervals)