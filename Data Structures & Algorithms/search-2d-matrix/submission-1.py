class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        create a BigArray to keep all the elements
        make the entire matrix a single array/list
        loop through the rows/length of the matrix
        append every row to bigArray
         use binary search to look for the target
        """

        bigArray = []
        for row in matrix:
            bigArray += row
        right = len(bigArray)-1
        left = 0
    
        while right >= left:
            mid = (right+left)//2
            if bigArray[mid] == target:
                return True
            elif bigArray[mid] > target:
                right = mid-1
            else:
                left = mid + 1
        return False
    
        