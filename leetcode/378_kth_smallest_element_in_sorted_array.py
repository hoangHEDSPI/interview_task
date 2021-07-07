class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flatten_matrix = []
        for i in range(len(matrix)):
            flatten_matrix.extend(matrix[i])
        
        flatten_matrix.sort()
        return flatten_matrix[k-1]
      
