from hashtable import HashTable
import csv

class Package:
    def __init__(self, package_id, address, city, state, zip, deadline, weight, notes, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status

    def __str__(self):
        return (f"Package ID: {self.package_id}\n"
                f"Address: {self.address}, {self.city}, {self.state} {self.zip}\n"
                f"Deadline: {self.deadline}\n"
                f"Weight: {self.weight} kgs\n"
                f"Notes: {self.notes if self.notes else 'None'}\n"
                f"Status: {self.status}")

# Test cases
print("=" * 50)
print("Test cases for package.py: ")
pkg = Package(1, "123 Main St", "Salt Lake City", "UT", "84101", "10:30 AM", 5, "Handle with care", "At Hub")
print(pkg)
print("=" * 50)
