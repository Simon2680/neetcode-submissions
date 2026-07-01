class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        create a BigArray to keep all the elements
        make the entire matrix a single array/list
        loop through the rows/length of the matrix
        append every row to bigArray
         use binary search to look for the target
        """

        # bigArray = []
        # for row in matrix:
        #     bigArray += row
        # right = len(bigArray)-1
        # left = 0
    
        # while right >= left:
        #     mid = (right+left)//2
        #     if bigArray[mid] == target:
        #         return True
        #     elif bigArray[mid] > target:
        #         right = mid-1
        #     else:
        #         left = mid + 1
        # return False
        # above is the O(m*n) solution

        #O(log(m*n)) sol
        ##################
        """
        do multiple binary search at each row
        create a while loop to keep checking if you have found the target and that we haven't gone out of the matrix
        under this while loop create another while loop that will be search in a row:

        return False at the end of bigger while loop
        """

        # for i in range(len(matrix)): --> O(mlog(n)) sol
        #     right = len(matrix[i])-1
        #     left = 0
        #     while right >= left:
        #         mid = (right + left)//2
        #         if matrix[i][mid] == target:
        #             return True
        #         elif matrix[i][mid] > target:
        #             right = mid -1
        #         else:
        #             left = mid + 1
        # return False


        """
        two binary search
        use rows to look whether the target might be in the boundry of them
        plan:
          right, left, len(matrix),0
          while:
            if --> true:
                record the row number
                do a binary search in that row
            return False

        """
        rowNumber = None
        rowFound = False
        left, right = 0, len(matrix)-1
        while right>=left:
            mid = (right+left)//2
            #if target in the range of mid row elements--> return true and the row number
            if matrix[mid][0]<= target<=matrix[mid][-1]:
                rowNumber = mid
                rowFound = True
                break
            elif not (matrix[mid][0]<= target<=matrix[mid][-1]) and target < matrix[mid][0]:
                #loop up
                right = mid-1
            else:
                left = mid + 1
        if rowFound:
            targetRow = matrix[rowNumber]
            l,r = 0, len(targetRow)-1
            while r>=l:
                m = (r+l)//2
                if targetRow[m] == target:
                    return True
                elif targetRow[m] > target:
                    r = m -1
                else:
                    l = m+1
            return False

        else:
            return False


























    
        