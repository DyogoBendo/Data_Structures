from linked_list import DoublyLinkedList

# Implementing stack with linked_list


class Stack:
    def __init__(self, element):
        self.list = DoublyLinkedList()
        self.push(element)

    def size(self):
        return self.list.size()

    def is_empty(self):
        return self.size() == 0

    def push(self, element):
        self.list.addLast(element)

    def pop(self):
        return self.list.removeLast()

    def peek(self):
        if self.is_empty():
            raise Exception("Empty Stack")
        return self.list.peekLast()

    def __repr__(self):
        return self.list.__repr__()


if __name__ == '__main__':
    stack = []
    # pushing elements to the stack
    stack.append('a')
    stack.append('b')
    stack.append('c')

    print(stack)

    # poping elements
    stack.pop()
    stack.pop()

    print(stack)

    # size of the stack
    print(len(stack))

    # using the class Stack

    another_stack = Stack(10)

    # pushing an element

    another_stack.push(5)
    print(another_stack)

    # popping an element

    another_stack.pop()
    print(another_stack)



