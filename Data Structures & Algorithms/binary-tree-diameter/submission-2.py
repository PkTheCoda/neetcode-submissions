# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.helper(root)
        return self.res
    
    def helper(self, root: Optional[TreeNode]):
        if not root:
            return 0
        
        left_max_height = self.helper(root.left)
        right_max_height = self.helper(root.right)

        self.res = max(self.res, left_max_height + right_max_height)

        return 1 + max(left_max_height, right_max_height)
        

        