# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        queue = [root]
        while len(queue) > 0:
            children = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    children.append(node.val)
                else:
                    children += "*"
                    continue
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(None)
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append(None)
            if children != children[::-1]: return False
        return True


