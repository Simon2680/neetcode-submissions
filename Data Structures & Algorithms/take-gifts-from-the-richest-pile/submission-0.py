import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        """
        make a heap with numbers reversed
        pick the maximum
        
        
    
        """
        myheap = [-s for s in gifts]
        heapq.heapify(myheap)
        for k in range(k):
            maximum = heapq.heappop(myheap)
            heapq.heappush(myheap, -math.isqrt(-maximum))
        return -sum(myheap)
       

        
    
    

      
        
        