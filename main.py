# Hunter Linton, Student ID: 012357727
from datetime import timedelta
import csv
from hashtable import HashTable
from package import Package
from truck import Truck
from ui import main_ui

# File paths for CSV data
csv_folder = "csv/"
address_csv = csv_folder + "addresses.csv"
distance_csv = csv_folder + "distances.csv"
packages_csv = csv_folder + "packages.csv"

# Loads address data from CSV
def load_addresses(filename):
    addresses = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            addresses.append(row[1])
    return addresses

# Loads distance matrix from CSV
def load_distances(filename):
    distances = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            distances.append([float(distance) for distance in row])
    return distances

# Loads package information from CSV
def load_packages(filename):
    packages = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            package_id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip = row[4]
            deadline = row[5]
            weight = row[6]
            notes = row[7] if len(row) > 7 else ""
            status = "At Hub"

            packages.append(Package(package_id, address, city, state, zip, deadline, weight, notes, status))

    return packages

# Returns distance between two addresses
def get_distance(address1, address2):
    addresses = load_addresses(address_csv)
    distances = load_distances(distance_csv)

    address1_index = addresses.index(address1)
    address2_index = addresses.index(address2)

    return distances[address1_index][address2_index]

# Sorts packages using the nearest neighbor algorithm
def sort_packages(truck, ht):
    sorted_package_list = []
    current_address = truck.hub_address
    package_list = [ht.lookup(package_id) for package_id in truck.package_list]

    while package_list:
        nearest_package = nearest_neighbor(current_address, package_list)
        sorted_package_list.append(nearest_package.package_id)
        current_address = nearest_package.address
        package_list.remove(nearest_package)

    truck.package_list = sorted_package_list

# Delivers packages using nearest neighbor algorithm
def nearest_neighbor(current_address, package_list):
    nearest_package = None
    nearest_package_distance = None

    for package in package_list:
        if package is not None:
            if nearest_package is None:
                nearest_package = package
                nearest_package_address = nearest_package.address
                nearest_package_distance = get_distance(current_address, nearest_package_address)

            else:
                package_address = package.address
                package_distance = get_distance(current_address, package_address)

                if package_distance < nearest_package_distance:
                    nearest_package = package
                    nearest_package_distance = package_distance

    return nearest_package

# Executes deliveries for a truck and its loaded packages
def execute_deliveries(truck, ht):
    current_address = truck.hub_address
    current_index = 0

    while current_index < len(truck.package_list):
        if current_index >= len(truck.package_list):
            break

        package_id = truck.package_list[current_index]
        package = ht.lookup(package_id)
        truck.en_route(ht)

        distance_traveled = get_distance(current_address, package.address)
        truck.deliver_package(ht, package_id, distance_traveled)
        current_address = package.address
        current_index += 1

    truck.return_to_hub(get_distance(current_address, truck.hub_address))

# Main function to load all data and run application
def main():

    # Loads address and distance data
    addresses = load_addresses(address_csv)
    distances = load_distances(distance_csv)

    # Initializes hash table for storage of package information
    ht = HashTable()
    packages = load_packages(packages_csv)

    # Inserts all packages into the hash table
    for package in packages:
        ht.insert(package.package_id, package.address, package.city, package.state, package.zip, package.deadline,
                  package.weight, package.notes, package.status)

    # Initializes 3 trucks and sets their start times
    truck1 = Truck(truck_id=1)
    truck1.time = timedelta(hours=8, minutes=0, seconds=0)
    truck2 = Truck(truck_id=2)
    truck2.time = timedelta(hours=9, minutes=5, seconds=0)
    truck3 = Truck(truck_id=3)
    truck3.time = timedelta(hours=12, minutes=30, seconds=0)

    # Manually assigns packages to trucks to stay under the total mileage limit of 140 miles
    truck1.package_list = [15, 1, 13, 14, 16, 20, 29, 30, 31, 37, 19, 2, 4, 5]
    for pid in truck1.package_list:
        package = ht.lookup(pid)
        package.loading_time = truck1.time
    truck2.package_list = [6, 25, 34, 40, 3, 17, 18, 21, 36, 38]
    for pid in truck2.package_list:
        package = ht.lookup(pid)
        package.loading_time = truck2.time
    truck3.package_list = [7, 8, 9, 10, 11, 12, 22, 23, 24, 26, 27, 28, 32, 33, 35, 39]
    for pid in truck3.package_list:
        package = ht.lookup(pid)
        package.loading_time = truck3.time

    # Sorts packages for each truck
    sort_packages(truck1, ht)
    sort_packages(truck2, ht)
    sort_packages(truck3, ht)

    # Displays sorted package order for each truck (DEBUG)
    print("Truck 1 Sorted Package Order:", truck1.package_list)
    print("Truck 2 Sorted Package Order:", truck2.package_list)
    print("Truck 3 Sorted Package Order:", truck3.package_list)

    # Display each truck's start time (DEBUG)
    print(f"Truck 1 Start Time: {truck1.time}")
    print(f"Truck 2 Start Time: {truck2.time}")
    print(f"Truck 3 Start Time: {truck3.time}")

    # Executes deliveries for each truck
    execute_deliveries(truck1, ht)
    execute_deliveries(truck2, ht)
    execute_deliveries(truck3, ht)

    # Displays package delivery summaries for all 40 packages (DEBUG)
    print("\n📦 Package Delivery Summary 📦")
    print("=" * 70)
    for package_id in range(1, 41):
        package = ht.lookup(package_id)
        assigned_truck = None
        for truck in [truck1, truck2, truck3]:
            if package_id in truck.package_list:
                assigned_truck = truck.truck_id
                break
        print(f"Package {package_id} | Delivered At: {package.delivery_time} | Address: {package.address},"
              f" {package.city}, {package.state}, {package.zip} | Truck {assigned_truck}")
    print("=" * 70)
    print("All packages delivered successfully!")

    # Calculates and displays mileage for each truck and total mileage (DEBUG)
    total_mileage = truck1.mileage + truck2.mileage + truck3.mileage
    print(f"Truck 1 Mileage: {truck1.mileage:.2f} miles")
    print(f"Truck 2 Mileage: {truck2.mileage:.2f} miles")
    print(f"Truck 3 Mileage: {truck3.mileage:.2f} miles")
    print(f"TOTAL MILEAGE: {total_mileage:.2f} miles")

    # Launches the user interface for queries
    main_ui(ht, [truck1, truck2, truck3])

# Executes the main function when the scrip is run
if __name__ == "__main__":
    main()
