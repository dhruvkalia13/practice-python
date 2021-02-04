# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def dfs(root, low, high):
            if root is None:
                return None
            temp = None
            if low <= root.val <= high:
                temp = TreeNode(root.val)
            if root.left:
                l = dfs(root.left, low, high)
                if l:
                    if temp:
                        temp.left = l
                    else:
                        temp = l
            if root.right:
                r = dfs(root.right, low, high)
                if r:
                    if temp:
                        temp.right = r
                    else:
                        temp = r
            return temp

        return dfs(root, low, high)
