import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for item in points:
            origin_distance = item[0]**2 + item[1]**2
            heapq.heappush(heap, [origin_distance, item])
        
        print(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
