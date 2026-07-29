import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = [-v for v in nums]
        heapq.heapify(self.nums)
        self.k = k

        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,-val)
        knums = []
        for n in range(self.k):
            knums.append(heapq.heappop(self.nums))
        res = knums[-1]
    
        for i in range(self.k):
            heapq.heappush(self.nums, knums[i])
        return -res




        
        
