import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

      """
      create a while loop until there is no more than 1 stone remaining:
        neg all the numbers
        heapify the nums
        y = -heappop
        x = -heappop

        if x<y:
          heappush(nums, -(y-x))
      after while loop:
      return heap[0] if heap else 0
      """
      stones = [-stone for stone in stones]
      heapq.heapify(stones)
      while len(stones)>1:
        y = -heapq.heappop(stones)
        x = -heapq.heappop(stones)
        if x<y:
          heapq.heappush(stones, -(y-x))
      return -stones[0] if stones else 0
       
            





        
        