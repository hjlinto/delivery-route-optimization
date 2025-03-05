from datetime import datetime, timedelta

# Retrieves the status of all packages at a given time
def get_package_statuses(time_check, ht, trucks):
    status_list = []

    input_time = timedelta(hours=time_check.hour, minutes=time_check.minute)

    for package_id in range(1, 41):
        package = ht.lookup(package_id)
        if package:
            # Determines which truck is handling the package
            assigned_truck = next((truck for truck in trucks if package_id in truck.package_list), None)

            # Updates the address for package 9 at correct time
            if package_id == 9 and input_time < timedelta(hours=10, minutes=20):
                package.address = "300 State St"
            elif package_id == 9 and input_time >= timedelta(hours=10, minutes=20):
                package.address = "410 S State St"


            # Handles all packages arriving at 9:05 am
            if package_id in [6, 25, 28, 32]:
                if input_time < timedelta(hours=9, minutes=5):
                    package.status = "Delayed on flight"
                    package.delivery_time = None
                elif input_time < package.loading_time:
                    package.status = "At Hub"
                    package.delivery_time = None
                elif input_time < package.delivery_time:
                    package.status = "En Route"
                    package.delivery_time = None
                else:
                    package.status = "Delivered"

            # Handles all other packages
            if package_id not in [6, 25, 28, 32]:
                if input_time < package.loading_time:
                    package.status = "At Hub"
                    package.delivery_time = None
                elif input_time < package.delivery_time:
                    package.status = "En Route"
                    package.delivery_time = None
                else:
                    package.status = "Delivered"
            # Formats package details for readable UI
            package_info = (
                f"Package: {package.package_id} | Truck: {assigned_truck.truck_id} | Address: {package.address}, {package.city}, {package.state} {package.zip} | "
                f"Deadline: {package.deadline} | {package.status}{f' @ {package.delivery_time}' if package.status == 'Delivered' else ''}"
            )

            status_list.append(package_info)

    return "\n".join(status_list)

def get_all_package_info(ht, trucks):
    info_list = []

    for package_id in range(1, 41):
        package = ht.lookup(package_id)
        if package:
            assigned_truck = next((truck for truck in trucks if package_id in truck.package_list), None)

            package_info = (
                f"Package {package.package_id} | Truck: {assigned_truck.truck_id if assigned_truck else 'N/A'}\n"
                f"{package.address}, {package.city}, {package.state} {package.zip}\n"
                f"Deadline: {package.deadline} |️ {package.weight}kg\n"
                f"{package.notes if package.notes else 'No notes'}\n"
                f"ETA: {package.delivery_time}\n"
                f"{'-' * 60}"
            )

            info_list.append(package_info)

    return "\n".join(info_list)
# Retrieves mileage summary for all trucks
def get_truck_mileage(trucks):
    mileage_list = []
    total_mileage = 0

    for truck in trucks:
        mileage_list.append(f"Truck {truck.truck_id}: {truck.mileage:.2f} miles")
        total_mileage += truck.mileage

    mileage_list.append(f"Total Mileage: {total_mileage:.2f} miles")
    return "\n".join(mileage_list)

# Generates a user interface for tracking package statuses and truck mileage
def main_ui(ht, trucks):
    while True:
        # Displays menu options
        print("\n WGUPS Package Tracking System")
        print("1. Get Package Statuses at a Specific Time")
        print("2. View Truck Mileage Summary")
        print("3. View All Package Info")
        print("4. Exit")

        choice = input("Enter your choice: ")
        # Prompts user for input time in 24-hour format to check package statuses at
        if choice == "1":
            time_input = input("Enter Time (HH:MM, 24-hour format): ")
            try:
                time_check = datetime.strptime(time_input, "%H:%M")
                print("\n Package Status at", time_input)
                print(get_package_statuses(time_check, ht, trucks))
            except ValueError:
                print("Invalid Time Format! Use HH:MM (e.g., 09:00)")
        # Displays summary of individual and collective truck mileage
        elif choice == "2":
            print("\n Truck Mileage Summary")
            print(get_truck_mileage(trucks))
        # Displays all package details
        elif choice == "3":
            print("\n All Package Info")
            print(get_all_package_info(ht, trucks))
        # Exits application
        elif choice == "4":
            print(" Exiting application - Have a great day!")
            break
        # Handles invalid inputs on menu screen and prompts user to try again
        else:
            print(" Invalid Choice! Please enter 1, 2, 3, or 4.")