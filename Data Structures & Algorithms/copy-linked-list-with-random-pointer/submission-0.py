"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
       d = {}
       d[None] = None

       curr = head
       while curr:
        created = Node(curr.val)
        d[curr] = created
        curr = curr.next
    
       for original, copy in d.items():
        if original != None:
            copy.next = d[original.next]
            copy.random = d[original.random]
       
       return d[head]




        