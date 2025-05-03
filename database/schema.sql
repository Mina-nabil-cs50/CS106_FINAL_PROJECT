-- Table: guests
CREATE TABLE IF NOT EXISTS guests (
    guest_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    phone_number TEXT,
    email TEXT,
    id_document TEXT
);

-- Table: rooms
CREATE TABLE IF NOT EXISTS rooms (
    room_id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_number TEXT NOT NULL,
    room_type TEXT NOT NULL,
    room_floor INTEGER,
    price_per_night REAL NOT NULL,
    is_occupied INTEGER DEFAULT 0
);

-- Table: payments
CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_id TEXT NOT NULL,
    amount REAL NOT NULL
);

-- Table: reservations
CREATE TABLE IF NOT EXISTS reservations (
    reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    guest_id INTEGER NOT NULL,
    room_id INTEGER NOT NULL,
    check_in_date TEXT NOT NULL,
    check_out_date TEXT NOT NULL,
    FOREIGN KEY (guest_id) REFERENCES guests (guest_id),
    FOREIGN KEY (room_id) REFERENCES rooms (room_id)
);