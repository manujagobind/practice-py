class BinaryTreeNode(object):
    """Binary Tree Node."""

    def __init__(self, key):
        self._key = key
        self._height = 0
        self._left, self._right = None, None

    def display(self, end=None):
        """Prints the contents of the current node."""
        print(self._key, self._height, '\t', end=end)

    def get_key(self):
        """Return the node's key."""
        return self._key

    def set_key(self, key):
        """Set the node's key."""
        self._key = key

    def get_height(self):
        """Return height of subtree rooted at this node."""
        return self._height

    def set_height(self, height):
        """Set height of subtree rooted at this node."""
        self._height = height

    def get_left(self):
        """Return the node's left child."""
        return self._left

    def set_left(self, node):
        """Set the node's left child."""
        self._left = node

    def has_left(self):
        """Returns true if node has a left child."""
        return self._left is not None

    def get_right(self):
        """Return the node's right child."""
        return self._right

    def set_right(self, node):
        """Set the node's right child."""
        self._right = node

    def has_right(self):
        """Returns true if node has a right child."""
        return self._right is not None
