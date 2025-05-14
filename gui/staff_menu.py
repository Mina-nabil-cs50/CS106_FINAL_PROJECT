import tkinter as tk

def open_staff_menu():
    win = tk.Toplevel()
    win.title("Staff Dashboard")
    win.geometry("400x400")
    tk.Label(win, text="Staff Dashboard", font=("Arial", 18)).pack(pady=20)
    # Add buttons for staff features:
    tk.Button(win, text="Add Reservation").pack(pady=5)
    tk.Button(win, text="View Rooms").pack(pady=5)
    tk.Button(win, text="View Guests").pack(pady=5)
    tk.Button(win, text="Logout", command=win.destroy).pack(pady=20)