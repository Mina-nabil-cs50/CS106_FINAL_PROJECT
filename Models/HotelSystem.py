from Models.guest import Guest
from Models.reservation import Reservation
from Models.payment import Payment
from Models.admin import admin_functions  # Import admin functions
from Models.staff import staff_functions  # Import staff functions


# Define el function el ra2esiya bta3t el menu
def main_menu():
    #Loop infinity (while True) 3shan el menu yfdal yesh8al
    while True:
        print("\nHotel Management System ")
        print("-------------------------------")
        print("1. Admin Functions")
        print("2. Staff Functions")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        # Check lw el user e5tar option 1
        if choice == "1":
            # Call el admin_functions (fe el admin model)
            admin_functions()  
        #check lw el user e5tar option 2
        elif choice == "2":
            #Call el staff_functions 3shan ne3mel execute lel staff options
            staff_functions()  
        #Check lw el user ekhtar option 3
        elif choice == "3":
            #print message en el system haye2fel
            print("Exiting the system. Goodbye!")
            #Exit el loop 3shan el program ye2fel
            break
        #lw el user da5al option 8alat
        else:
            #Print error message lel user 3shan ye3raf en el input 8alat
            print("Invalid choice. Please try again.")


#Check law el file da etran directly
if __name__ == "__main__":
    #Call el main_menu function 3shan el program yebda2 men el menu el ra2esi
    main_menu()


