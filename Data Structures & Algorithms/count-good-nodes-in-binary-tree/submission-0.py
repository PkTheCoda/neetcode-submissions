# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_good = self.helper(root, root.val) # plus one for the root
        return num_good
    
    def helper(self, root: TreeNode, curr_max: int) -> int:
        if not root:
            return 0
        
        curr_val = root.val
        
        if curr_max <= curr_val:
            return 1 + self.helper(root.left, curr_val) + self.helper(root.right, curr_val)
        else:
            return self.helper(root.left, curr_max) + self.helper(root.right, curr_max)
        

        
    
        