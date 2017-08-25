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

    def find(self, key):
        """Returns node with given key."""
        cur = self.get_head()
        while cur:
            if cur.get_key() is key:
                return cur
            cur = cur.get_next()

    def reverse(self):
        """Reverses the list."""
        if self.get_head() and self.get_head().has_next():
            cur, prev = self.get_head(), None
            while cur:                
                next_ = cur.get_next()
                cur.set_prev(next_)
                cur.set_next(prev)
                prev = cur
                cur = next_
            self.set_head(prev)

    def node_at(self, position):
        """Returns of node at given position."""
        if position > 0:
            cur = self.get_head()
            count = 1
            while cur and count < position:
                cur = cur.get_next()
                count += 1
            return cur
        return None

    def node_from_end(self, position):
        """Returns node at given position from end."""
        if position > 0:
            temp = self.get_head()
            count = 0
            while temp and count < position:
                temp = temp.get_next()
                count += 1
            if temp:
                cur = self.get_head()
                while temp:
                    cur = cur.get_next()
                    temp = temp.get_next()
                return cur
        return None

    def insert_at(self, key, position):
        """Inserts a node at the given position."""
        if position > 0:
            cur, prev = self.get_head(), None
            count = 1
            while cur and count < position:
                prev = cur
                cur = cur.get_next()
                count += 1
            if count == position:
                node = Node(key)
                if prev:
                    prev.set_next(node)
                    node.set_prev(prev)
                else:
                    self.set_head(node)
                node.set_next(cur)

    def erase_at(self, position):
        """Removes node at the given position."""
        if position > 0:
            cur, prev = self.get_head(), None
            count = 1
            while cur and count < position:
                prev = cur
                cur = cur.get_next()
                count += 1
            if cur:
                cur = cur.get_next()
            if prev:
                prev.set_next(cur)
            else:
                self.set_head(cur)

    def rotate(self, k, clockwise=False):
        """Rotates the list by k positions in the given driection."""
        sz = self.size()
        k %= sz
        if clockwise:
            k = sz - k
        if k > 0:
            cur, prev = self.get_head(), None
            count = 0
            while cur and count < k:
                prev = cur
                cur = cur.get_next()
                count += 1
            prev.set_next(None)
            cur.set_prev(None)
            temp = cur                
            while temp.has_next():
                temp = temp.get_next()
            temp.set_next(self.get_head())
            self.get_head().set_prev(temp)
            self.set_head(cur)

    def mid(self):
        """Return middle node."""
        slow = fast = self.get_head()
        while fast and fast.has_next():
            fast = fast.get_next()
            if fast.has_next():
                slow = slow.get_next()
                fast = fast.get_next()
        return slow
