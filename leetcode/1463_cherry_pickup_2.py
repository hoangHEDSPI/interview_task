from functools import lru_cache
from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @lru_cache
        def dfs(r, c1, c2):
            if r == m:
                return 0
            cherries = grid[r][c1] if c1 == c2 else grid[r][c1] + grid[r][c2]
            ans = 0
            for nc1 in range(c1 - 1, c1 + 2):
                for nc2 in range(c2 - 1, c2 + 2):
                    if nc1 >= 0 and nc1 < n and nc2 >= 0 and nc2 < n:
                        ans = max(ans, dfs(r + 1, nc1, nc2))
            return ans + cherries
        return dfs(0, 0, n-1)


if __name__ == '__main__':
    sol = Solution()
    grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
    assert sol.cherryPickup(grid) == 24
    grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
    assert sol.cherryPickup(grid) == 28
                
                