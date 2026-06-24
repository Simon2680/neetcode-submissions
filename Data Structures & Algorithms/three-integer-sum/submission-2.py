class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        first sort the numbers
        take one number and look up for the other two numbers that add up to be equal to - that number
        use two pointers to check for for the complement number
        """
        #sort

        #make a for loop to go through all the numbers:
        
        # use a while loop to keep jumping if next number is the same as the previous one

              #update the pointer  within this while loop:
              #right = will keep going forward

        #if we find two numbers that add up to - current i: --> append on the list[all 3 numbers]

        # if sum > -current i:
            #left -=1
        # if sum < -current sum --> right +=1

        # return the result
        nums.sort()

        result = []
        right = len(nums)-1
        left = 1
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while right > left:
                if nums[i]  + nums[right] + nums[left] == 0:
                    lst = [nums[i],nums[right],nums[left]]
                    result.append(lst)
                    right -= 1
                    left +=1
                    while right > left and nums[right+1] == nums[right]:
                        right -= 1
                    while right > left and nums[left-1] == nums[left]:
                        left +=1
                    
                elif nums[i] + nums[right] + nums[left] > 0:
                    right -=1
                else:
                    left +=1
            
        return result
            


        