from LinkedListNode import DoubleLinkedListNode as Node


class LinkedList(object):
    """Linked List Class."""

    def __init__(self):
        self._head = None

    def get_head(self):
        """Return head of linked list."""
        return self._head

    def set_head(self, node):
        """Set head of linked list."""
        self._head = node

    def empty(self):
        """Return true if list is empty."""
        return self._head is None

    def size(self):
        """Return the number of nodes in the list."""
        cur, count = self._head, 0
        while cur:
            count += 1
            cur = cur.get_next()
        return count

    def print(self):
        """Prints the entire list."""
        cur = self.get_head()
        while cur:
            cur.display(end=' ')
            cur = cur.get_next()
        print()

    def front(self):
        """Return node at the begining of the list."""
        return self.get_head()

    def back(self):
        """Returns node at the end of the list."""
        cur = self.get_head()
        while cur and cur.has_next():
            cur = cur.get_next()
        return cur

    def push_front(self, key):
        """Insert an item at the begining of the list."""
        node = Node(key)
        if not self.empty():
            node.set_next(self.get_head())
            self.get_head().set_prev(node)
        self.set_head(node)

    def push_back(self, key):
        """Append an item to the list."""
        node = Node(key)
        cur = self.get_head()
        while cur and cur.has_next():
            cur = cur.get_next()
        if cur:
            cur.set_next(node)
            node.set_prev(cur)
        else:
            self.set_head(node)

    def pop_front(self):
        """Removes item at the begining of the list."""
        cur = self.get_head()
        if cur.has_next():
            self.set_head(cur.get_next())
            cur.get_next().set_prev(None)
        else:
            self.set_head(None)
        del cur

    def pop_back(self):
        """Removes item at the end of the list."""
        cur, prev = self.get_head(), None
        while cur and cur.has_next():
            prev = cur
            cur = cur.get_next()
        if prev:
            prev.set_next(None)
        else:
            self.set_head(None)
        del cur
        