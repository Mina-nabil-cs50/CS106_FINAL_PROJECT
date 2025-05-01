from Models.guest import Guest  # Import the Guest class

if __name__ == "__main__":
    # Load guest1 from the database
    loaded_guest = Guest.load_from_db(0)  # Use the guest_id of guest1

    if loaded_guest:
        print("Guest loaded from database:")
        print(f"ID: {loaded_guest.guest_id}")
        print(f"Name: {loaded_guest.full_name}")
        print(f"Phone: {loaded_guest.phone_number}")
        print(f"Email: {loaded_guest.email}")
        print(f"ID Document: {loaded_guest.id_document}")
    else:
        print("Guest not found in the database.")
