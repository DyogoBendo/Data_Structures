class PQueue(object):
    def __init__(self):
        self.heapSize = 0  # The number of elements currently inside the heap
        self.heapCapacity = 0  # The internal capacity of the heap
        self.heap = []  # A dynamic list to track the elements inside the heap

    # Checks if the heap is empty
    def is_empty(self):
        return self.heapSize == 0

    # Clears everything inside the heap, O(n)
    def clear(self):
        for i in range(self.heapCapacity):
            self.heap[i] = None
        self.heapSize = 0

    # Return the size of the heap
    def size(self):
        return self.heapSize

    # Returns the value of the element with the lowest
    # priority in this priority queue. If the priority
    # queue is empty null is returned.

    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    # Removes the root of the heap, O(log(n))
    def poll(self):
        return self.remove_at(0)

    # Test if an element is in heap, O(n)
    def contains(self, elem):
        for i in range(self.heapSize):
            if self.heap[i] == elem:
                return True

    # Adds an element to the priority queue, the
    # element must not be null, O(log(n))
    def add(self, elem):
        if elem is None:
            raise Exception('IllegalArgumentException()')
        if self.heapSize < self.heapCapacity:
            self.heap[self.heapSize] = elem
        else:
            self.heap.append(elem)
            self.heapCapacity += 1
        self.swim(self.heapSize)
        self.heapSize += 1

    # Tests if the value of node i <= node j
    # This method assumes i & j are valid indices, O(1)
    def less(self, i, j):
        node1 = self.heap[i]
        node2 = self.heap[j]
        return node1 <= node2

    # Perform bottom up node swim, O(log(n))
    def swim(self, k):
        # Grab the index of the next parent node WRT to k
        parent = (k - 1) // 2

        # Keep swimming while we have not reached the
        # root and while we're less than our parent.
        while k > 0 and self.less(k, parent):
            # Exchange k with the parent
            self.swap(parent, k)
            k = parent

            # Grab the index of the next parent node WRT to k
            parent = (k - 1) // 2

    # Top down node sink, O(log(n))
    def sink(self, k):
        while True:
            left = 2 * k + 1  # Left  node
            right = 2 * k + 2  # Right node
            smallest = left  # Assume left is the smallest node of the two children

            # Find which is smaller left or right
            # If right is smaller set smallest to be right
            if right < self.heapSize and self.less(right, left):
                smallest = right

            # Stop if we're outside the bounds of the tree
            # or stop early if we cannot sink k anymore
            if left >= self.heapSize or self.less(k, smallest):
                break

            # Move down the tree following the smallest node
            self.swap(smallest, k)
            k = smallest

    # Swap two nodes. Assumes i & j are valid, O(1)
    def swap(self, i, j):
        elem_i = self.heap[i]
        elem_j = self.heap[j]

        self.heap[i] = elem_j
        self.heap[j] = elem_i

    # Removes a particular element in the heap, O(n)
    def remove(self, element):
        if element is None:
            return False
        # Linear removal via search, O(n)
        for i in range(self.heapSize):
            if element == self.heap[i]:
                self.remove_at(i)
                return True

        return False

    # Removes a node at particular index, O(log(n))
    def remove_at(self, i):
        if self.is_empty():
            return None

        self.heapSize -= 1
        removed_data = self.heap[i]
        self.swap(i, self.heapSize)

        # Obliterate the value
        self.heap[self.heapSize] = None

        # Check if the last element was removed
        if i == self.heapSize:
            return removed_data
        elem = self.heap[i]

        # Try sinking element
        self.sink(i)

        # If sinking did not work try swimming
        if self.heap[i] == elem:
            self.swim(i)
        return removed_data

    # Recursively checks if this heap is a min heap
    # This method is just for testing purposes to make
    # sure the heap invariant is still being maintained
    # Called this method with k=0 to start at the root
    def is_min_heap(self, k):
        # If we are outside the bounds of the heap return true
        if k >= self.heapSize:
            return True
        left = 2 * k + 1
        right = 2 * k + 2

        # Make sure that the current node k is less than
        # both of its children left, and right if they exist
        # return false otherwise to indicate an invalid heap

        if left < self.heapSize and not self.less(k, left):
            return False
        if right < self.heapSize and not self.less(k, right):
            return False

        # Recurse on both children to make sure they're also valid heaps
        return self.is_min_heap(left) and self.is_min_heap(right)

    def __repr__(self):
        return self.heap.__repr__()


if __name__ == '__main__':
    teste = PQueue()
    amigos = PQueue()

    teste.add(4)
    teste.add(8)
    teste.add(9)
    teste.add(1)
    teste.add(3)

    print(teste)

    teste.poll()
    teste.poll()
    teste.poll()

    print(teste)

    amigos.add('Dyogo')
    amigos.add('Jimenez')
    amigos.add('Nikoly')
    amigos.add('Daniel')
    amigos.add('Sgobero')

    print(amigos)

    amigos.remove('Sgobero')
    amigos.remove('Dyogo')
    amigos.remove_at(1)

    print(amigos)
