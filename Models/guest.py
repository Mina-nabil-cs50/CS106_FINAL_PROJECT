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
        Print el object ba3d ma yet7afaz fel database.
        """
        # Print el details bta3t el guest
        print("Saved to database: Guest(guest_id=", self.guest_id, ", full_name='", self.full_name, "', phone_number='", self.phone_number, "', email='", self.email, "', id_document='", self.id_document, "')")

    def update_detail(self, full_name=None, phone_number=None, email=None, id_document=None):
        #Check law el full_name et8ayar w update it
        if full_name:
            self.full_name = full_name
        #Check law el phone_number et8ayar w update it
        if phone_number:
            self.phone_number = phone_number
        #Check law el email et8ayar w update it
        if email:
            self.email = email
        #Check law el id_document et38yar w update it
        if id_document:
            self.id_document = id_document

    def save_to_db(self):
        """
        Save el guest fel database.
        """
        # Get el connection lel database
        conn = get_connection()
        # Create cursor 3shan ne3mel execute lel SQL commands
        cursor = conn.cursor()

        # Insert aw update el guest record fel database
        cursor.execute('''
            INSERT OR REPLACE INTO guests (guest_id, full_name, phone_number, email, id_document)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.guest_id, self.full_name, self.phone_number, self.email, self.id_document))

        # Commit el changes fel database
        conn.commit()
        # Close el connection ba3d el save
        conn.close()

        # Call el print_added_object function 3shan te3mel print lel guest details
        self.print_added_object()


