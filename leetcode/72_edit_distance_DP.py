class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        distances = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            distances[i][0] = i
        for j in range(n+1):
            distances[0][j] = j
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    distances[i][j] = distances[i-1][j-1]
                else:
                    distances[i][j] = 1 + min(distances[i-1][j], distances[i][j-1], distances[i-1][j-1])
        return distances[-1][-1]
