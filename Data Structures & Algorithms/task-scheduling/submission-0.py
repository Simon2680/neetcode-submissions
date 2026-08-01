import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        create the counter of each character
        make the max-heap of values
        make the heap(deque)--will keep the tuple(current value, next_time)
        normal current time = 0
        create the time counter--> time of next turn = n + current_time
        while max_heap or heap:
            if top of normal heap' next_time = current time:
                push the value to the max_heap
                pop it from the queue
            popedValue +1 = new_Vaue
            time = +=1
            next_time = time+n
            push onto the queue (next_time, new_value)
        return time    


        """
        counter = Counter(tasks)
        max_heap = [-v for v in list(counter.values())]
        heapq.heapify(max_heap)
        time = 0
        heap = deque([])
        while heap or max_heap:
           
            if heap and heap[0][0] == time:
                heapq.heappush(max_heap, heap[0][1])
                heap.popleft()
                
            
            elif max_heap:
                next_value = 1+heapq.heappop(max_heap)
                time +=1
                next_time = n + time
                if next_value:
                    heap.append([next_time, next_value])  
            else:
                time +=1  
        return time



        