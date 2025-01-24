




def main():
    system = AmbulanceBookingSystem()

    while True:
        print("\n--- Ambulance System ---")
        print("1.Book Ambulance")
        print("2.View bookings")
        print("3.Cancel booking")
        print("4.Exit")

        choice = int(input("\nEnter your choice: "))
        if choice == "1":
            name = input("Enter your name: ")
            surname = input("Enter your surname: ")
            phone_number = input("Enter your phone number: ")
            location = input("Enter your location: ")
            emergency_type = input("Enter your emergency type: ")

            system.add_booking(name, surname, phone_number, location, emergency_type)

        elif choice == "2":
             system.view_bookings()

        elif choice == "3":
             ambulance_id = int(input("Enter ambulance id to cancel booking: "))
             system.cancel_booking(ambulance_id)

        elif choice == "4":
            print("Exitig the system...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()


