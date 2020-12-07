DEFAULT_CAPACITY = 3
DEFAULT_LOAD_FACTOR = 0.75


class Entry:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.hash = hash(key)

    #  // We are not overriding the Object equals method
    #   // No casting is required with this method.

    def equals(self, other):
        if hash != other.hash:
            return False
        else:
            return self.key == other.key  # return self.key.equals(other.key)

    def __repr__(self):
        return f'{self.key} => {self.value}'


class HashTableSeparateChaining:
    def __init__(self, capacity, maxLoadFactor):
        if capacity < 0:
            raise Exception('Illegal capacity')
        if maxLoadFactor <= 0:
            raise Exception('Illegal maxLoadFactor')
        self.size = 0
        self.maxLoadFactor = maxLoadFactor
        self.capacity = max(DEFAULT_CAPACITY, capacity)
        self.threshold = int(self.capacity * self.maxLoadFactor)
        self.table = [[], [], []]

    # Returns the number of elements currently inside the hash-table
    def size(self):
        return self.size

    # Returns true/false depending on whether the hash-table is empty
    def is_empty(self):
        return self.size == 0

    # // Converts a hash value to an index. Essentially, this strips the
    #   // negative sign and places the hash value in the domain [0, capacity)
    def normalizeIndex(self, keyHash):
        return (keyHash & 0x7FFFFFFF) % self.capacity

    # Clears all the contents of the hash-table
    def clear(self):
        self.table = [None * self.capacity]
        self.size = 0

    # Returns true/false depending on whether a key is in the hash table
    def contains_key(self, key):
        return self.has_key(key)

    def has_key(self, key):
        bucket_index = self.normalizeIndex(hash(key))
        return self.bucket_seek_entry(bucket_index, key) is not None

    # Insert, put and add all place a value in the hash-table
    def put(self, key, value):
        return self.insert(key, value)

    def add(self, key, value):
        return self.insert(key, value)

    def insert(self, key, value):
        if key is None:
            raise Exception('Null key')
        new_entry = Entry(key, value)
        bucket_index = self.normalizeIndex(new_entry.hash)
        return self.bucket_insert_entry(bucket_index, new_entry)

    #  // Gets a key's values from the map and returns the value.
    #   // NOTE: returns null if the value is null AND also returns
    #   // null if the key does not exists, so watch out..
    def get(self, key):
        if key is None:
            return None
        bucket_index = self.normalizeIndex(hash(key))
        entry = self.bucket_seek_entry(bucket_index, key)
        if entry is not None:
            return entry.value
        return None

    # // Removes a key from the map and returns the value.
    #   // NOTE: returns null if the value is null AND also returns
    #   // null if the key does not exists.
    def remove(self, key):
        if key is None:
            return None
        bucket_index = self.normalizeIndex(hash(key))
        return self.bucket_remove_entry(bucket_index, key)

    # // Removes an entry from a given bucket if it exists
    def bucket_remove_entry(self, bucket_index, key):
        entry = self.bucket_seek_entry(bucket_index, key)
        if entry:
            links = self.table[bucket_index]
            links.remove(entry)
            self.size -= 1
            return entry.value
        return None

    #   // Inserts an entry in a given bucket only if the entry does not already
    #   // exist in the given bucket, but if it does then update the entry value
    def bucket_insert_entry(self, bucket_index, entry):
        bucket = self.table[bucket_index]

        existent_entry = self.bucket_seek_entry(bucket_index, entry.key)

        if not existent_entry:
            bucket.append(entry)
            if self.size + 1 > self.threshold:
                self.resizeTable()
            return None  # Use null to indicate that there was no previous entry
        else:
            oldVal = existent_entry.value
            existent_entry.value = entry.value
            return oldVal

    # Finds and returns a particular entry in a given bucket if it exists, returns null otherwise
    def bucket_seek_entry(self, bucket_index, key):
        if not key:
            return None
        bucket = self.table[bucket_index]
        if bucket is None:
            return None
        for entry in bucket:
            if entry.key == key:
                return entry
        return None

    # Resizes the internal table holding buckets of entries
    def resizeTable(self):
        self.capacity *= 2
        self.threshold = int(self.capacity * self.maxLoadFactor)
        new_table = []

        for i in range(len(self.table)):
            if self.table[i]:
                for entry in self.table[i]:
                    bucket_index = self.normalizeIndex(entry.hash)
                    bucket = new_table[bucket_index]
                    if not bucket:
                        new_table[bucket_index] = bucket = []
                    bucket.append(entry)

                self.table[i] = None

        self.table = new_table

    # Returns the list of keys found within the hash table
    def keys(self):
        keys = []
        for bucket in self.table:
            if bucket:
                for entry in bucket:
                    keys.append(entry.key)
        return keys

    # Returns the list of values found within the hash table
    def values(self):
        values = []
        for bucket in self.table:
            if bucket:
                for entry in bucket:
                    values.append(entry.value)

        return values

    def __repr__(self):
        sb = '{'
        for i in range(len(self.table)):
            if not self.table[i]:
                continue
            for entry in self.table[i]:
                sb += f'{entry}, '
        sb += '}'
        return str(sb)


if __name__ == '__main__':
    hash_table = HashTableSeparateChaining(DEFAULT_CAPACITY, DEFAULT_LOAD_FACTOR)

    hash_table.add('Bobo', 'Jimenez')
    hash_table.add('Linda', 'Nikoly')
    hash_table.add('Cheiroso', 'Dyogo')
    hash_table.add('Otaku', 'Sarah')
    hash_table.add('Gatinho', 'Gabriel')

    print(hash_table.remove('Bobo'))
    print(hash_table.is_empty())
    print(hash_table.get('Otaku'))
    print(hash_table.keys())
    print(hash_table.values())
    print(hash_table.has_key('Cheiroso'))

    print(hash_table)
