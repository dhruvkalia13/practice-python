# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def dfs(root: TreeNode, val):
            if root.val != val:
                return False
            if root.left:
                if not dfs(root.left, val):
                    return False
            if root.right:
                if not dfs(root.right, val):
                    return False
            return True

        return dfs(root, root.val)