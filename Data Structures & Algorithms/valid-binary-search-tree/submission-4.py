# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # start it
        isLeftValid = self.helper(root.left, float('-inf'), root.val)
        isRightValid = self.helper(root.right, root.val, float('inf'))

        return (isLeftValid and isRightValid)
        
    
    def helper(self, root: Optional[TreeNode], val_min, val_max) -> bool:
        if not root:
            return True
        
        val = root.val
        
        if val <= val_min or val >= val_max:
            return False
        
        isLeftValid = self.helper(root.left, val_min, val) # min will always be -1000, max shrinks
        isRightValid = self.helper(root.right, val, val_max) # max will always be 1000, min grows

        return (isLeftValid and isRightValid)


        
