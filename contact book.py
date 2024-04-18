import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, master):
        self.master = master
        master.title("Contact Book")

        # Contact list
        self.contacts = []

        # Define colors
        bg_color = "#f0f0f0"  # Light gray
        button_color = "#4caf50"  # Green
        delete_button_color = "#f44336"  # Red
        entry_color = "#ffffff"  # White
        label_color = "#333333"  # Dark gray

        # Set background color
        master.configure(bg=bg_color)

        # Labels
        self.name_label = tk.Label(master, text="Name:", bg=bg_color, fg=label_color)
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.phone_label = tk.Label(master, text="Phone:", bg=bg_color, fg=label_color)
        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.email_label = tk.Label(master, text="Email:", bg=bg_color, fg=label_color)
        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.address_label = tk.Label(master, text="Address:", bg=bg_color, fg=label_color)
        self.address_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        # Entries
        self.name_entry = tk.Entry(master, bg=entry_color)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        self.phone_entry = tk.Entry(master, bg=entry_color)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
        self.email_entry = tk.Entry(master, bg=entry_color)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        self.address_entry = tk.Entry(master, bg=entry_color)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact, bg=button_color, fg='white')
        self.add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
        self.view_button = tk.Button(master, text="View Contacts", command=self.view_contacts, bg=button_color, fg='white')
        self.view_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
        self.delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact, bg=delete_button_color, fg='white')
        self.delete_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and Phone fields are required.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Information", "No contacts to display.")
            return

        view_window = tk.Toplevel(self.master)
        view_window.title("View Contacts")

        for i, contact in enumerate(self.contacts, start=1):
            label_text = f"{i}. {contact['Name']} - {contact['Phone']}"
            tk.Label(view_window, text=label_text).pack(padx=10, pady=5)

    def delete_contact(self):
        if not self.contacts:
            messagebox.showinfo("Information", "No contacts to delete.")
            return

        delete_window = tk.Toplevel(self.master)
        delete_window.title("Delete Contact")

        tk.Label(delete_window, text="Select contact to delete:", bg="#f0f0f0", fg="#333333").pack(padx=10, pady=5)

        for i, contact in enumerate(self.contacts, start=1):
            label_text = f"{contact['Name']} - {contact['Phone']}"
            tk.Button(delete_window, text=label_text, command=lambda idx=i-1: self.perform_deletion(idx)).pack(padx=10, pady=5)

    def perform_deletion(self, index):
        del self.contacts[index]
        messagebox.showinfo("Success", "Contact deleted successfully!")

root = tk.Tk()
app = ContactBookApp(root)
root.mainloop()
