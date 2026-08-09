class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, btm = 0, ROWS - 1

        while top <= btm:
            mid_r = (top + btm) // 2

            if target > matrix[mid_r][-1]:
                top = mid_r + 1
            elif target < matrix[mid_r][0]:
                btm = mid_r - 1
            else:
                break
        
        if not (top <= btm):
            return False

        mid_r = (top + btm) // 2

        L, R = 0, COLS - 1

        while L <= R:
            mid_c = (L + R) // 2

            if target > matrix[mid_r][mid_c]:
                L = mid_c + 1
            elif target < matrix[mid_r][mid_c]:
                R = mid_c - 1
            else:
                return True
        return False

            

         
        