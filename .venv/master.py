class AmbulanceBookingSystem:
    ambulance_id = 1  # Static variable to track unique ambulance IDs

    def __init__(self):
        self.bookings = []  # List to store booking details

    def add_booking(self, name, surname, phone, location, emergency_type):
        """
        Adds a new ambulance booking with user details.
        """
        booking = {
            "id": AmbulanceBookingSystem.ambulance_id,
            "name": name,
            "surname": surname,
            "phone": phone,
            "location": location,
            "emergency_type": emergency_type
        }

        self.bookings.append(booking)  # Store the booking in the list
        print(f"Ambulance booked successfully, your ID is {AmbulanceBookingSystem.ambulance_id}")
        AmbulanceBookingSystem.ambulance_id += 1  # Increment ID for the next booking

    def view_bookings(self):
        """
        Displays all active bookings.
        """
        if not self.bookings:
            print("No active bookings.")
            return
        print("\n--- Active Bookings ---")
        for booking in self.bookings:
            print(f"ID: {booking['id']} | {booking['name']} {booking['surname']} |"
                  f" Phone: {booking['phone']} | Location: {booking['location']} |"
                  f" Emergency type: {booking['emergency_type']}")

    def cancel_booking(self, ambulance_id):
        """
        Cancels a booking based on the provided ambulance ID.
        """
        for booking in self.bookings:
            if booking["id"] == ambulance_id:
                self.bookings.remove(booking)
                print(f"Booking with ID {ambulance_id} has been successfully canceled.")
                return
        print(f"No booking found with ID {ambulance_id}")

    def mod_choise(self, ambulance_id):
        """
        Allows modification of an existing booking by ID.
        """
        for booking in self.bookings:
            if booking["id"] == ambulance_id:
                while True:
                    print("\n--- Modify booking ---")
                    print("1. Change name")
                    print("2. Change surname")
                    print("3. Change phone number")
                    print("4. Change location")
                    print("5. Change emergency type")
                    print("6. Exit")

                    try:
                        choice = int(input("\nEnter your choice: "))
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        continue

                    if choice == 1:
                        booking["name"] = input("Enter new name: ")
                    elif choice == 2:
                        booking["surname"] = input("Enter new surname: ")
                    elif choice == 3:
                        booking["phone"] = input("Enter new phone: ")
                    elif choice == 4:
                        booking["location"] = input("Enter new location: ")
                    elif choice == 5:
                        booking["emergency_type"] = input("Enter new emergency type: ")
                    elif choice == 6:
                        print("Exiting modification menu...")
                        break
                    else:
                        print("Invalid choice, try again.")
                return
        print(f"No booking found with ID {ambulance_id}")


def main():
    """
    Main function to handle user interactions with the ambulance booking system.
    """
    system = AmbulanceBookingSystem()

    while True:
        print("\n--- Ambulance System ---")
        print("1. Book Ambulance")
        print("2. View bookings")
        print("3. Cancel booking")
        print("4. Modify booking")
        print("5. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid choice, try again.")
            continue

        if choice == 1:
            name = input("Enter your name: ")
            if not name.isalpha():
                print("\nInvalid name.")
                continue

            surname = input("Enter your surname: ")
            if not surname.isalpha():
                print("\nInvalid surname.")
                continue

            try:
                phone_number = int(input("Enter your phone number: "))
            except ValueError:
                print("\nInvalid phone number.")
                continue

            location = input("Enter your location: ")
            if not location.isalpha():
                print("\nInvalid location.")
                continue

            emergency_type = input("Enter your emergency type: ")
            if not emergency_type.isalpha():
                print("\nInvalid emergency type.")
                continue

            system.add_booking(name, surname, phone_number, location, emergency_type)

        elif choice == 2:
            system.view_bookings()

        elif choice == 3:
            try:
                ambulance_id = int(input("Enter ambulance ID to cancel booking: "))
                system.cancel_booking(ambulance_id)
            except ValueError:
                print("\nInvalid ambulance ID.")

        elif choice == 4:
            try:
                ambulance_id = int(input("Enter ambulance ID to modify booking: "))
                system.mod_choise(ambulance_id)
            except ValueError:
                print("\nInvalid ambulance ID.")

        elif choice == 5:
            print("Exiting the system...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
