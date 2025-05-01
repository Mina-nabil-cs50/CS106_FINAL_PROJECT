from Database.db_manager import get_connection
# Removed redundant import of Guest

class Guest:
    def __init__(self, guest_id: int, full_name: str, phone_number: str, email: str, id_document: str):
        self.guest_id = guest_id
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.id_document = id_document

    def update_detail(self, full_name=None, phone_number=None, email=None, id_document=None):
        if full_name:
            self.full_name = full_name
        if phone_number:
            self.phone_number = phone_number
        if email:
            self.email = email
        if id_document:
            self.id_document = id_document

    def save_to_db(self):
        """
        Save the guest to the database.
        """
        conn = get_connection()
        cursor = conn.cursor()

        # Insert or update the guest record
        cursor.execute('''
            INSERT OR REPLACE INTO guests (guest_id, full_name, phone_number, email, id_document)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.guest_id, self.full_name, self.phone_number, self.email, self.id_document))

        conn.commit()
        conn.close()

    @classmethod
    def load_from_db(cls, guest_id):
        """
        Load a guest from the database by guest_id.
        """
        conn = get_connection()
        cursor = conn.cursor()

        # Query the guest record
        cursor.execute('SELECT * FROM guests WHERE guest_id = ?', (guest_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            # Create and return a Guest object
            return cls(guest_id=row[0], full_name=row[1], phone_number=row[2], email=row[3], id_document=row[4])
        else:
            return None

# Save a guest to the database
guest1 = Guest(0, "Mina Nabil", "01280940703", "minasaman310@gmail.com", "passport1234")
guest1.save_to_db()
print("Guest saved to the database.")

# Load the guest from the database
loaded_guest = Guest.load_from_db(0)  # Use the guest_id of the saved guest

# Check if the guest was found and print their details
if loaded_guest:
    print("Guest loaded from database:")
    print(f"ID: {loaded_guest.guest_id}")
    print(f"Name: {loaded_guest.full_name}")
    print(f"Phone: {loaded_guest.phone_number}")
    print(f"Email: {loaded_guest.email}")
    print(f"ID Document: {loaded_guest.id_document}")
else:
    print("Guest not found in the database.")