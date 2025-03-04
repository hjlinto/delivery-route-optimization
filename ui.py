from datetime import datetime, timedelta

# Retrieves the status of all packages at a given time
def get_package_statuses(time_check, ht, trucks):
    status_list = []

    input_time = timedelta(hours=time_check.hour, minutes=time_check.minute)

    for package_id in range(1, 41):
        package = ht.lookup(package_id)
        if package:
            # Determine which truck is handling the package
            assigned_truck = next((truck for truck in trucks if package_id in truck.package_list), None)

            # Prints truck assignments and start times (DEBUG) --- NEXT STEP (start times aren't loading properly)
            print(
                f"DEBUG: Package {package.package_id} assigned to Truck {assigned_truck.truck_id if assigned_truck else 'N/A'} | Truck Start Time: {assigned_truck.time if assigned_truck else 'N/A'}")
            print(f"DEBUG: Input Time: {input_time} | Delivery Time: {package.delivery_time}")

            # Handles the status of packages that don't arrive until 9:05 am
            if package.notes and "Delayed on flight---will not arrive to depot until 9:05 am" in package.notes:
                if input_time < timedelta(hours=9, minutes=5):
                    status = "On the Way to the Hub"

            # Assigns status of all packages based on where package is at given time
            if assigned_truck:
                truck_start_time = assigned_truck.time
                if package.delivery_time and package.delivery_time <= input_time:
                    status = "Delivered"
                elif truck_start_time and truck_start_time <= input_time:
                    status = "En Route"
                else:
                    status = "At Hub"

            # Formats package details for readable UI
            package_info = (
                f"Package {package.package_id} | Status: {status}\n"
                f"Address: {package.address}, {package.city}, {package.state}, {package.zip}\n"
                f"Deadline: {package.deadline} | Weight: {package.weight}kg\n"
                f"Notes: {package.notes if package.notes else 'None'}\n"
                f"Truck ID: {assigned_truck.truck_id if assigned_truck else 'N/A'}\n"
                f"Estimated Delivery Time: {package.delivery_time}\n"
                f"{'-' * 60}"
            )

            status_list.append(package_info)

    return "\n".join(status_list)

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
        print("3. Exit")

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
        # Exits application
        elif choice == "3":
            print(" Exiting application - Have a great day!")
            break
        # Handles invalid inputs on menu screen and prompts user to try again
        else:
            print(" Invalid Choice! Please enter 1, 2, or 3.")