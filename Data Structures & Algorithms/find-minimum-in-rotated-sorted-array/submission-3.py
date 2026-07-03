class Solution:
    def findMin(self, nums: List[int]) -> int:

        right, left = len(nums)-1, 0
        while right>left:
            mid = (right+left)//2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
        return nums[right]
          
        