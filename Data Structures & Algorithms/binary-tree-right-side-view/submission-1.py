# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []

        q = deque()
        q.append(root)

        res.append(root.val)

        while q:
            curr_level = []
            level_len = len(q)

            for i in range(level_len):
                popped = q.popleft()

                if popped.left:
                    curr_level.append(popped.left.val)
                    q.append(popped.left)
                
                if popped.right:
                    curr_level.append(popped.right.val)
                    q.append(popped.right)
            
            if len(curr_level) > 0:
                res.append(curr_level[-1])
        
        return res
        