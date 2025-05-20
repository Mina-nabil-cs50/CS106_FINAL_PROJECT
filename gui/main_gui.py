import customtkinter
from tkinter import messagebox
import sqlite3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.dirname(__file__))
from Models.admin import edit_staff, remove_staff, ensure_admin_and_staff, Admin
from Models.staff import Staff
from admin_menu import open_admin_menu
from room_gui import open_manage_rooms_window

def get_connection():
    return sqlite3.connect("C:/Users/hanat/Desktop/College/CS106_FINAL_PROJECT/database/hotel.db")

def check_login(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT staff_role FROM staff WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]  # 'admin' or 'staff'
    return None

def open_dashboard(role):
    if role == "admin":
        from admin_menu import open_admin_menu
        open_admin_menu()
    elif role == "staff":
        from staff_menu import open_staff_menu
        open_staff_menu()

def login():
    username = username_entry.get()
    password = password_entry.get()
    role = check_login(username, password)
    if role:
        root.withdraw()  # Hide the login window instead of destroying it
        open_dashboard(role)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title("Hotel Management System - Login")
root.geometry("350x220")

customtkinter.CTkLabel(root, text="Username:", font=("Arial", 12)).pack(pady=5)
username_entry = customtkinter.CTkEntry(root)
username_entry.pack()

customtkinter.CTkLabel(root, text="Password:", font=("Arial", 12)).pack(pady=5)
password_entry = customtkinter.CTkEntry(root, show="*")
password_entry.pack()

customtkinter.CTkButton(root, text="Login", command=login).pack(pady=20)

default_admin = Admin(1, "Admin", 30, "admin", "admin123")
default_admin.save_to_db() 

default_staff = Staff(2, "Default Staff", 25, "staff", "staff", "staff123")
default_staff.save_to_db()

root.mainloop()