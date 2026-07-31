class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        make all the heap
        pop the smallest and put it in the list


        """
        # nums = [-v for v in nums]
        # heapq.heapify(nums)
        # for i in range(k):
        #     if i == k-1:
        #         return -heapq.heappop(nums)
        #     else:
        #         heapq.heappop(nums)

        nums.sort(reverse = True)
        return nums[k-1]

            
        