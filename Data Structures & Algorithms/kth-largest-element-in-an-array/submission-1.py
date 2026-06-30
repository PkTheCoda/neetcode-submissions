import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # brute force
        heap = []
        res = []

        for num in nums:
            heap.append(-num)
        
        heapq.heapify(heap)

        for i in range(k):
            res.append(heapq.heappop(heap))
        
        return -res[-1]