class UnionFind:
    def __init__(self, N: int) -> None:
        self.parent = list(range(N))
        self.rank = [1]*N
    
    def find(self, p:int) -> int:
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    
    def union(self, p: int, q: int) -> bool:
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False
        if self.rank[prt] > self.rank[qrt]:
            prt, qrt = qrt, prt
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt]
        return True
