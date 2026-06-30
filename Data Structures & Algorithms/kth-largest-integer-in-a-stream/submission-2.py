import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for item in nums:
            self.add(item)

    def add(self, val: int) -> int:
        if len(self.heap) != self.k: 
                heapq.heappush(self.heap, val)
        else:
            heapq.heappush(self.heap, val)
            heapq.heappop(self.heap)
            
        return self.heap[0]


        
