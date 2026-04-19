import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        to use O(n):
        find a product without using 0's in the list
        loop over if the i
           
        """
        newnums = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            newnums[i] = prefix
            prefix *= nums[i]
        postfix =1
        for i in range(len(nums)-1, -1, -1):
            newnums[i] = postfix * newnums[i]
            postfix *= nums[i]
        return newnums
        
       