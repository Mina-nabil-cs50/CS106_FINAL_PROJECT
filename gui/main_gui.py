import customtkinter
from tkinter import messagebox
import sqlite3

def get_connection():
    return sqlite3.connect("c:/Users/minas/OneDrive/Desktop/TERM 2/CS106-Project/database/hotel.db")

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
        root.destroy()
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

root.mainloop()