from database.db_manager import get_connection


class Guest:  # Creating the guest class
    def __init__(self, guest_id: int, full_name: str, phone_number: str, email: str, id_document: str):
        self.guest_id = guest_id
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.id_document = id_document

    def print_added_object(self):
        """
        Print the object after it is saved to the database.
        """
        print(f"Saved to database: Guest(guest_id={self.guest_id}, full_name='{self.full_name}', phone_number='{self.phone_number}', email='{self.email}', id_document='{self.id_document}')")

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

        self.print_added_object()


