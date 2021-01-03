# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        if root:
            output = self.postorderTraversal(root.left)
            output = output + self.postorderTraversal(root.right)
            output.append(root.val)
        return output

