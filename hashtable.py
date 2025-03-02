class HashTable:
    # Initializes an instance of hash table
    def __init__(self, initial_capacity = 40):
        self.capacity = initial_capacity
        self.table = [[] for _ in range(initial_capacity)]

    def _hash(self, key):
        return key % self.capacity

    # Inserts a new key-value pair into the hash table
    def insert(self, package_id, address, city, state, zip, deadline, weight, notes, status):
        index = self._hash(package_id)
        bucket = self.table[index]

        # Updates key-value pair if found in bucket
        for i, (pid, _) in enumerate(bucket):
            if pid == package_id:
                bucket[i] = (package_id, [address, city, state, zip, deadline, weight, notes, status])
                return True

        # Inserts key-value pair if not found in bucket
        bucket.append((package_id, [address, city, state, zip, deadline, weight, notes, status]))

    # Searches for matching key-value pair in the hash table
    def lookup(self, package_id):
        index = self._hash(package_id)
        bucket = self.table[index]

        for pid, data in bucket:
            if pid == package_id:
                return f"Package ID: {pid}, Details: {data}"
        return None


# Test cases
print("=" * 50)
print("Test cases for hashtable.py: ")
ht = HashTable()
ht.insert(1, "123 Main St", "Salt Lake City", "Utah", "84101", "10:30 AM", 5, "Deliver on truck 2", "En route" )
print(ht.lookup(1))
print("=" * 50)