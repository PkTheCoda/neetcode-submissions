from collections import deque
from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = []

        for key, value in freq.items():
            heap.append(-value)
        
        heapq.heapify(heap)

        time = 0
        q = deque()

        while heap or q:
            # increment time
            time += 1

            if heap:
                popped = heapq.heappop(heap)
                new_val = popped + 1
                if new_val < 0:
                    q.append([new_val, time + n])

            
            # only add back to queue (along with when to next add)
            
            
            while q and q[0][1] == time:
                popped = q.popleft()
                heapq.heappush(heap, popped[0])

        return time