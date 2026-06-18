class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        i = 0
        j = n*m - 1

        while i <= j:
            mid = (j-i)//2 + i
            
            row = mid // m
            col = mid % m

            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                i = mid + 1
            else:
                j = mid - 1
        
        return False
            