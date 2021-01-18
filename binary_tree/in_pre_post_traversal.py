# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        curr = root
        output = []
        if curr:
            output.append(curr.val)
            if curr.left:
                l = self.preorderTraversal(curr.left)
                if l:
                    output.extend(l)
            if curr.right:
                r = self.preorderTraversal(curr.right)
                if r:
                    output.extend(r)
            if not curr.left and not curr.right:
                return output
        return output
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        if root:
            if root.left:
                l = self.inorderTraversal(root.left)
                if l:
                    output.extend(l)
            output.append(root.val)
            if root.right:
                r = self.inorderTraversal(root.right)
                if r:
                    output.extend(r)
        return output
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        if root:
            if root.left:
                l = self.postorderTraversal(root.left)
                if l: output.extend(l)
            if root.right:
                r = self.postorderTraversal(root.right)
                if r: output.extend(r)
            output.append(root.val)
        return output
