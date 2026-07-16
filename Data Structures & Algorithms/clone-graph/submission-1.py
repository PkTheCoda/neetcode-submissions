"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # 1 <-> 2 <-> 3
        # q: Node(1)
        # [1]: Node(1)
        # X, q: Node(2)
        
        q = deque()
        freq = {}
        q.append(node)

        while q:
            popped = q.popleft()

            if not popped:
                return None
            
            if popped.val not in freq:
                freq[popped.val] = Node(popped.val)
            
            for neighbor in popped.neighbors:
                if neighbor.val not in freq:
                    freq[neighbor.val] = Node(neighbor.val)
                    q.append(neighbor)
                
                freq[popped.val].neighbors.append(freq[neighbor.val])
        
        return freq[1]
