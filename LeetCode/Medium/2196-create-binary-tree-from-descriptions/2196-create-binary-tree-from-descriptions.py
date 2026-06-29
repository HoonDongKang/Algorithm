# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = {}
        child_set = set()

        for parent, child, isLeft in descriptions:
            if parent not in node_map:
                node_map[parent] = TreeNode(parent)
            
            if child not in node_map:
                node_map[child] = TreeNode(child)
            
            child_set.add(child)

            if isLeft:
                node_map[parent].left = node_map[child]
            else:
                node_map[parent].right = node_map[child]

        root = None
        for node in node_map.keys():
            if node not in child_set:
                root = node_map[node]

        return root