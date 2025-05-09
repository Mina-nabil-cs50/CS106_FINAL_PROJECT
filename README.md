# Hotel Reservation Management System

A simple offline desktop hotel reservation management system written in Python, using Tkinter for the GUI and SQLite for data storage. Designed to automate booking, check-in/out, and payment operations for small hotels using a single computer.

---

## Features

* Add, update, cancel, and search reservations
* Check in and check out guests
* View room availability and guest list
* Confirm payments and generate simple receipts
* Admin-only access for room management
* User-friendly interface with fast response time
* Data is stored locally using SQLite (no internet needed)

---

## Project Structure

```plaintext
hotel_system/
├── main.py                  # Entry point
├── models/                 # Class files: guest.py, room.py, reservation.py, payment.py, staff.py, admin.py, hotel_system.py
├── database/               # SQLite setup and operations
│   ├── db_manager.py
│   ├── schema.sql
│   └── hotel.db
├── gui/                    # GUI screens using Tkinter
│   ├── button.py
│   └── GUI_v1/
├── utils/                  # Helpers and constants
└── README.md               # This file
```

---

## Technologies Used

* Python 3.10+
* Tkinter for the GUI
* SQLite for the database
* Object-Oriented Programming

---

## Functional Overview

### Staff Functions:

* Add, modify, and cancel reservations
* Check in/check out guests
* Confirm and store payments
* View room and guest information

### Admin Functions:

* Add, update, and delete room data
* View all reservations
* Restricted access to admin-only features

---

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/Mina-nabil-cs50/CS106_FINAL_PROJECT
cd hotel-reservation-system
```

2. Run the setup:

```bash
python main.py
```

Make sure Python is installed and `tkinter` is available (included with most standard installations).

---

## Notes

* This system is designed for use on one local computer
* All data is saved locally in `hotel.db`
* No internet connection required

---

## License

This project is for educational use. You may adapt and extend it freely.

---

## Authors

Built by:

* Mina Nabil
* Hana Tarek
* Karim Samir
* Retaj Yousef
* Retaj Tarek
* Malak Abdelwahed
* Ghalia Nassar
