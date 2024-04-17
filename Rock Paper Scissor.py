import tkinter as tk
import random

class RockPaperScissorsApp:
    def __init__(self, master):
        self.master = master
        master.title("Rock, Paper, Scissors")

        self.choices = ["rock", "paper", "scissors"]

        self.user_choice_var = tk.StringVar()
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # User choice selection
        self.user_choice_label = tk.Label(self.master, text="Choose rock, paper, or scissors:")
        self.user_choice_label.grid(row=0, column=0, columnspan=3)

        self.rock_btn = tk.Button(self.master, text="Rock", command=lambda: self.get_user_choice("rock"))
        self.rock_btn.grid(row=1, column=0)
        self.paper_btn = tk.Button(self.master, text="Paper", command=lambda: self.get_user_choice("paper"))
        self.paper_btn.grid(row=1, column=1)
        self.scissors_btn = tk.Button(self.master, text="Scissors", command=lambda: self.get_user_choice("scissors"))
        self.scissors_btn.grid(row=1, column=2)

        # Result display
        self.result_label = tk.Label(self.master, textvariable=self.result_var)
        self.result_label.grid(row=2, column=0, columnspan=3)

        # Play again button
        self.play_again_btn = tk.Button(self.master, text="Play Again", command=self.play_again)
        self.play_again_btn.grid(row=3, column=1)

    def get_user_choice(self, choice):
        self.user_choice_var.set(choice)
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(choice, computer_choice)
        self.result_var.set(result)

    def determine_winner(self, user_choice, computer_choice):
        # Tie
        if user_choice == computer_choice:
            return "It's a tie!"

        # User wins
        if (user_choice == "rock" and computer_choice == "scissors") or \
           (user_choice == "paper" and computer_choice == "rock") or \
           (user_choice == "scissors" and computer_choice == "paper"):
            return f"You win! {user_choice.capitalize()} beats {computer_choice}."

        # Computer wins
        else:
            return f"You lose! {computer_choice.capitalize()} beats {user_choice}."

    def play_again(self):
        self.result_var.set("")
        self.user_choice_var.set("")

root = tk.Tk()
app = RockPaperScissorsApp(root)
root.mainloop()
