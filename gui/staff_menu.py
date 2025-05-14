import tkinter as tk
import customtkinter

def open_staff_menu():
    win = customtkinter.CTkToplevel()
    win.title("Staff Dashboard")
    win.geometry("400x400")
    customtkinter.CTkLabel(win, text="Staff Dashboard", font=("Arial", 18)).pack(pady=20)
    customtkinter.CTkButton(win, text="Add Reservation").pack(pady=5)
    customtkinter.CTkButton(win, text="View Rooms").pack(pady=5)
    customtkinter.CTkButton(win, text="View Guests").pack(pady=5)
    customtkinter.CTkButton(win, text="Logout", command=win.destroy).pack(pady=20)