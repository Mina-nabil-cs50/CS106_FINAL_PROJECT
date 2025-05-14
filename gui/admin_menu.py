import tkinter as tk
import customtkinter
from room_gui import open_manage_rooms_window

def open_admin_menu():
    win = customtkinter.CTkToplevel()
    win.title("Admin Dashboard")
    win.geometry("400x400")
    customtkinter.CTkLabel(win, text="Admin Dashboard", font=("Arial", 18)).pack(pady=20)
    # Add buttons for admin features:
    customtkinter.CTkButton(win, text="Manage Rooms", command=open_manage_rooms_window).pack(pady=5)
    customtkinter.CTkButton(win, text="Manage Staff").pack(pady=5)
    customtkinter.CTkButton(win, text="View Reservations").pack(pady=5)
    customtkinter.CTkButton(win, text="Logout", command=win.destroy).pack(pady=20)