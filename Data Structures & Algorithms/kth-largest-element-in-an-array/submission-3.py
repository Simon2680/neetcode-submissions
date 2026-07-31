class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        make all the heap
        pop the smallest and put it in the list


        """
        mini_heap = []
        heapq.heapify(mini_heap)
        for i in range (len(nums)):
            heapq.heappush(mini_heap, nums[i])
            if len(mini_heap) > k:
                #pop the the small
                heapq.heappop(mini_heap)
        return mini_heap[0]



            
        