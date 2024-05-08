import tkinter as tk
from tkinter import messagebox
import sqlite3

class BusinessMemberRegistrationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Business Member Registration")
        self.master.geometry("400x400")
        self.master.configure(bg="#F0F0F0")

        self.title_label = tk.Label(self.master, text="PRINCE HOSTEL REGISTRATION FORM", bg="#FF5733", fg="white", font=("Times New Roman", 20))
        self.title_label.pack(pady=10)

        self.name_label = tk.Label(self.master, text="Enter Name:", bg="#F0F0F0", font=("Times New Roman", 15))
        self.name_label.pack()
        self.name_entry = tk.Entry(self.master)
        self.name_entry.pack()

        self.email_label = tk.Label(self.master, text="Enter Email:", bg="#F0F0F0", font=("Times New Roman", 15))
        self.email_label.pack()
        self.email_entry = tk.Entry(self.master)
        self.email_entry.pack()

        self.contact_label = tk.Label(self.master, text="Contact Number:", bg="#F0F0F0", font=("Times New Roman", 15))
        self.contact_label.pack()
        self.contact_entry = tk.Entry(self.master)
        self.contact_entry.pack()

        self.gender_label = tk.Label(self.master, text="Select Gender:", bg="#F0F0F0", font=("Times New Roman", 15))
        self.gender_label.pack()
        self.gender_var = tk.StringVar(self.master)
        self.gender_var.set("Select Gender")
        self.gender_combobox = tk.OptionMenu(self.master, self.gender_var, "Male", "Female", "Other")
        self.gender_combobox.pack()

        self.country_label = tk.Label(self.master, text="Select Country:", bg="#F0F0F0", font=("Times New Roman", 15))
        self.country_label.pack()
        self.country_var = tk.StringVar(self.master)
        self.country_var.set("Select Country")
        self.country_combobox = tk.OptionMenu(self.master, self.country_var, "USA", "Canada", "UK", "Australia")
        self.country_combobox.pack()

        self.password_label = tk.Label(self.master, text="Enter Password:", bg="#F0F0F0", font=("Times New Roman", 15))
        self.password_label.pack()
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()

        self.repassword_label = tk.Label(self.master, text="Re-enter Password:", bg="#F0F0F0", font=("Times New Roman", 15))
        self.repassword_label.pack()
        self.repassword_entry = tk.Entry(self.master, show="*")
        self.repassword_entry.pack()

        self.register_button = tk.Button(self.master, text="Register", command=self.register_member)
        self.register_button.pack(pady=10)

        self.footer_label = tk.Label(self.master, text="Business Location:BUGEMA LUWERO DISTRIC UGANDA ", bg="#FF5733", fg="white", font=("Times New Roman", 15))
        self.footer_label.pack(side="bottom", fill="x")

        # Database connection
        self.conn = sqlite3.connect("business_members.db")
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS members\n'
                       '                          (id INTEGER PRIMARY KEY AUTOINCREMENT,\n'
                       '                          name TEXT,\n'
                       '                          email TEXT,\n'
                       '                          contact TEXT,\n'
                       '                          gender TEXT,\n'
                       '                          country TEXT,\n'
                       '                          password TEXT)')
        self.conn.commit()

    def register_member(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        contact = self.contact_entry.get()
        gender = self.gender_var.get()
        country = self.country_var.get()
        password = self.password_entry.get()
        repassword = self.repassword_entry.get()

        if not all([name, email, contact, gender != "Select Gender", country != "Select Country", password, repassword]):
            messagebox.showerror("Error", "Please fill in all fields")
            return

        if password != repassword:
            messagebox.showerror("Error", "Passwords do not match")
            return

        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO members (name, email, contact, gender, country, password)
                          VALUES (?, ?, ?, ?, ?, ?)''', (name, email, contact, gender, country, password))
        self.conn.commit()

        messagebox.showinfo("Success", "Registration Successful!")
        self.clear_fields()

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.gender_var.set("Select Gender")
        self.country_var.set("Select Country")
        self.password_entry.delete(0, tk.END)
        self.repassword_entry.delete(0, tk.END)

root = tk.Tk()
app = BusinessMemberRegistrationApp(root)
root.mainloop()
