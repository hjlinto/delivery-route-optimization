from package import Package
class HashTable:
    # Initializes an instance of HashTable
    def __init__(self, initial_capacity = 40):
        self.capacity = initial_capacity
        self.table = [[] for _ in range(initial_capacity)]

    def _hash(self, key):
        return key % self.capacity

    # Inserts a new key-value pair into the hash table
    def insert(self, package_id, address, city, state, zip, deadline, weight, notes, status):
        index = self._hash(package_id)
        bucket = self.table[index]

        package = Package(package_id, address, city, state, zip, deadline, weight, notes, status)

        # Updates key-value pair if found in bucket
        for i, (pid, _) in enumerate(bucket):
            if pid == package_id:
                bucket[i] = (package_id, package)
                return True

        # Inserts key-value pair if not found in bucket
        bucket.append((package_id, package))

    # Searches for matching key-value pair in the hash table
    def lookup(self, package_id):
        index = self._hash(package_id)
        bucket = self.table[index]

        for pid, package in bucket:
            if pid == package_id:
                return package

        return None