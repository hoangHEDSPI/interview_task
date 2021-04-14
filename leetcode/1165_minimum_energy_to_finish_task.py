from typing import List
from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Not my solution
        tasks.sort(key=lambda x: x[1]-x[0])
        min_energy = 0
        for task in tasks:
            min_energy += task[0]
            if min_energy < task[1]:
                min_energy = task[1]
        return min_energy