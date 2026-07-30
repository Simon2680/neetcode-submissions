import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mini_heap = []
        for i in range(len(points)):
            x1, y1 = 0, 0
            x2, y2 = points[i][0], points[i][1]
            distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

            heapq.heappush(mini_heap, (-distance, points[i]))
            if len(mini_heap) > k:
                heapq.heappop(mini_heap)

        return [point for _, point in mini_heap]