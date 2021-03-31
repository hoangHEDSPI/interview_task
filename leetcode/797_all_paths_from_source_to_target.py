from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1
        res = []
        def dfs(path: List[int]):
            if path[-1] == target:
                res.append(path)
                return
            for child in graph[path[-1]]:
                dfs(path + [child])
        dfs([0])
        return res

if __name__ == '__main__':
    graph = [[1,2],[3],[3],[]]
    sol = Solution()
    assert sol.allPathsSourceTarget(graph) == [[0,1,3],[0,2,3]]