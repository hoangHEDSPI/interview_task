from typing import List

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        pos = [0 for _ in range(len(row))]
        res = 0
        for i in range(len(row)):
            pos[row[i]] = i
        for i in range(0, len(row), 2):
            pair = row[i]+1 if row[i] % 2 == 0 else row[i]-1
            if row[i+1] != pair:
                row[pos[pair]] = row[i+1]
                pos[row[i+1]] = pos[pair]
                res += 1
        return res

if __name__ == '__main__':
    row = [0, 2, 1, 3]
    row_1 = [3, 2, 0, 1]
    row_2 = [1, 4, 3, 0, 2, 5]
    sol = Solution()
    assert sol.minSwapsCouples(row) == 1
    assert sol.minSwapsCouples(row_1) == 0
    assert sol.minSwapsCouples(row_2) == 2
