from tkinter import *
from functools import partial


class Game:
    def __init__(self):
        self.game_stats_list = [50,6]

        self.round_stats_list = ['Silver ($5) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $6'
                                'Silver ($5) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $6', 'Lead ($0) | Silver ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $3'
                                'Silver ($5) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $6', 'Lead ($0) | Silver ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $3', 'Lead ($0) | Copper ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $2'
                                'Silver ($5) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $6', 'Lead ($0) | Silver ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $3', 'Lead ($0) | Copper ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Silver ($5) | Lead ($0) - Cost: $Lead ($0) | Payback: $5 | Current Balance: $2'
                                'Silver ($5) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $6', 'Lead ($0) | Silver ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $3', 'Lead ($0) | Copper ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Silver ($5) | Lead ($0) - Cost: $Lead ($0) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Lead ($0) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $1'
                                'Silver ($5) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $6', 'Lead ($0) | Silver ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $3', 'Lead ($0) | Copper ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Silver ($5) | Lead ($0) - Cost: $Lead ($0) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Lead ($0) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $1', 'Copper ($5) | Copper ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $4'
                                'Silver ($5) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $6', 'Lead ($0) | Silver ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $3', 'Lead ($0) | Copper ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Silver ($5) | Lead ($0) - Cost: $Lead ($0) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Lead ($0) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $1', 'Copper ($5) | Copper ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $4', 'Lead ($0) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $4'      
                                'Silver ($5) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $6', 'Lead ($0) | Silver ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $3', 'Lead ($0) | Copper ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Silver ($5) | Lead ($0) - Cost: $Lead ($0) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Lead ($0) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $1', 'Copper ($5) | Copper ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $4', 'Lead ($0) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $4', 'Copper ($5) | Lead ($0) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $3'
                                'Silver ($5) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $6', 'Lead ($0) | Silver ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $3', 'Lead ($0) | Copper ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Silver ($5) | Lead ($0) - Cost: $Lead ($0) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Lead ($0) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $1', 'Copper ($5) | Copper ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $4', 'Lead ($0) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $4', 'Copper ($5) | Lead ($0) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $3', 'Lead ($0) | Lead ($0) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $1'
                                'Silver ($5) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $6', 'Lead ($0) | Silver ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $3', 'Lead ($0) | Copper ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Silver ($5) | Lead ($0) - Cost: $Lead ($0) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Lead ($0) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $1', 'Copper ($5) | Copper ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $4', 'Lead ($0) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $4', 'Copper ($5) | Lead ($0) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $3', 'Lead ($0) | Lead ($0) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $1', 'Lead ($0) | Copper ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $2']

        self.game_frame = Frame()
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Play...", font="Arial 24 bold", padx=10, pady=10)
        self.heading_label.grid(row=0)

        # History Button (Row 1)
        self.stats_button = Button(self.game_frame, text="Game Stats", font="Ariel 14")

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("title goes here")
    something = Game(root)
    root.mainloop()
