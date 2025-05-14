import tkinter as tk

def open_admin_menu():
    win = tk.Toplevel()
    win.title("Admin Dashboard")
    win.geometry("400x400")
    tk.Label(win, text="Admin Dashboard", font=("Arial", 18)).pack(pady=20)
    # Add buttons for admin features:
    tk.Button(win, text="Manage Rooms").pack(pady=5)
    tk.Button(win, text="Manage Staff").pack(pady=5)
    tk.Button(win, text="View Reservations").pack(pady=5)
    tk.Button(win, text="Logout", command=win.destroy).pack(pady=20)