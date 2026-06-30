import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # make heap

        heap = stones
        for i in range(len(heap)):
            heap[i] = -1 * heap[i]
        
        heapq.heapify(heap)
        print(heap)

        while len(heap) > 1:
            l1 = (-1) * heapq.heappop(heap)
            l2 = (-1) * heapq.heappop(heap)

            if l1 != l2:
                to_add = (-1) * (max(l1, l2) - min(l1, l2))
                heapq.heappush(heap, to_add)

        if heap:
            return heap[0] * -1
        else:
            return 0
        