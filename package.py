class Package:
    # Initializes an instance of Package
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
        self.en_route_time = None
        self.delivery_time = None

    # Returns a string representation of the package details
    def __str__(self):
        return (f"Package ID: {self.package_id}\n"
                f"Address: {self.address}, {self.city}, {self.state} {self.zip}\n"
                f"Deadline: {self.deadline}\n"
                f"Weight: {self.weight} kgs\n"
                f"Notes: {self.notes if self.notes else 'None'}\n"
                f"Status: {self.status}")