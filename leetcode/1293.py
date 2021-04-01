from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0
        # each item in this queue contains 4 elements
        # 0. row index
        # 1. col index
        # 2. num of remanining obstacles that can be removed
        # 3. num of steps 
        queue = deque([(0, 0, k, 0)])
        visited = set([(0, 0, k)])

        if k > (len(grid)-1 + len(grid[0])-1):
            return len(grid) + len(grid[0]) - 2
        while queue:
            row, col, eliminate, steps = queue.popleft()
            for new_row, new_col in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                if new_row >= 0 and new_row < len(grid) and new_col >=0 and new_col < len(grid[0]):
                    if grid[new_row][new_col] == 1 and eliminate > 0 and (new_row, new_col, eliminate-1) not in visited:
                        visited.add((new_row, new_col, eliminate-1))
                        queue.append((new_row, new_col, eliminate-1, steps+1))
                    if grid[new_row][new_col] == 0 and (new_row, new_col, eliminate) not in visited:
                        if new_row == len(grid)-1 and new_col == len(grid[0])-1:
                            return steps + 1
                        visited.add((new_row, new_col, eliminate))
                        queue.append((new_row, new_col, eliminate, steps+1))
        return -1

if __name__ == '__main__':
    grid = [[0,0,0],
            [1,1,0],
            [0,0,0],
            [0,1,1],
            [0,0,0]], 
    k = 1
    sol = Solution()
    print(sol.shortestPath(grid, k))

    grid_1 = [[0,0,0]]
    k_1 = 1
    print(sol.shortestPath(grid_1, k_1))
