import tkinter as tk
import random

class CardGame(tk.Tk):
    def init(self):
        super().init()

        self.title("Guess the Card")
        self.geometry("400x300")

        # Create the deck of cards
        self.cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

        self.current_card = None

        self.create_widgets()

    def create_widgets(self):
        self.card_label = tk.Label(self, text="Click 'Start' to play!", font=("Arial", 16))
        self.card_label.pack(pady=20)

        self.start_button = tk.Button(self, text="Start", command=self.start_game)
        self.start_button.pack(pady=10)

        self.guess_entry = tk.Entry(self, font=("Arial", 14))
        self.guess_entry.pack(pady=10)

        self.submit_button = tk.Button(self, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(self, text="", font=("Arial", 16))
        self.result_label.pack(pady=20)

    def start_game(self):
        self.current_card = random.choice(self.cards) + " of " + random.choice(self.suits)
        self.card_label.config(text=self.current_card)
        self.result_label.config(text="")

    def check_guess(self):
        guess = self.guess_entry.get()

        if guess.lower() == self.current_card.lower():
            self.result_label.config(text="Correct! You guessed the card.")
        else:
            self.result_label.config(text="Wrong! The card was: " + self.current_card)

        self.guess_entry.delete(0, tk.END)
name=""
if name == "main":
    game = CardGame()
    game.mainloop()
