import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")

        # Define colors
        bg_color = "#f0f0f0"  # Light gray
        label_color = "#333333"  # Dark gray
        button_color = "#4caf50"  # Green
        entry_color = "#ffffff"  # White
        dialog_color = "#cccccc"  # Grey

        # Set background color
        master.configure(bg=bg_color)

        # Length label
        self.length_label = tk.Label(master, text="Password Length(in numbers):", bg=bg_color, fg=label_color)
        self.length_label.grid(row=0, column=0, padx=10, pady=10)

        # Length entry
        self.length_entry = tk.Entry(master, bg=entry_color)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        # Generate button
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password, bg=button_color, fg='white')
        self.generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Frame for password display
        self.password_frame = tk.Frame(master, bg=dialog_color)
        self.password_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Password label
        self.password_label = tk.Label(self.password_frame, text="Generated Password:", bg=dialog_color, fg=label_color)
        self.password_label.grid(row=0, column=0, padx=10, pady=10)

        # Password entry
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(self.password_frame, textvariable=self.password_var, state='readonly', bg=entry_color)
        self.password_entry.grid(row=1, column=0, padx=10, pady=10)

    def generate_password(self):
        password_length = int(self.length_entry.get())
        if password_length <= 0:
            self.password_var.set("Invalid length")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(password_length))
        self.password_var.set(password)

root = tk.Tk()
app = PasswordGeneratorApp(root)
root.mainloop()
