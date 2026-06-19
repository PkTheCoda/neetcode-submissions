# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.recursive(root)

        return self.result
    
    def recursive(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        left_height = self.recursive(root.left)
        right_height = self.recursive(root.right)

        self.result = max(self.result, left_height + right_height)

        return 1 + max(left_height, right_height)
        