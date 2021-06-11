from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        pass

if __name__ == '__main__':
    sol = Solution()
    grid_1 = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
    assert sol.countServers(grid_1) == 4
    grid_2 = [[1,0],[0,1]]
    assert sol.countServers(grid_2) == 0
    grid_3 = [[1,0],[1,1]]
    assert sol.countServers(grid_3) == 3