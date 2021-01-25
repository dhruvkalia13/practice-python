# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root: 'TreeNode'):
            mid = False
            if root is None:
                return False
            if root == p or root == q:
                mid = True
            l = dfs(root.left)
            r = dfs(root.right)
            if (l and r) or (l and mid) or (r and mid):
                self.ans = root
            return l or r or mid
        dfs(root)
        return self.ans