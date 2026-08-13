class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = cols*row - 1
        while left <= right:
            mid = (left+right) // 2
            row = mid // cols
            col = mid % cols
            if target == matrix[row][col]:
                return True
            elif matrix[row][col] < target:
                left = mid +1
                
            else:
                right = mid-1
        return False
        