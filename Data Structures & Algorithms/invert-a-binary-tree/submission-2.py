# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.left:
            self.invertTree(root.left)
        
        if root.right:
            self.invertTree(root.right)
        
        # now we're at nodes where we've recursed all the way down. now we're backtracking up from the leaf nodes
        root.left, root.right = root.right, root.left   

        return root  
        