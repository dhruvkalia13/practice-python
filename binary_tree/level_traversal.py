# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        output = []
        done = False
        curr = [root]
        while not done:
            temp = []
            a = []
            done = True
            for c in curr:
                temp.append(c.val)
                if c.left:
                    a.append(c.left)
                    done = False
                if c.right:
                    a.append(c.right)
                    done = False
            output.append(temp)
            curr = a
        return output
