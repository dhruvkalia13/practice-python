# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None and sum == 0:
            return False
        if root and root.left is None and root.right is None:
            if root.val == sum:
                return True
        if root and root.left:
            if self.hasPathSum(root.left, sum - root.val):
                return True
        if root and root.right:
            if self.hasPathSum(root.right, sum - root.val):
                return True
        return False