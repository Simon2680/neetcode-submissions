import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        to use O(n):
        find a product without using 0's in the list
        loop over if the i
           
        """
        newnums = []
        for i in range(len(nums)):
            newnums.append((math.prod(nums[0:i]))*(math.prod(nums[i+1:len(nums)])))
        return newnums

       