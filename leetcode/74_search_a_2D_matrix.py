class Solution:
    def binarySearch(self, arr: List[int], target: int) -> bool:
        low = 0
        high = len(arr) - 1
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            # If x is greater, ignore left half
            if arr[mid] < target:
                low = mid + 1

            # If x is smaller, ignore right half
            elif arr[mid] > target:
                high = mid - 1
            # means x is present at mid
            else:
                return mid
        # If we reach here, then the element was not present
        return -1
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        converted_matrix = []
        for i in range(len(matrix)):
            converted_matrix.extend(matrix[i])
        return self.binarySearch(converted_matrix, target) != -1
        
