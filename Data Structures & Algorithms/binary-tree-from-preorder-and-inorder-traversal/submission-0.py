# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        
        root = preorder[0]
        root_node = TreeNode(root)
        pre_index_inorder = inorder.index(root)

        root_node.left = self.buildTree(preorder[1:1+pre_index_inorder], inorder[:pre_index_inorder])
        root_node.right = self.buildTree(preorder[1+pre_index_inorder:], inorder[pre_index_inorder + 1:])

        return root_node