from node import Node

#Single Linked List
class LinkedList(object):

    def __init__(self):
        self.head = None;

    def set_head(self, node):
        self.head = node

    #Check whether list is empty
    def empty(self):
        if self.head:
            return False
        return True

    #Get value at the begining of the list
    def front(self):
        if not self.empty():
            return self.head.get_data()
        return None

    #Get value at the end of the list
    def back(self):
        if not self.empty():
            current = self.head
            while current.has_next():
                current = current.get_next()
            return current.get_data()
        return None

    #Push an item at the begining of the list
    def push_front(self, data):
        node = Node(data=data)
        node.set_next(self.head)
        self.set_head(node)

    #Pop an item from the begining of the list and return it's value
    def pop_front(self):
        if not self.empty():
            node = self.head
            self.head = self.head.get_next()
            return node.get_data()
        else:
            raise Exception('Cannot pop from empty list')

    #Push an item to the end of the list
    def push_back(self, data):
        node = Node(data)
        if self.empty():
            self.set_head(node)
        else:
            cursor = self.head
            while cursor.has_next():
                cursor = cursor.get_next()
            cursor.set_next(node)

    #Pop an item from the end of the list and return it
    def pop_back(self):
        if not self.empty():
            current = self.head
            previous = None
            while current.has_next():
                previous = current
                current = current.get_next()
            if previous:
                previous.set_next(None)
                return current.get_data()
            else:
                self.set_head(None)
                return current.get_data()
        else:
            raise Exception('Cannot pop from empty list')

    #Get the number of elements in the list
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next()
        return count

    #Print the list
    def show(self):
        current = self.head
        output = ""
        while current:
            output += str(current.get_data()) + " --> "
            current = current.get_next()
        print output

    #Get value at specified index (indexing begins at 0)
    def value_at(self, index):
        if index >= 0:
            if not self.empty():
                cursor = self.head
                count = 0
                while cursor:
                    if count == index:
                        return cursor.get_data()
                    cursor = cursor.get_next()
                    count += 1
            raise Exception('Index out of bounds')
        else:
            raise Exception('Invalid index')

    #Inserts node at given index
    def insert_at(self, index, data):
        node = Node(data=data)
        if index >= 0:
            if not self.empty():
                current = self.head
                previous = None
                count = 0
                while current:
                    if count == index:
                        if previous:
                            #Any index between 1 and size - 1 (inclusive)
                            previous.set_next(node)
                        else:
                            #When index is zero
                            self.set_head(node)
                        node.set_next(current)
                        return
                    previous = current
                    current = current.get_next()
                    count += 1
                if index == count:
                    #When index is size (last index + 1)
                    previous.set_next(node)
                    return
                #Max index allowed is last index + 1
                raise Exception('Invalid index')
        else:
            raise Exception('Invalid index')

    #Removes node at given index
    def erase_at(self, index):
        if index >= 0:
            if not self.empty():
                current = self.head
                previous = None
                count = 0
                while current:
                    if count == index:
                        if previous:
                            #Any index between 1 and size - 1 (inclusive)
                            previous.set_next(current.get_next())
                        else:
                            #When index is 0
                            self.set_head(current.get_next())
                        return
                    previous = current
                    current = current.get_next()
                    count += 1
            raise Exception('Index out of bounds')
        else:
            raise Exception('Invalid index')

    #Removes the first node in the list with a specific value
    def remove(self, data):
        if not self.empty():
            current = self.head
            previous = None
            while current:
                if current.get_data() == data:
                    if previous:
                        #For any node other than the first node
                        previous.set_next(current.get_next())
                    else:
                        #If first node contains that data
                        self.set_head(current.get_next())
                previous = current
                current = current.get_next()

    #Returns value of node from nth position from the end
    def value_from_end(self, n):
        size = self.size()
        if n > 0 and n <= size:
            index = size - n
            return self.value_at(index)
        elif n <= 0:
            raise Exception('Invalid position')
        else:
            raise Exception('Too few items in list')

    #Reverses a linked list
    def reverse(self):
        #No need to reverse if list has 0 or 1 node
        if self.head:

            a = self.head
            if a.has_next():
                b = a.get_next()
            else:
                #List has only 1 element
                return

            if b.has_next():
                #List has three or more elements
                a.set_next(None)
                while b.has_next():
                    c = b.get_next()
                    b.set_next(a)
                    a, b = b, c
                b.set_next(a)
                self.head = b
            else:
                #List has two elements
                a.set_next(None)
                b.set_next(a)
                self.head = b


    #Swaps nodes in a linked list without swapping the data
    def swap_nodes(self, data1, data2):
        if data1 == data2:
            return

        current1 = self.head
        previous1 = None
        while current1 and current1.get_data() != data1:
            previous1 = current1
            current1 = current1.get_next()

        current2 = self.head
        previous2 = None
        while current2 and current2.get_data() != data2:
            previous2 = current2
            current2 = current2.get_next()

        if current1 is None or current2 is None:
            return

        if previous1:
            previous1.set_next(current2)
        else:
            self.set_head(current2)
        current2.set_next(current1)

        if previous2:
            previous2.set_next(current1)
        else:
            self.set_head(current1)
        current1.set_next(current2)
