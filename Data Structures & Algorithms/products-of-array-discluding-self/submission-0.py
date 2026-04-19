class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        create an empty list
        loop over the given list and multiply everything with the rest of others in list
        at except i
        put the product at i in new list
        return new list
        """

        myList = []
        for i in range(len(nums)):
            product = 1
           
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                  
                    product *= nums[j]
                   
            myList.append(product)
            
        return myList



        