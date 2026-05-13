# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        
        if not postorder:
            return None
        

        root = postorder[-1]
        result = TreeNode(root)

        root_idx = inorder.index(root)
        left_inorder, right_inorder = inorder[:root_idx], inorder[root_idx + 1:]
        left_postorder, right_postorder = postorder[:len(left_inorder)], postorder[len(left_inorder): -1]

        result.left = self.buildTree(left_inorder, left_postorder)
        result.right = self.buildTree(right_inorder, right_postorder)

        return result
