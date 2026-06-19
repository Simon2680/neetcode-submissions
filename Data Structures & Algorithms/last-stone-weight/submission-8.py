import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        make a heap

        while x and y:
        
        pop two max : x and y
        compare them and if x==y:
          do nothing since we have already poped them put
        if x != y:
            small stone is destroyed--> no need to push it back
            bigger stone change weight:
            push max-min

        # Returns (x or y) if the condition evaluates to True, otherwise returns None
          return (x or y) if (x or y) else None
        '''
        myheap = [-stone for stone in stones]
        heapq.heapify(myheap)
        x = None
        y = None
        if myheap:
            x = heapq.heappop(myheap)
        if myheap:y = heapq.heappop(myheap)
        while x != None and y != None:
            x *= -1
            y *= -1
            if x != y:
               diff = max(x,y) - min(x,y)
               heapq.heappush(myheap, -1 *diff)
            x = None
            y = None
            if myheap:
                x = heapq.heappop(myheap)
            if myheap:
                y = heapq.heappop(myheap)

            
        return (-x or -y) if (x or y) else 0
            





        
        