from custombinarysearchtree.Node import Node


class CustomBinarySearchTree:

    def insert(self, root, key):
        if root is None:
            root = Node(key)
        else:
            if root.key > key:
                if root.left is None:
                    root.left = Node(key)
                else:
                    self.insert(root.left, key)
            elif root.key <= key:
                if root.right is None:
                    root.right = Node(key)
                else:
                    self.insert(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key)
            self.inorder(root.right)
