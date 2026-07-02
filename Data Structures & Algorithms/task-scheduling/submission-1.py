from collections import Counter
from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = []
        time = 0

        q = deque()
        for key, value in freq.items():
            heapq.heappush(heap, -value)
        
        heapq.heapify(heap)
        print(heap)

        while heap or q:
            time += 1
            if heap:
                popped = heapq.heappop(heap)
                popped = popped + 1
                if popped < 0:
                    q.append([popped, time + n])

            while q and q[0][1] == time:
                popped = q.popleft()
                heapq.heappush(heap, popped[0])
        
        return time
