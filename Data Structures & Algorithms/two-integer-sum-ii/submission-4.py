class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        use pointers
        use 2 pointers
        one at the end and other at the begining
        compare two numbers at both end
        if sum is > target--> move right pointer in
        if sum is < target--> move the right pointer in
        if sum = target--> return [leftPointer, rightPointer]


        """

        left = 0
        right = len(numbers)-1
        while True:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left+1,right+1]

    
       

                
                
        