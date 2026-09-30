# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        out = []

        while q:
            curr_len = len(q)
            level_built = []

            for i in range(curr_len):
                front = q.popleft()
                level_built.append(front.val)

                if front.left:
                    q.append(front.left)
                
                if front.right:
                    q.append(front.right)
            
            out.append(level_built)
        
        return out

