# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         """
#         use binary search

#         create small variable
#         right and left pointers
#          have a while loop until left and right are 1 distance apart--> right-left = 1
#          find mid
#          midleft
#          midright
#          small = mid
#          if midright > mid and midleft> mid:
#             return nums[mid]
#          elif midright > mid:
#             <<------go left
#             right = mid -1
#          elif midright < mid:
#             left = mid +1

#         if no return that happened that means that min is btn two numbers and return min btn them
           

         


#         """
#         left , right = 0, len(nums)-1
#         while right>left:
#             mid = (right+left)//2
#             midRight = nums[mid+1]
#             midLeft = nums[mid-1]
#             if midRight>nums[mid] and midLeft > nums[mid]:
#                 return nums[mid]
#             elif midRight > nums[mid]:
#                 right = mid-1
#             else:
#                 left = mid +1
#         return nums[right] 
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        # Standard binary search condition works perfectly here
        while left < right:
            mid = (left + right) // 2
            
            # If mid element is greater than the rightmost element,
            # the minimum element must be in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, the minimum is in the left half (including mid)
            else:
                right = mid
                
        return nums[right]
        