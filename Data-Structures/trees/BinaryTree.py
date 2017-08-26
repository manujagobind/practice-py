"""Includes classes BinaryTree, BinarySearchTree and AVLTree."""

from TreeNode import BinaryTreeNode as Node

class BinaryTree(object):
    """Binary Tree Class."""

    def __init__(self):
        self._root = None        

    def get_root(self):
        """Returns root of tree."""
        return self._root

    def set_root(self, node):
        """Set the root of tree to given node."""
        self._root = node

    def inorder(self):
        """Inorder traversal."""
        def inorder(node):
            if node:
                inorder(node.get_left())
                print(node.get_key(), end=' ')
                inorder(node.get_right())
        inorder(self.get_root())
        print()

    def preorder(self):
        """Inorder traversal."""
        def preorder(node):
            if node:
                print(node.get_key(), end=' ')
                preorder(node.get_left())                
                preorder(node.get_right())
        preorder(self.get_root())
        print()

    def postorder(self):
        """Inorder traversal."""
        def postorder(node):
            if node:
                postorder(node.get_left())                
                postorder(node.get_right())
                print(node.get_key(), end=' ')
        postorder(self.get_root())
        print()


class BinarySearchTree(BinaryTree):
    """Binary Search Tree Class."""

    def __init__(self):
        super(BinarySearchTree, self).__init__()

    def minimum(self, node=None):
        """Returns node with minimum key value."""
        if not node:
            node = self.get_root()
        while not node.has_left():
            node = node.get_left()
        return node

    def insert(self, key):
        """Inserts new node in the tree."""
        def insert(node, key):
            if not node:
                node = Node(key)
            elif key < node.get_key():
                node.set_left(insert(node.get_left(), key))
            elif key > node.get_key():
                node.set_right(insert(node.get_right(), key))            
            return node
        self.set_root(insert(self.get_root(), key))        

    def delete(self, key):
        """Deletes node from tree with given key."""
        def delete(node, key):
            if node.get_key() is key:
                if not node.has_left():
                    node = node.get_right()
                elif not node.has_right():
                    node = node.get_left()
                else:
                    mini = self.minimum(node.get_right())
                    node.set_key(mini.get_key())
                    node.set_right(delete(node.get_right(), mini.get_key()))
            elif key < node.get_key():
                node.set_left(delete(node.get_left(), key))
            else:                
                node.set_right(delete(node.get_right(), key))            
            return node
        self.set_root(delete(self.get_root(), key))


class AVLTree(BinarySearchTree):
    """AVL Tree Class."""
    pass