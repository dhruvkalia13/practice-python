# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def dfs(t1: TreeNode, t2: TreeNode):
            if not t1 and not t2:
                return None
            if t1 and not t2:
                return t1
            if t2 and not t1:
                return t2
            node = TreeNode(t1.val + t2.val)
            if t1.left and t2.left:
                node.left = dfs(t1.left, t2.left)
            else:
                if t1.left and not t2.left:
                    node.left = t1.left
                if t2.left and not t1.left:
                    node.left = t2.left
            if t1.right and t2.right:
                node.right = dfs(t1.right, t2.right)
            else:
                if t1.right and not t2.right:
                    node.right = t1.right
                if t2.right and not t1.right:
                    node.right = t2.right
            return node
        return dfs(t1, t2)