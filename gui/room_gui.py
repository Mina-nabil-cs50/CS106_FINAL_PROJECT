import customtkinter
import sqlite3

def get_connection():
    return sqlite3.connect("C:/Users/hanat/Desktop/College/CS106_FINAL_PROJECT/database/hotel.db")

def open_manage_rooms_window():
    win = customtkinter.CTkToplevel()
    win.title("Manage Rooms")
    win.geometry("600x400")
    customtkinter.CTkLabel(win, text="Manage Rooms", font=("Arial", 18)).pack(pady=10)

    # Table header
    header = customtkinter.CTkFrame(win)
    header.pack(fill="x", padx=10)
    for col in ["ID", "Number", "Type", "Floor", "Price", "Occupied"]:
        customtkinter.CTkLabel(header, text=col, width=90).pack(side="left", padx=2)

    # Show all rooms from DB
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT room_id, room_number, room_type, room_floor, price_per_night, is_occupied FROM rooms")
    rooms = cursor.fetchall()
    conn.close()

    # Scrollable frame for rooms
    scroll = customtkinter.CTkScrollableFrame(win, width=560, height=250)
    scroll.pack(padx=10, pady=10)

    for room in rooms:
        row = customtkinter.CTkFrame(scroll)
        row.pack(fill="x", pady=2)
        for value in room:
            customtkinter.CTkLabel(row, text=str(value), width=90).pack(side="left", padx=2)

    # Add Room button (expand later)
    customtkinter.CTkButton(win, text="Add Room", command=lambda: print("Add Room clicked")).pack(pady=10)
