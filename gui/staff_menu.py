import tkinter as tk
import customtkinter
from Models.staff import Staff
from Models.guest import Guest
from Models.reservation import Reservation
from Models.payment import Payment
from tkinter import messagebox
from database.db_manager import get_connection

def open_add_guest_window():
    win = customtkinter.CTkToplevel()
    win.title("Add Guest")
    win.geometry("350x350")
    entries = {}
    for label in ["Guest ID", "Full Name", "Phone Number", "Email", "ID Document", "Guest Age"]:
        customtkinter.CTkLabel(win, text=label).pack()
        entry = customtkinter.CTkEntry(win)
        entry.pack()
        entries[label] = entry

    def on_add():
        try:
            guest_id = int(entries["Guest ID"].get())
            full_name = entries["Full Name"].get()
            phone_number = entries["Phone Number"].get()
            email = entries["Email"].get()
            id_document = entries["ID Document"].get()
            guest_age = int(entries["Guest Age"].get())
            guest = Guest(guest_id, full_name, phone_number, email, id_document, guest_age)
            guest.save_to_db()
            messagebox.showinfo("Success", "Guest added successfully!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    customtkinter.CTkButton(win, text="Add Guest", command=on_add).pack(pady=10)

def open_add_reservation_window():
    win = customtkinter.CTkToplevel()
    win.title("Add Reservation")
    win.geometry("350x350")
    entries = {}
    for label in ["Reservation ID", "Guest ID", "Room ID", "Check-In Date (YYYY-MM-DD)", "Check-Out Date (YYYY-MM-DD)"]:
        customtkinter.CTkLabel(win, text=label).pack()
        entry = customtkinter.CTkEntry(win)
        entry.pack()
        entries[label] = entry

    def on_add():
        try:
            reservation_id = int(entries["Reservation ID"].get())
            guest_id = int(entries["Guest ID"].get())
            room_id = int(entries["Room ID"].get())
            check_in_date = entries["Check-In Date (YYYY-MM-DD)"].get()
            check_out_date = entries["Check-Out Date (YYYY-MM-DD)"].get()
            reservation = Reservation(reservation_id, [guest_id], room_id, check_in_date, check_out_date)
            reservation.save_to_db()
            messagebox.showinfo("Success", "Reservation added successfully!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    customtkinter.CTkButton(win, text="Add Reservation", command=on_add).pack(pady=10)

def open_add_payment_window():
    win = customtkinter.CTkToplevel()
    win.title("Add Payment")
    win.geometry("350x350")
    entries = {}
    for label in ["Payment ID", "Reservation ID", "Payment Date (YYYY-MM-DD)", "Payment Amount", "Is Paid (yes/no)", "Payment Method"]:
        customtkinter.CTkLabel(win, text=label).pack()
        entry = customtkinter.CTkEntry(win)
        entry.pack()
        entries[label] = entry

    def on_add():
        try:
            payment_id = int(entries["Payment ID"].get())
            reservation_id = int(entries["Reservation ID"].get())
            payment_date = entries["Payment Date (YYYY-MM-DD)"].get()
            payment_amount = float(entries["Payment Amount"].get())
            is_paid = entries["Is Paid (yes/no)"].get().lower() == "yes"
            payment_method = entries["Payment Method"].get()
            payment = Payment(payment_id, reservation_id, payment_date, payment_amount, is_paid, payment_method)
            payment.save_to_db()
            messagebox.showinfo("Success", "Payment added successfully!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    customtkinter.CTkButton(win, text="Add Payment", command=on_add).pack(pady=10)

def open_delete_reservation_window():
    win = customtkinter.CTkToplevel()
    win.title("Delete Reservation")
    win.geometry("300x150")
    customtkinter.CTkLabel(win, text="Reservation ID:").pack()
    reservation_id_entry = customtkinter.CTkEntry(win)
    reservation_id_entry.pack()

    def on_delete():
        try:
            reservation_id = int(reservation_id_entry.get())
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM reservations WHERE reservation_id = ?", (reservation_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", f"Reservation {reservation_id} deleted.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    customtkinter.CTkButton(win, text="Delete Reservation", command=on_delete).pack(pady=10)

def open_staff_menu():
    win = customtkinter.CTkToplevel()
    win.title("Staff Dashboard")
    win.geometry("400x500")
    customtkinter.CTkLabel(win, text="Staff Dashboard", font=("Arial", 18)).pack(pady=20)
    customtkinter.CTkButton(win, text="Add Guest", command=open_add_guest_window).pack(pady=5)
    customtkinter.CTkButton(win, text="Add Reservation", command=open_add_reservation_window).pack(pady=5)
    customtkinter.CTkButton(win, text="Add Payment", command=open_add_payment_window).pack(pady=5)
    customtkinter.CTkButton(win, text="Delete Reservation", command=open_delete_reservation_window).pack(pady=5)
    customtkinter.CTkButton(win, text="Logout", command=win.destroy).pack(pady=20)