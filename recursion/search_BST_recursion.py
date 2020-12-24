# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        if root.left is None and root.right is None or root is None:
            if root.val != val:
                return None
            else:
                return root
        elif root.val == val:
            return root
        elif root.val > val:
            return Solution.searchBST(self, root.left, val)
        else:
            return Solution.searchBST(self, root.right, val)