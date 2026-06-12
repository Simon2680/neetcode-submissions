class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        replace the element by the greatest elemnt at the right
        if the element is the last one repkace it by -1

        edge cases: empty list
                    if all the elements are uniform --> return the same array

        Plan: if empty --> in constraints
              uniform:
               . make the list into the set, and then return the length of the 
               set==1; if true
               return ythe list with out changing any thing

               take pointer to element at index 0
               replace it with the next bigger element in the list
               move pointer to 1

               if pointer is at the len(arr)-1, replace it with -1
               return the arr
        """

       
        
        if len(arr) <1:
            return []
        pointer = 0
        for i in range(len(arr)-1):
            arr[i] = max(arr[i+1::])
        arr[len(arr)-1] = -1
        return arr

        
        