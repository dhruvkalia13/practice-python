# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        output = []
        temp = queue
        i = 1
        while len(queue) != 0:
            out = []
            for j in range(len(queue)):
                node = queue.pop(0)
                out.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            if i % 2 == 0:
                output.append(out[::-1])
            else:
                output.append(out)
            i += 1
            queue = temp
        return output
