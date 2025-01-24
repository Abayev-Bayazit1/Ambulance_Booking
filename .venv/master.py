


class AmbulanceBookingSystem:
    ambulance_id = 1
    def __init__(self):
        self.bookings = []
    def add_booking(self, name, surname, phone, location, emergency_type):
        booking = {
            "id" : AmbulanceBookingSystem.ambulance_id,
            "name" : name,
            "surname": surname,
            "phone" : phone,
            "location" : location,
            "emergency_type" : emergency_type
        }
        self.bookings.append(booking)
        print(f"Ambulance booked successfully, your ID is {AmbulanceBookingSystem.ambulance_id}")
        AmbulanceBookingSystem.ambulance_id += 1
    def view_bookings(self):
        if not self.bookings:
            print("No active bookings.")
            return
        print("\n--- Active Bookings ---")
        for booking in self.bookings:
            print(f"ID : {booking["id"]}, {booking["name"]} {booking["surname"]}"
                  f"Phone : {booking["phone"]}, Location: {booking["location"]}"
                  f"Emergency type : {booking["emergency_type"]}")
    def cancel_booking(self,ambulance_id):
        for booking in self.bookings:
            if booking["id"] == ambulance_id :
                self.bookings.remove(booking)
                print(f"Booking with ID {ambulance_id} has been successfully canceled.")
                return
            print(f"No booking fount with ID {ambulance_id}")


def main():
    system = AmbulanceBookingSystem()

    while True:
        print("\n--- Ambulance System ---")
        print("1.Book Ambulance")
        print("2.View bookings")
        print("3.Cancel booking")
        print("4.Exit")

        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            name = input("Enter your name: ")
            surname = input("Enter your surname: ")
            phone_number = input("Enter your phone number: ")
            location = input("Enter your location: ")
            emergency_type = input("Enter your emergency type: ")

            system.add_booking(name, surname, phone_number, location, emergency_type)

        elif choice == 2:
             system.view_bookings()

        elif choice == 3:
             ambulance_id = int(input("Enter ambulance id to cancel booking: "))
             system.cancel_booking(ambulance_id)

        elif choice == 4:
            print("Exiting the system...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()


