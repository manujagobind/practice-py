class SingleLinkedListNode(object):
    """Single Linked List Node."""

    def __init__(self, key):
        self._key = key
        self._next = None

    def display(self, end=None):
        """Displays the contents of the node."""
        print(self._key, end=end)
    
    def get_key(self):
        """Return the node's key."""
        return self._key

    def set_key(self, key):
        """Set the node's key."""
        self._key = key

    def get_next(self):
        """Return the node's next element."""
        return self._next

    def set_next(self, next_):
        """Set the node's next element."""
        self._next = next_
    
    def has_next(self):
        """Returns true if node's next is not None."""
        return self._next is not None

class DoubleLinkedListNode(SingleLinkedListNode):
    """Double Linked List Node."""

    def __init__(self, key):
        super(DoubleLinkedListNode, self).__init__(key)
        self._prev = None

    def get_prev(self):
        """Return the node's previous element."""
        return self._prev

    def set_prev(self, prev):
        """Set the node's previous element."""
        self._prev = prev

    def has_prev(self):
        """Returns true if node's previous is not None."""
        return self._prev is not None
    