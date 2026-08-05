from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        to_return = [0] * len(temperatures)
        q = []
        

        for i in range(len(temperatures)):

            while q and temperatures[i] > temperatures[q[-1]]:
                popped = q.pop(-1)
                to_return[popped] = i - popped
            
            q.append(i)
        
        return to_return

