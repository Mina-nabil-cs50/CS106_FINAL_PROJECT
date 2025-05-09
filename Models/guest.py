from database.db_manager import get_connection


class Guest:  # Creating the guest class
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


# Save meme-named guests to the database
guests = [
    Guest(1, "Shrek Ogre", "1234567890", "shrek@swamp.com", "onion123"),
    Guest(2, "Big Chungus", "0987654321", "chungus@bunny.com", "carrot456"),
    Guest(3, "Pepe Frog", "1112223333", "pepe@memes.com", "sad789"),
    Guest(4, "Doge Dog", "4445556666", "doge@wow.com", "wow101"),
    Guest(5, "Chad Thundercock", "7778889999", "chad@alpha.com", "gymbro202"),
    Guest(6, "Karen Manager", "0001112222", "karen@complain.com", "letme123"),
    Guest(7, "Giga Chad", "3334445555", "giga@chad.com", "alpha456"),
    Guest(8, "Rick Astley", "6667778888", "rick@roll.com", "never123"),
    Guest(9, "John Wick", "9990001111", "john@baba.com", "dog456"),
    Guest(10, "Walter White", "2223334444", "walter@heisenberg.com", "meth789"),
]

for guest in guests:
    guest.save_to_db()

print("All meme-named guests saved to the database.")
