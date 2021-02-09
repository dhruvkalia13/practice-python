# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if root is None:
                return None
            dfs(root.right)
            self.total += root.val
            root.val = self.total
            dfs(root.left)
            return root

        return dfs(root)


