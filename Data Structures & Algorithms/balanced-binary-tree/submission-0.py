# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        self.height(root)

        return self.balanced
    
    def height(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        right_height = self.height(root.right)
        left_height = self.height(root.left)
        
        if abs(right_height - left_height) > 1:
            self.balanced = False

        return 1 + max(right_height, left_height)
        