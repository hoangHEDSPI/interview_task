from collections import deque

class Graph:
    def __init__(self, num_vertices: int) -> None:
        self.num_vertices = num_vertices
        self.graph = [] * num_vertices
        self.dist = [0] * num_vertices

    def add_edge(self, u: int, v: int):
        if u >= self.num_vertices or v >= self.num_vertices:
            print("Vertice indexes cannot equal or bigger than the total number of vertices.")
            return
        if v in self.graph[u]:
            print("This edge has already been added.")
            return
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def multi_source_bfs(self):
        q = deque([i for i in range(self.num_vertices)])
        visited = [False] * self.num_vertices
        while q:
            v = q.popleft()
            for i in self.graph[v]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
                    self.dist[i] = self.dist[v] + 1
    