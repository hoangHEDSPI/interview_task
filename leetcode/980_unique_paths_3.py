from typing import List

class Solution:
    def dfs(self, grid: List[List[int]], res: int, x: int, y: int, empty: int):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return
        if grid[x][y] == 2 and empty == 0:
            res += 1
        grid[x][y] = -2
        self.dfs(grid, res, x+1, y, empty-1)
        self.dfs(grid, res, x-1, y, empty-1)
        self.dfs(grid, res, x, y+1, empty-1)
        self.dfs(grid, res, x, y-1, empty-1)
        grid[x][y] = 0

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        res = 0
        empty = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x, y = (i, j)
                elif grid[i][j] == 0:
                    empty += 1
        self.dfs(grid, res, x, y, empty)
        return res


if __name__ == '__main__':
    grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    sol = Solution()
    assert sol.uniquePathsIII(grid) == 2