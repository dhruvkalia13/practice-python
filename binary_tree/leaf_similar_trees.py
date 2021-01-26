# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.root1_leaf = ""
        self.root2_leaf = ""
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root: TreeNode, i: int):
            if not root:
                return
            if not root.left and not root.right:
                if i == 1:
                    self.root1_leaf += (str(root.val) + "*")
                else:
                    self.root2_leaf += (str(root.val) + "*")
            if root.left:
                dfs(root.left, i)
            if root.right:
                dfs(root.right, i)
        dfs(root1, 1)
        dfs(root2, 2)
        return self.root1_leaf == self.root2_leaf