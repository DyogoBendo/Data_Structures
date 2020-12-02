class UnionFind(object):
    def __init__(self, size):
        if size <= 0:
            raise Exception('Size <= 0 is not allowed')
        self._size = size  # The number of elements in this union find
        self._sz = []  # Used to track the size of each of the component
        self._id = []  # id[i] points to the parent of i, if id[i] = i then i is a root node
        self._numcomponents = size  # Tracks the number of components in the union find

        for i in range(size):
            self._id.append(i)  # Link to itself (self root)
            self._sz.append(1)  # Each component is originally of size one

    # Find which component/set 'p' belongs to, takes amortized constant time.
    def find(self, p):
        # Find the root of the component/set
        root = p

        while root != id[root]:
            root = id[root]

        #  Compress the path leading back to the root.
        #  Doing this operation is called "path compression"
        #  and is what gives us amortized time complexity.

        while p != root:
            next = id[p]
            id[p] = root
            p = next

        return root

    # Return whether or not the elements 'p' and
    # 'q' are in the same components/set.
    def connected(self, p, q):
        return self.find(p) == self.find(q)

    # Return the size of the components/set 'p' belongs to
    def componentSize(self, p):
        return self._sz[self.find(p)]

    # Return the number of elements in this UnionFind/Disjoint set
    def size(self):
        return self._size

    # Returns the number of remaining components/sets
    def components(self):
        return self._numcomponents

    # Unify the components/sets containing elements 'p' and 'q'
    def unify(self, p, q):
        # These elements are already in the same group!
        if self.connected(p, q):
            return
        root1 = self.find(p)
        root2 = self.find(q)

        # Merge smaller component/set into the larger one.
        if self.sz[root1] < self._sz[root2]:
            self._sz[root2] += self._sz[root1]
            self._id[root1] = root2
        else:
            self._sz[root1] += self._sz[root2]
            self._id[root2] = root1

        # Since the roots found are different we know that the
        # number of components/sets has decreased by one

        self._numcomponents -= 1




