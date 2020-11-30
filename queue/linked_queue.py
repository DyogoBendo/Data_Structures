from queue import Queue
from linked_list import DoublyLinkedList


class LinkedQueue(Queue):
    """
    A linked list implementation of a queue
    """
    def __init__(self):
        self.list = DoublyLinkedList()
        self.iterList = iter(self.list)

    def size(self):
        """
        Return the size of the queue
        """
        return self.list.size()

    def is_empty(self):
        """
        Return whether or not the queue is empty
        """
        return self.list.is_empty()

    def peek(self):
        """
        Poll an element from the front of the queue
        The method throws an error if the queue is empty
        """
        if self.is_empty():
            raise Exception('Queue Empty')
        return self.list.peekFirst()

    def poll(self):
        """
        Pull an element from the front of the queue
        The method throws an error if the queue is empty
        """
        if self.is_empty():
            raise Exception('Queue Empty')
        return self.list.removeFirst()

    def offer(self, elem):
        """
        Add an element at the back of the queue
        """
        self.list.addLast(elem)

    def __iter__(self):
        """
        Called when iteration is initialized

        Return an iterator to allow the user to traverse
        through the elements found inside the queue
        """
        self.iterList = iter(self.list)
        return self

    def __next__(self):
        """
        To move to next element
        """
        return next(self.iterList)


if __name__ == '__main__':
    q = LinkedQueue()

    # Adding elements
    q.offer("Dyogo")
    q.offer("Nikoly")
    q.offer("Jimenez")
    q.offer("Sarah")
    q.offer("Jefferson")

    print(f"remove: {q.poll()}")  # remove Dyogo
    print(f"remove: {q.poll()}")  # remove Nikoly
    print(f"remove: {q.poll()}")  # remove Jimenez
    print(f"remove: {q.poll()}")  # remove Sarah

    print()

    print(f"Is it empty? {q.is_empty()}")  # False

    print()

    # Adding new elements
    q.offer("Jonas")
    q.offer("Augusto")
    q.offer("Vinivius")

    print(f"remove: {q.poll()}")  # remove Jefferson
    print(f"remove: {q.poll()}")  # remove Jonas
    print(f"remove: {q.poll()}")  # remove Augusto

    print()

    print(f"peek: {q.peek()}")  # Vinivius




