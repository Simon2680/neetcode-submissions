class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      #   for i in range(len(nums)):
      #    for j in range(len(nums)):
      #       if nums[i] + nums[j] == target and i != j:
      #          return [i, j]

      '''
      create a hasmap
      loop through the nums
      if number-target is in hasmap and its value is different from index of number --> [value, index]
      else:
         add the nums-target to the hasmap and its corresponding index
      '''
      hasmap = {}
      for i in range(len(nums)):
         compliment = target - nums[i]
         if compliment in hasmap:
            return [hasmap[compliment], i]
         else:
            hasmap[nums[i]] = i
   
        