# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if root.val == subRoot.val:
            if self.check(root, subRoot):
                return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return (left or right)
    
    def check(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False
        
        # vals have to be equal, but might as well
        if root.val != subRoot.val:
            return False
        
        left_equal = self.check(root.left, subRoot.left)
        right_equal = self.check(root.right, subRoot.right)

        return left_equal and right_equal
        