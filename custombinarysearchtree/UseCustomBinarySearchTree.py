from custombinarysearchtree.CustomBinarySearchTree import CustomBinarySearchTree
from custombinarysearchtree.Node import Node

root = Node(5)
tree = CustomBinarySearchTree()
CustomBinarySearchTree.insert(tree, root, 2)
CustomBinarySearchTree.insert(tree, root, 7)
CustomBinarySearchTree.insert(tree, root, 4)
CustomBinarySearchTree.insert(tree, root, 3)
CustomBinarySearchTree.insert(tree, root, 6)

CustomBinarySearchTree.inorder(tree, root)
