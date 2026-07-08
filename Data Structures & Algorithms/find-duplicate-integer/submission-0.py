class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        use Floyd's algorithm

        use two pointers
        first intersection
        slow = 1 step
        fast = 2step


        second intersection:
        take slow back to index 0
        move them together and now fast is moving one step at atime

        the first time they meet that will be interance of the cycle
        
        """

        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        