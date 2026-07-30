import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = [-n for n in nums]
        heapq.heapify(self.nums)
        self.mini_heap = []
        self.k = k
        while self.nums and len(self.mini_heap)<self.k:
            heapq.heappush(self.mini_heap, -heapq.heappop(self.nums))
               
            
    def add(self, val: int) -> int:
        if len(self.mini_heap)<self.k:
            heapq.heappush(self.mini_heap, val) 
        elif self.mini_heap[0] < val:
            heapq.heappop(self.mini_heap)
            heapq.heappush(self.mini_heap, val)
        return self.mini_heap[0]
        

        

        




        
        
