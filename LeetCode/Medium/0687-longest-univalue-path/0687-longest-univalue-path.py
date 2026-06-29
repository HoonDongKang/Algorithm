# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def search(node):
            nonlocal answer
            if not node:
                return 0
            
            cur_left_path = search(node.left)
            cur_right_path = search(node.right)
            left_path = 0
            right_path = 0

            if node.left and node.val == node.left.val:
                left_path = cur_left_path + 1

            if node.right and node.val == node.right.val:
                right_path = cur_right_path + 1

            answer = max(answer, left_path + right_path)
            return max(left_path, right_path)
        
        search(root)
        return answer