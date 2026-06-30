import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        res = []

        for num in nums:
            heap.append(-num)
        
        heapq.heapify(heap)

        for i in range(k):
            res.append(heapq.heappop(heap))
        
        print(heap)
        print
        
        return -res[-1]