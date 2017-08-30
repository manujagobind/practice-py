"""Includes classes BinaryTree, BinarySearchTree and AVLTree."""

from TreeNode import BinaryTreeNode as Node

class BinaryTree(object):
    """Binary Tree Class."""

    def __init__(self):
        self._root = None
        self._size = 0

    def get_root(self):
        """Returns root of tree."""
        return self._root

    def set_root(self, node):
        """Set the root of tree to given node."""
        self._root = node

    def get_size(self):
        """Return number of nodes in the tree."""
        return self._size

    def height(self, node):
        """Returns height of subtree rooted at node."""
        if not node:
            return -1
        return node.get_height()

    def inorder(self):
        """Inorder traversal."""
        def inorder(node):
            """Utility function."""
            if node:
                inorder(node.get_left())
                node.display(end=' ')
                inorder(node.get_right())
        inorder(self.get_root())
        print()

    def preorder(self):
        """Inorder traversal."""
        def preorder(node):
            """Utility function."""
            if node:
                node.display(end=' ')
                preorder(node.get_left())
                preorder(node.get_right())
        preorder(self.get_root())
        print()

    def postorder(self):
        """Inorder traversal."""
        def postorder(node):
            """Utility function."""
            if node:
                postorder(node.get_left())
                postorder(node.get_right())
                node.display(end=' ')
        postorder(self.get_root())
        print()

    def levelorder(self):
        """Level order traversal"""
        from collections import deque
        d = deque()
        d.append(self.get_root())
        while len(d) is not 0:
            node = d.popleft()
            node.display(end=' ')
            if node.has_left():
                d.append(node.get_left())
            if node.has_right():
                d.append(node.get_right())
        print()

    def print_level(self, node, level):
        """Prints nodes at a given level."""
        if node:
            if level is 0:
                node.display(end=' ')
            self.print_level(node.get_left(), level-1)
            self.print_level(node.get_right(), level-1)

    def level_by_level(self):
        """Prints nodes level by level."""
        ht = self.height(self.get_root())
        for i in range(ht+1):
            self.print_level(self.get_root(), i)
            print()


class BinarySearchTree(BinaryTree):
    """Binary Search Tree Class."""

    def __init__(self):
        super(BinarySearchTree, self).__init__()

    def minimum(self, node=None):
        """Returns node with minimum key value."""
        if not node:
            node = self.get_root()
        while node.has_left():
            node = node.get_left()
        return node

    def maximum(self, node=None):
        """Returns node with maximum key value."""
        if not node:
            node = self.get_root()
        while node.has_right():
            node = node.get_right()
        return node

    def insert(self, key):
        """Inserts new node in the tree."""
        def insert(node, key):
            """Utility function."""
            if not node:
                node = Node(key)
            elif key < node.get_key():
                node.set_left(insert(node.get_left(), key))
            elif key > node.get_key():
                node.set_right(insert(node.get_right(), key))
            node.set_height(1 + max(self.height(node.get_left()),
                                    self.height(node.get_right())))
            return node
        self.set_root(insert(self.get_root(), key))
        self._size += 1

    def delete(self, key):
        """Deletes node from tree with given key."""
        def delete(node, key):
            """Utility function."""
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
            if node:
                node.set_height(1 + max(self.height(node.get_left()),
                                        self.height(node.get_right())))
            return node
        self.set_root(delete(self.get_root(), key))
        self._size -= 1


class AVLTree(BinarySearchTree):
    """AVL Tree Class."""

    def __init__(self):
        super(AVLTree, self).__init__()

    def balance(self, node):
        """Returns difference in heights of left and right subtrees."""
        if node:
            return self.height(node.get_left()) - self.height(node.get_right())
        return 0

    def left_rotate(self, node):
        """Performs left rotation."""
        pivot = node.get_right()
        T = pivot.get_left()
        pivot.set_left(node)
        node.set_right(T)
        node.set_height(1 + max(self.height(node.get_left()),
                                self.height(node.get_right())))
        pivot.set_height(1 + max(self.height(pivot.get_left()),
                                 self.height(pivot.get_right())))
        return pivot

    def right_rotate(self, node):
        """Performs right rotation."""
        pivot = node.get_left()
        T = pivot.get_right()
        pivot.set_right(node)
        node.set_left(T)
        node.set_height(1 + max(self.height(node.get_left()),
                                self.height(node.get_right())))
        pivot.set_height(1 + max(self.height(pivot.get_left()),
                                 self.height(pivot.get_right())))
        return pivot

    def insert(self, key):
        """Inserts new node in the tree."""
        def insert(node, key):
            """Utility function."""
            if not node:
                node = Node(key)
            elif key < node.get_key():
                node.set_left(insert(node.get_left(), key))
            elif key > node.get_key():
                node.set_right(insert(node.get_right(), key))

            node.set_height(1 + max(self.height(node.get_left()),
                                    self.height(node.get_right())))
            bal = self.balance(node)

            if bal > 1:
                if key < node.get_left().get_key():
                    node = self.right_rotate(node)
                else:
                    node.set_left(self.left_rotate(node.get_left()))
                    node = self.right_rotate(node)
            if bal < -1:
                if key > node.get_right().get_key():
                    node = self.left_rotate(node)
                else:
                    node.set_right(self.right_rotate(node.get_right()))
                    node = self.left_rotate(node)
            return node

        self.set_root(insert(self.get_root(), key))
        self._size += 1

    def delete(self, key):
        """Deletes node from tree with given key."""
        def delete(node, key):
            """Utility function."""
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

            if node:
                node.set_height(1 + max(self.height(node.get_left()),
                                        self.height(node.get_right())))
                bal = self.balance(node)

                if bal > 1:
                    if self.balance(node.get_left()) >= 0:
                        node = self.right_rotate(node)
                    else:
                        node.set_left(self.left_rotate(node.get_left()))
                        node = self.right_rotate(node)
                if bal < -1:
                    if self.balance(node.get_right()) <= 0:
                        node = self.left_rotate(node)
                    else:
                        node.set_right(self.right_rotate(node.get_right()))
                        node = self.left_rotate(node)
            return node

        self.set_root(delete(self.get_root(), key))
        self._size -= 1
