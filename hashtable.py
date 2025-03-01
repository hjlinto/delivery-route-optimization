class HashTable:
    # Initializes an instance of hash table
    def __init__(self, initial_capacity = 10):
        self.table = []
        for _ in range(initial_capacity):
            self.table.append([])

    # Inserts a new key-value pair into the hash table
    def insert(self, key, value):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Updates key-value pair if found in bucket
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = value
                return True

        # Inserts key-value pair if not found in bucket
        key_value = [key, value]
        bucket_list.append(key_value)
        return True

    # Searches for matching key-value pair in the hash table
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None

    # Removes key-value pair from the hash table
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove(kv)
"""
# Testing
ht = HashTable()
ht.insert("name", "Hunter")
ht.insert("age", 28)
ht.insert("city", "Detroit")
print(ht.search("name"))        # Hunter
print(ht.search("age"))         # 28
print(ht.search("city"))        # Detroit
print(ht.search("country"))     # None
ht.remove("city")
print(ht.search("city"))        # None
"""