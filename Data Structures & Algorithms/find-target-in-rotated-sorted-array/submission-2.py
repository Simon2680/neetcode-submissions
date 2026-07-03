class Solution:
    def search(self, nums: List[int], target: int) -> int:

        """
        use binary search
        create a left and right pointers
        create a while loop, while right > left:
          find mid
          if target == nums[mid]:
            return mid
        elif compare look for the side where target might be
          if target is btn mid value and the mostright or equal:
            search right
          else:
            seach left
        """

        right, left = len(nums)-1, 0
        while right>=left:
            mid = (right+left)//2
            if target == nums[mid]:
                return mid
            #know the side you are at and the side that target should be at accordingly
            in_bigger = nums[mid] > nums[right]
            in_small = nums[mid]<nums[right]
            if in_bigger and target > nums[mid]:
                left = mid+1
            elif in_bigger and target < nums[mid]:
                #check the side of left
                if nums[left] <= target:
                    right = mid -1
                else:
                    left = mid + 1
            elif in_small and target > nums[mid]:
                if nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid -1

            else:
                right = mid -1
        return -1




    
        