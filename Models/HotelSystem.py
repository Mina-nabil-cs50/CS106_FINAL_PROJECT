from Models.guest import Guest
from Models.reservation import Reservation
from Models.payment import Payment
from Models.admin import admin_functions  # Import admin functions
from Models.staff import staff_functions  # Import staff functions


def main_menu():
    while True:
        print("\nHotel Management System ")
        print("-------------------------------")
        print("1. Admin Functions")
        print("2. Staff Functions")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            admin_functions()  
        elif choice == "2":
            staff_functions()  
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()



