import tkinter as tk
import customtkinter
from room_gui import open_manage_rooms_window
from Models.admin import (
    edit_staff, remove_staff, ensure_admin_and_staff,
    edit_room, remove_room, admin_functions
)
from Models.room import Room
from Models.staff import Staff
from tkinter import messagebox

def open_manage_staff_window():
    win = customtkinter.CTkToplevel()
    win.title("Manage Staff")
    win.geometry("400x300")
    customtkinter.CTkLabel(win, text="Manage Staff", font=("Arial", 16)).pack(pady=10)

    def on_edit():
        try:
            staff_id = int(staff_id_entry.get())
            edit_staff(staff_id)
            messagebox.showinfo("Success", f"Staff {staff_id} edited.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def on_remove():
        try:
            staff_id = int(staff_id_entry.get())
            remove_staff(staff_id)
            messagebox.showinfo("Success", f"Staff {staff_id} removed.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    customtkinter.CTkLabel(win, text="Staff ID:").pack(pady=5)
    staff_id_entry = customtkinter.CTkEntry(win)
    staff_id_entry.pack()

    customtkinter.CTkButton(win, text="Edit Staff", command=on_edit).pack(pady=5)
    customtkinter.CTkButton(win, text="Remove Staff", command=on_remove).pack(pady=5)

def open_remove_staff_window():
    win = customtkinter.CTkToplevel()
    win.title("Remove Staff")
    win.geometry("300x150")
    customtkinter.CTkLabel(win, text="Staff ID:").pack()
    staff_id_entry = customtkinter.CTkEntry(win)
    staff_id_entry.pack()

    def on_remove():
        try:
            staff_id = int(staff_id_entry.get())
            remove_staff(staff_id)
            messagebox.showinfo("Success", f"Staff {staff_id} removed.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    customtkinter.CTkButton(win, text="Remove Staff", command=on_remove).pack(pady=10)

def open_change_season_window():
    win = customtkinter.CTkToplevel()
    win.title("Change Season")
    win.geometry("300x150")
    customtkinter.CTkLabel(win, text="Enter new season:").pack(pady=10)
    season_entry = customtkinter.CTkEntry(win)
    season_entry.pack(pady=5)

    def on_change():
        season = season_entry.get()
        # Implement your logic to change the season here
        messagebox.showinfo("Success", f"Season changed to {season}")
        win.destroy()

    customtkinter.CTkButton(win, text="Change", command=on_change).pack(pady=10)

def open_admin_menu():
    win = customtkinter.CTkToplevel()
    win.title("Admin Dashboard")
    win.geometry("400x600")
    customtkinter.CTkLabel(win, text="Admin Dashboard", font=("Arial", 18)).pack(pady=20)
    customtkinter.CTkButton(win, text="Add Room", command=open_add_room_window).pack(pady=5)
    customtkinter.CTkButton(win, text="Edit Room", command=open_edit_room_window).pack(pady=5)
    customtkinter.CTkButton(win, text="Remove Room", command=open_remove_room_window).pack(pady=5)
    customtkinter.CTkButton(win, text="Add Staff", command=open_add_staff_window).pack(pady=5)
    customtkinter.CTkButton(win, text="Edit Staff", command=open_manage_staff_window).pack(pady=5)
    customtkinter.CTkButton(win, text="Remove Staff", command=open_remove_staff_window).pack(pady=5)
    customtkinter.CTkButton(win, text="Change Season", command=open_change_season_window).pack(pady=5)
    customtkinter.CTkButton(win, text="Manage Rooms (Table View)", command=open_manage_rooms_window).pack(pady=5)
    customtkinter.CTkButton(win, text="Logout", command=win.destroy).pack(pady=20)

def open_add_room_window():
    win = customtkinter.CTkToplevel()
    win.title("Add Room")
    win.geometry("350x350")

    entries = {}
    for label in ["Room ID", "Room Type", "Room Floor", "Room Number", "Price Per Night", "Available (yes/no)"]:
        customtkinter.CTkLabel(win, text=label).pack()
        entry = customtkinter.CTkEntry(win)
        entry.pack()
        entries[label] = entry

    def on_add():
        try:
            room_id = int(entries["Room ID"].get())
            room_type = entries["Room Type"].get()
            room_floor = int(entries["Room Floor"].get())
            room_number = entries["Room Number"].get()
            price_per_night = float(entries["Price Per Night"].get())
            available = entries["Available (yes/no)"].get().lower() == "yes"
            room = Room(room_id, room_type, room_floor, room_number, price_per_night, available)
            room.save_to_db()
            messagebox.showinfo("Success", "Room added successfully!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    customtkinter.CTkButton(win, text="Add Room", command=on_add).pack(pady=10)

def open_edit_room_window():
    win = customtkinter.CTkToplevel()
    win.title("Edit Room")
    win.geometry("300x200")
    customtkinter.CTkLabel(win, text="Room ID:").pack()
    room_id_entry = customtkinter.CTkEntry(win)
    room_id_entry.pack()

    def on_edit():
        try:
            room_id = int(room_id_entry.get())
            edit_room(room_id)
            messagebox.showinfo("Success", f"Room {room_id} edited (via CLI prompts).")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    customtkinter.CTkButton(win, text="Edit Room (CLI prompts)", command=on_edit).pack(pady=10)

def open_remove_room_window():
    win = customtkinter.CTkToplevel()
    win.title("Remove Room")
    win.geometry("300x150")
    customtkinter.CTkLabel(win, text="Room ID:").pack()
    room_id_entry = customtkinter.CTkEntry(win)
    room_id_entry.pack()

    def on_remove():
        try:
            room_id = int(room_id_entry.get())
            remove_room(room_id)
            messagebox.showinfo("Success", f"Room {room_id} removed.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    customtkinter.CTkButton(win, text="Remove Room", command=on_remove).pack(pady=10)

def open_add_staff_window():
    win = customtkinter.CTkToplevel()
    win.title("Add Staff")
    win.geometry("350x300")

    entries = {}
    for label in ["Staff ID", "Staff Name", "Staff Age", "Staff Role"]:
        customtkinter.CTkLabel(win, text=label).pack()
        entry = customtkinter.CTkEntry(win)
        entry.pack()
        entries[label] = entry

    def on_add():
        try:
            staff_id = int(entries["Staff ID"].get())
            staff_name = entries["Staff Name"].get()
            staff_age = int(entries["Staff Age"].get())
            staff_role = entries["Staff Role"].get()
            staff = Staff(staff_id, staff_name, staff_age, staff_role)
            staff.save_to_db()
            messagebox.showinfo("Success", "Staff added successfully!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    customtkinter.CTkButton(win, text="Add Staff", command=on_add).pack(pady=10)