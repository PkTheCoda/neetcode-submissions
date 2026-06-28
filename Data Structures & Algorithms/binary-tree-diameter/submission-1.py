# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.distance(root)
        return self.res

    def distance(self, root: Optional[TreeNode]) -> int:    
        if not root:
            return 0
        
        leftDistance = self.distance(root.left)
        rightDistance = self.distance(root.right)

        self.res = max(self.res, leftDistance + rightDistance)

        return 1 + max(leftDistance, rightDistance)