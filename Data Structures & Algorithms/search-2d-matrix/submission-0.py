class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) - 1
        target_row = -1
        while lo <= hi:
            m = (lo + hi) // 2
            if target < matrix[m][0]:
                hi = m - 1
            elif target > matrix[m][len(matrix[m]) - 1]:
                lo = m + 1
            else:
                target_row = m
                break
        lo, hi = 0, len(matrix[target_row]) - 1
        while lo <= hi:
            m = (lo + hi) // 2
            if target ==  matrix[target_row][m]:
                return True
            elif target > matrix[target_row][m]:
                lo = m + 1
            else:
                hi = m - 1
        return False