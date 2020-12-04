from collections import deque
import random


class Node:
    """
    Internal node containing node references
    and the actual node data
    """
    def __init__(self, left, right, elem):
        self.data = elem
        self.left = left
        self.right = right


def find_min(node):
    """
    Helper method to find the leftmost node (which has the smallest value)
    """
    while node.left is not None:
        node = node.left
    return node


class BinarySearchTree:
    """
    An implementation of an indexed binary heap priority queue
    """
    def __init__(self):

        # Tracks the number of nodes in this BST
        self.nodeCount = 0

        # This BST is a rooted tree so we maintain a handle on the root node
        self.root = None

        self.stackPreOrderIter = deque()

    def is_empty(self):
        """
        Check if this binary tree is empty
        """
        return self.size() == 0

    def size(self):
        """
        Get the number of nodes in this binary tree
        """
        return self.nodeCount

    def add(self, elem):
        """
            Add an element to this binary tree.
            Returns true if we successfully perform an insertion
        """

        # Check if the value already exists in this
        # binary tree, if it does ignore adding it

        if self.contains(elem):
            return False

        # Otherwise add this element to the binary tree
        else:
            self.root = self.__add(self.root, elem)
            self.nodeCount += 1
            return True

    def __add(self, node, elem):

        # Base case: found a leaf node
        if node is None:
            node = Node(None, None, elem)

        else:
            # Pick a subtree to insert element
            if elem < node.data:
                node.left = self.__add(node.left, elem)
            else:
                node.right = self.__add(node.right, elem)

        return node

    def remove(self, elem):
        """
        Remove a value from this binary tree if it exists, O(n)
        """

        # Make sure the node we want to remove
        # actually exists before we remove it
        if self.contains(elem):
            self.root = self.__remove(self.root, elem)
            self.nodeCount -= 1
            return True

        return False

    def __remove(self, node, elem):
        if node is None:
            return None

        cmp = elem < node.data

        if elem == node.data:

            # This is the case with only a right subtree or
            # no subtree at all. In this situation just
            # swap the node we wish to remove with its right child

            if node.left is None:

                right_child = node.right

                node.data = None

                return right_child

            # This is the case with only a left subtree or
            # no subtree at all. In this situation just
            # swap the node we wish to remove with its left child
            elif node.right is None:

                left_child = node.left

                node.data = None

                return left_child

            # When removing a node from a binary tree with two links the
            # sucessor of the node being removed can either be the largest
            # value in the left subtree or the smallest value in the right
            # subtree. In this implementation I have decided to find the
            # smallest value in the right subtree which can be found by
            # transversing as far left as possible in the right subtree
            else:

                # Find the leftmost node in the right subtree
                tpm = find_min(node.right)

                # Swap the data
                node.data = tpm.data

                # Go into the right subtree and remove the leftmost node we
                # found and swapped data with. This prevents us from having
                # two nodes in our tree with the same value
                node.right = self.__remove(node.right, tpm.data)

                # if instead we wanted to find the largest node in the left
                # subtree as opposed to smallest node in the right subtree
                # here is what we would do:
                # Node  tpm = findMax(node.left)
                # node.data = tpm.daa
                # node.left = self.__remove(node.left, tpm.data)

        # Dig into left subtree, the value we're looking
        # for is smaller than the current value
        elif cmp is True:
            node.left = self.__remove(node.left, elem)

            # Dig into right subtree, the value we're looking
            # for this greater than the current value
        elif cmp is False:
            node.right = self.__remove(node.right, elem)

            # Found the node we wish to remove
        else:
            return None

        return node

    def contains(self, elem):
        """
        return true if the element exists in the three
        """
        return self.__contains(self.root, elem)

    def __contains(self, node, elem):
        """
        private recursive method to find an element in the three
        """

        # Base case: reached bottom, value not found
        if node is None:
            return False

        cmp = elem < node.data

        # We found the value we were looking for:
        if elem == node.data:
            return True

        # Dig into the left subtree because the value we're
        # looking for is smaller than the current value
        elif cmp:
            return self.__contains(node.left, elem)

        # Dig into the right subtree because the value we`re
        # looking for is smaller than the current value
        elif not cmp:
            return self.__contains(node.right, elem)

    def height(self):
        """
        Computes the height of the tree , O(n)
        """
        return self.__height(self.root)

    def __height(self, node):
        """
        Recursive helper method to compute the height of the tree
        """
        if node is None:
            return 0
        return max(self.__height(node.left), self.__height(node.right)) + 1

    def traverse(self, order):
        """
        This method returns an iterator for a given TreeTraversalOrder
        The ways in which you can traverse the tree are in four different ways:
        preorder, inorder, postorder and levelorder
        """

        if order == 'PRE_ORDER':
            return self.pre_order_traversal()
        if order == 'IN_ORDER':
            return self.in_order_traversal()
        if order == 'POST_ORDER':
            return self.post_order_traversal()
        if order == 'LEVEL_ORDER':
            return self.level_order_traversal()

        return None

    def __iter__(self):
        """
        Called when iteration is initialized
        Returns as iterator to traverse the tree in pre order
        """
        self.expectedNodeCount = self.nodeCount
        self.stackPreOrderIter.clear()
        self.stackPreOrderIter.append(self.root)
        return self

    def __next__(self):
        """
        To move to next element
        """
        if self.expectedNodeCount != self.nodeCount:
            raise Exception('ConcurrentModificationException')

        if self.root is None or len(self.stackPreOrderIter) == 0:
            raise StopIteration

        node = self.stackPreOrderIter.popleft()
        if node.right is not None:
            self.stackPreOrderIter.append(node.right)
        if node.left is not None:
            self.stackPreOrderIter.append(node.left)

        return node.data

    def pre_order_traversal(self):
        """
        Returns as iterator to traverse the tree in pre order
        """
        if self.root is None:
            return None

        stack = deque()
        stack.append(self.root)

        while True:
            if self.root is None or len(stack) == 0:
                break

            node = stack.pop()
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

            yield node.data

        else:
            raise StopIteration

    def in_order_traversal(self):
        """
        Returns as iterator to traverse the tree in order
        """
        stack = deque()
        stack.append(self.root)
        trav = self.root
        while True:
            if self.root is None or len(stack) == 0:
                break

            # Dig left
            while trav is not None and trav.left is not None:
                stack.append(trav.left)
                trav = trav.left

            node = stack.pop()

            # Try moving down right once
            if node.right is not None:
                stack.append(node.right)
                trav = node.right

            yield node.data
        else:
            raise StopIteration

    def post_order_traversal(self):
        """
        Return as iterator to traverse the tree in post order
        """
        stack1 = deque()
        stack1.append(self.root)
        stack2 = deque()

        while len(stack1) != 0:
            node = stack1.pop()
            if node is not None:
                stack2.append(node)
                if node.left is not None:
                    stack1.append(node.left)
                if node.right is not None:
                    stack1.append(node.right)

        while True:
            if self.root is None or len(stack2) == 0:
                break

            node = stack2.pop()

            yield node.data
        else:
            raise StopIteration

    def level_order_traversal(self):
        """
        Returns as iterator to traverse the tree in level order
        """
        queue = deque()
        queue.append(self.root)

        while True:
            if self.root is None or len(queue) == 0:
                break

            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

            yield node.data
        else:
            raise StopIteration

    def display(self):
        lines, *_ = self.display_aux(self.root)
        for line in lines:
            print(line)

    def display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child
        if node.right is None and node.left is None:
            line = f'{node.data}'
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self.display_aux(node.left)
            s = f'{node.data}'
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self.display_aux(node.right)
            s = '%s' % node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.display_aux(node.left)
        right, m, q, y = self.display_aux(node.right)
        s = '%s' % node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


if __name__ == '__main__':
    arvore_binaria = BinarySearchTree()

    lista_alunos = ['Nikoly', 'Jimenez', 'Daniel', 'Dyogo', 'Sarah', 'Aluisio', 'Annalucia', 'Augusto',
                    'Becker', 'Brambilla', 'Caio', 'Ditz', 'Erick', 'Fabio', 'Felipe', 'Gaby', 'Heck',
                    'Joao', 'Kelvin', 'Lara', 'Laurentino', 'Luiz', 'Lukas', 'Matheus', 'Nicolas',
                    'Nicolly', 'Obregon', 'Pedro da Mata', 'Pedro Henrique', 'Rubens', 'Andressa S', 'Andressa V',
                    'Sgobero', 'Vinicius', 'Xavier', 'Thomas', 'Pachola']

    while lista_alunos:
        escolha_aleatoria = random.choice(lista_alunos)
        lista_alunos.remove(escolha_aleatoria)
        arvore_binaria.add(escolha_aleatoria)

    print(arvore_binaria.contains('Dyogo'))
    print(arvore_binaria.contains('Daniel'))
    print(arvore_binaria.height())

    print(arvore_binaria.remove('Jimenez'))

    arvore_binaria.display()

    print('IN ORDER \n')
    for i in arvore_binaria.traverse('IN_ORDER'):
        print(i)

    print('\n POST ORDER \n')
    for i in arvore_binaria.traverse('POST_ORDER'):
        print(i)

    print('\n LEVEL ORDER \n')
    for i in arvore_binaria.traverse('LEVEL_ORDER'):
        print(i)

    print('\n PRE ORDER \n')
    for i in arvore_binaria.traverse('PRE_ORDER'):
        print(i)