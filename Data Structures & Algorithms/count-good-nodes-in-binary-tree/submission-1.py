# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_good = self.helper(root, root.val)
        return num_good
    
    def helper(self, root: TreeNode, runningMax):
        if not root:
            return 0
        
        curr_val = root.val
        curr_max = max(runningMax, curr_val)

        if runningMax > curr_val:
            return 0 + self.helper(root.left, curr_max) + self.helper(root.right, curr_max)
        else:
            return 1 + self.helper(root.left, curr_max) + self.helper(root.right, curr_max)
        