class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        # Compare the maximum number of each column
    
        topCol = 0
        bottomCol = len(mat) - 1
        while bottomCol > topCol:
            midCol = (bottomCol + topCol) // 2
            if max(mat[midCol]) > max(mat[midCol + 1]):
                bottomCol = midCol
            else:
                topCol = midCol + 1
        return [bottomCol, mat[bottomCol].index(max(mat[bottomCol]))]
      
