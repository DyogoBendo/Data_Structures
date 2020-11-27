class Node(object):
    """
    Internal node class to represent data
    """

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return str(self.data)


class DoublyLinkedList(object):
    """
    Dynamic Array Class (Similar to Python List)
    """

    def __init__(self):
        self.llSize = 0
        self.head = None
        self.tail = None
        self.travIter = None

    def __len__(self):
        """
        Return number of elements sorted in array
        """
        return self.llSize

    def clear(self):
        """
        Empty this linked list, O(n)
        """
        trav = self.head
        while trav is not None:
            next = trav.next
            trav.prev = trav.next = None
            trav.data = None
            trav = next

        self.head = None
        self.tail = None
        trav = None
        self.llSize = 0

    def size(self):
        """
        Return the size of this linked list
        """
        return self.llSize

    def is_empty(self):
        """
        Is this linked list empty?
        """
        return self.size() == 0

    def add(self, elem):
        """
        Add an element to the tail of the linked list, O(1)
        """
        self.addLast(elem)

    def addLast(self, elem):
        """
        Add a node to the tail of the linked list, O(1)
        """
        if self.is_empty():
            self.head = self.tail = Node(elem, None, None)
        else:
            self.tail.next = Node(elem, self.tail, None)
            self.tail = self.tail.next

        self.llSize += 1

    def addFirst(self, elem):
        """
        Add an element to the beginning of this linked list, O(1)
        """
        if self.is_empty():
            self.head = self.tail = Node(elem, None, None)
        else:
            self.head.prev = Node(elem, None, None)
            self.head = self.head.prev

        self.llSize += 1

    def addAt(self, index, data):
        """
        Add an element at a specified index
        """
        if index < 0:
            raise Exception(f'index should not be negative. The value of index was {index}')

        if index == 0:
            self.addFirst(data)
            return

        if index == self.llSize:
            self.addLast(data)
            return

        temp = self.head
        for i in range(0, index - 1):
            temp = temp.next

        newNode = Node(data, temp, temp.next)
        temp.next.prev = newNode
        temp.next = newNode

        self.llSize += 1

    def peekFirst(self):
        """
        Check the value on the first node if it exists, O(1)
        """
        if self.is_empty():
            raise Exception("Empty list")
        return self.head.data

    def peekLast(self):
        """
        Check the value of the last node if it exists, O(1)
        """

        if self.is_empty():
            raise Exception("Empty List")
        return self.tail.data

    def removeFirst(self):
        """
        Remove the first value at the head of the linked list, O(1)
        """
        # Can't remove data from an empty list
        if self.is_empty():
            raise Exception("Empty list")

        # Extract the data at the head and move
        # the head pointer forwards one node
        data = self.head.data
        self.head = self.head.next
        self.llSize -=1

        # if the list is empty set the tail to null
        if self.is_empty():
            self.tail = None

        # Do a memory cleanup of the previus node
        else:
            self.head.prev = None

        # Return the data tha was at the first node we just removed
        return data

    def removeLast(self):
        """
        remove the last value at the tail of the linked list, O(1)
        """
        # Can't remove data from an empty list
        if self.is_empty():
            raise Exception("Empty list")

        # Extract te data at the tail and move
        # the tail pointer backwards one node

        data = self.tail.data
        self.tail = self.tail.prev
        self.llSize -= 1

        if self.is_empty():
            self.head = None

        # Do a memory clean of the node that was just removed
        else:
            self.tail.next = None

        # Return the data that was in the last node we just removed
        return data

    def __remove__(self, node):
        """
        Remove an arbitrary node from the linked list, O(1)
        """
        # if the node to remove is somewhere either at the head or the tail handle those independently
        if node.prev is None:
            return self.removeFirst()
        if node.next is None:
            return self.removeLast()

        # Make the pointers from the adjacents nodes skip over 'node'
        node.next.prev = node.prev
        node.prev.next = node.next

        # Temporarily store the data we want to return
        data = node.data

        # Memory cleanup
        node.data = None
        node.next = None
        node.prev = None
        node = None

        self.llSize -= 1

        # Return the data in the node we just removed
        return data


    def removeAt(self, index):
        """
        Remove a node at a particular index, O(n)
        """
        # make sure the index provided is valid
        if index < 0 or index >= self.llSize:
            raise ValueError("wrong index")

        # Search from the fron of the list
        if index < self.llSize / 2:
            i = 0
            trav = self.head
            while i != index:
                i += 1
                trav = trav.next

        # Search from the back of the list
        else:
            i = self.llSize - 1
            trav = self.tail
            while i != index:
                i -= 1
                trav = trav.prev

        return self.__remove__(trav)

    def remove(self, object):
        """
        Remove a particular value in the linked list, O(n)
        """
        trav = self.head

        # Support searching for null
        if object is None:
            trav = self.head
            while trav is not None:
                if trav.data is None:
                    self.__remove__(trav)
                    return True
                trav = trav.next

        # Search for non null object
        else:
            trav = self.head
            while trav is not None:
                if object == trav.data:
                    self.__remove__(trav)
                    return True

                trav = trav.next

        return False

    def indexOf(self, obj):
        """
        Find the index of a particular value in the linked list, O(n)
        """
        index = 0
        trav = self.head

        # Support search for null
        if obj is None:
            while trav is not None:
                if trav.data is None:
                    return index

                trav = trav.next
                index += 1

        # Search for non null
        else:
            while trav is not None:
                if obj == trav.data:
                    return index
                trav = trav.next
                index += 1

        return -1

    def contains(self, obj):
        """
        Check if a value is cointained within the linked list
        """
        return self.indexOf(obj) != -1

    def __iter__(self):
        """
        called when iteration is initialized
        """
        self.travIter = self.head
        return self

    def __next__(self):
        """
        To move to the next element
        """

        # Stop iteration if limit is reached
        if self.travIter is None:
            raise StopIteration

        # Store current travIter.data
        data = self.travIter.data
        self.travIter = self.travIter.next

        # Else increment and return old value
        return data

    def __repr__(self):
        sb = ""
        sb = sb + '[ '
        trav = self.head
        while trav is not None:
            sb = sb + str(trav.data)
            if trav.next is not None:
                sb = sb + ', '

            trav = trav.next

        sb = sb + ' ]'
        return str(sb)
