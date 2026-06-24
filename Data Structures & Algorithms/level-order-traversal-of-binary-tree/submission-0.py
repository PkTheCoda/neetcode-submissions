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
        
        main_arr = []
        q = deque()

        
        q.append(root)
        main_arr.append([root.val])


        while q:
            curr_level = []
            size = len(q)

            for i in range(size):
                popped = q.popleft()

                if popped.left:
                    curr_level.append(popped.left.val)
                    q.append(popped.left)
                
                if popped.right:
                    curr_level.append(popped.right.val)
                    q.append(popped.right)
            
            if len(curr_level) > 0:
                main_arr.append(curr_level)

        return main_arr





        