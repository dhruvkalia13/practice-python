# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def dfs(root: TreeNode):
            if root is None:
                return None
            if not root.left and not root.right:
                if root.val == 0:
                    return None
                else:
                    return root
            node = TreeNode(root.val)
            l, r = False, False
            if root.left:
                a = dfs(root.left)
                if a:
                    l = True
                    node.left = a
            if root.right:
                b = dfs(root.right)
                if b:
                    r = True
                    node.right = b
            if not l and not r and node.val == 0:
                return None
            return node

        return dfs(root)


