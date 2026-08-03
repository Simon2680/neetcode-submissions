class Solution:
    def bin_find(self, nums: List[int], start_idx:int, end_idx:int, target:int) -> int:
        if start_idx >= end_idx:
            return start_idx if start_idx < len(nums) and nums[start_idx] == target else -1

        mid_idx = (start_idx + end_idx) // 2

        if nums[mid_idx] == target:
            return mid_idx

        if nums[mid_idx] > target:
            return self.bin_find(nums, start_idx, mid_idx - 1, target)
        else:
            return self.bin_find(nums, mid_idx + 1, end_idx, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.bin_find(nums,0,len(nums) - 1, target)
