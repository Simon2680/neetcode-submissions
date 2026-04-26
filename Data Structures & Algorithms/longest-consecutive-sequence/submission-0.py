class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        U: I: list of integers
           O: integer representing the length of lengest consecutive chain
           E: empty list --> 0
              
           C
        P: sort the list
           create a counter to keep track of the greatest counter
           loop create a while loop to loop through the entire list:
              counter = 1
              



        """

        counter = 1
        nums.sort()
        count = 1

        i = 0
        if len(nums) == 0:
            return 0
        while i < len(nums)-1:
            
            if (nums[i] - nums[i+1]) == -1:
                count+=1
            elif (nums[i] - nums[i+1]) == 0:
                count+=0
            else:
                counter = max(counter, count)
                count = 1
            i += 1
        counter = max(counter, count)
        
        return counter
            


        