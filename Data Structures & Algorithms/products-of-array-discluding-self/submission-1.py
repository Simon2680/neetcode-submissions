import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        to use O(n):
        find a product without using 0's in the list
        loop over if the i
           
        """
        # newnums = [1]*len(nums)
        # prefix = 1
        # for i in range(len(nums)):
        #     newnums[i] = prefix
        #     prefix *= nums[i]
        # postfix =1
        # for i in range(len(nums)-1, -1, -1):
        #     newnums[i] = postfix * newnums[i]
        #     postfix *= nums[i]
        # return newnums
        # newarray = []
        # for i in range(len(nums)):
        #     summ = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             summ *= nums[j]
        #     newarray.append(summ) 
        # return newarray
        """
        find prefix and suffix
        create a new array
        multiply every prefix and suffx in the same position
        add the product to the new array

        """
        newarray = []
        postfix = []
        prefix = [1]
        for i in range(len(nums)):
            if i>0:
                prefix.append(math.prod(nums[:i]))
        for i in range(len(nums)):
            if i < len(nums)-1:
                postfix.append(math.prod(nums[i+1::]))
        postfix.append(1)
        print(postfix)
        for i in range(len(nums)):
            newarray.append(prefix[i]*postfix[i])
        return newarray






                

