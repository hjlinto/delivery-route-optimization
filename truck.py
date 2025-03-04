import csv
from hashtable import HashTable
from package import Package
from datetime import timedelta

class Truck:
    # Initializes an instance of Truck
    def __init__(self, truck_id):
        self.truck_id = truck_id
        self.package_list = []
        self.speed = 18
        self.mileage = 0.0
        self.time = timedelta(hours = 8, minutes = 0, seconds = 0)
        self.hub_address = "4001 South 700 East"
        self.at_hub = True

    # Adds mileage to the truck's total distance traveled
    def add_mileage(self, miles):
        self.mileage += miles

    # Marks all packages on truck as "En Route and records their departure time
    def en_route(self, ht):
        for package_id in self.package_list:
            package = ht.lookup(package_id)
            package.status = "En route"
            package.en_route_time = self.time

    # Delivers a package, updates its status, and marks the time delivered
    def deliver_package(self, ht, package_id, distance_traveled):
        package = ht.lookup(package_id)
        if package.status in self.package_list:
            self.package_list.remove(package_id)
        self.add_mileage(distance_traveled)
        travel_time = timedelta(minutes=(distance_traveled / self.speed * 60))
        self.time += travel_time
        package.status = "Delivered"
        self.at_hub = False
        package.delivery_time = self.time

    # Returns the truck to the hub and updates time/mileage
    def return_to_hub(self, distance_from_hub):
        self.add_mileage(distance_from_hub)
        self.time += timedelta(minutes=(distance_from_hub / self.speed))
        self.at_hub = True