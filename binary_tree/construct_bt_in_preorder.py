# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(start, end):
            if start > end:
                return None
            root = TreeNode(preorder.pop())
            index = map[root.val]
            root.left = helper(start, index-1)
            root.right = helper(index+1, end)
            return root
        preorder.reverse()
        map = {val:i for i, val in enumerate(inorder)}
        return helper(0, len(inorder)-1)