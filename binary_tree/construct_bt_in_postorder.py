# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(start, end):
            if start > end:
                return None
            if len(postorder) > 0:
                root = TreeNode(postorder.pop())
            index = map[root.val]

            root.right = helper(index + 1, end)
            root.left = helper(start, index - 1)
            return root

        map = {val: i for i, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)