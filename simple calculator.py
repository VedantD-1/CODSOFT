import tkinter as tk
import re

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        
        self.expression = ''
        self.result_var = tk.StringVar()
        
        self.create_widgets()

    def create_widgets(self):
        self.result_entry = tk.Entry(self.master, textvariable=self.result_var, font=('Arial', 14), bd=10, insertwidth=4, width=20, justify='right')
        self.result_entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('(', 5, 0), (')', 5, 1), ('C', 5, 2), ('^', 5, 3)
        ]

        for (text, row, col) in buttons:
            if text == '=':
                btn = tk.Button(self.master, text=text, font=('Arial', 14), bd=5, padx=20, pady=10, command=self.calculate)
            elif text == 'C':
                btn = tk.Button(self.master, text=text, font=('Arial', 14), bd=5, padx=20, pady=10, command=self.clear)
            else:
                btn = tk.Button(self.master, text=text, font=('Arial', 14), bd=5, padx=20, pady=10, command=lambda t=text: self.add_to_expression(t))
            btn.grid(row=row, column=col)

    def add_to_expression(self, char):
        self.expression += char
        self.result_var.set(self.expression)

    def calculate(self):
        try:
            self.result_var.set(eval(self.expression))
        except Exception as e:
            self.result_var.set("Error")

    def clear(self):
        self.expression = ''
        self.result_var.set('')

root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()
