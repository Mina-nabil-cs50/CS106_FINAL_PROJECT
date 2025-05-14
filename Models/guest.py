from database.db_manager import get_connection


class Guest:  # Creating the guest class
    def __init__(self, guest_id: int, full_name: str, phone_number: str, email: str, id_document: str, guest_age: int):
        # el function di betet3amel lama te3mel object Guest gedid
        self.guest_id = guest_id
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.id_document = id_document
        self.guest_age = guest_age 

    def print_added_object(self):
        # hena ba3mel print lel data b tari2a sadeqa lel beginner
        print("Saved to database: Guest(guest_id=", self.guest_id, ", full_name=", self.full_name, ", phone_number=", self.phone_number, ", email=", self.email, ", id_document=", self.id_document, ", guest_age=", self.guest_age, ")")

    def update_detail(self, full_name=None, phone_number=None, email=None, id_document=None, guest_age=None):
        # function di law 3ayez te3del 3la ay 7aga fel guest
        if full_name:
            self.full_name = full_name
        if phone_number:
            self.phone_number = phone_number
        if email:
            self.email = email
        if id_document:
            self.id_document = id_document
        if guest_age is not None:  
            self.guest_age = guest_age

    def save_to_db(self):
        # di function bet7ot el guest fel database
        conn = get_connection()
        cursor = conn.cursor()

        # hena by7ot el data fel table guests
        cursor.execute(
            '''
            INSERT OR REPLACE INTO guests (guest_id, full_name, phone_number, email, id_document, guest_age)
            VALUES (?, ?, ?, ?, ?, ?)
            ''',
            (self.guest_id, self.full_name, self.phone_number, self.email, self.id_document, self.guest_age)
        )

        conn.commit()
        conn.close()

        # ba3d ma y7ot el data, by3mel print 3la el object
        self.print_added_object()


