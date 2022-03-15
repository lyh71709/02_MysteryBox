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
        self.stats_button = Button(self.game_frame, text="Game Stats", font="Ariel 14", padx=10, pady=10, command=lambda: self.to_stats(self.round_stats_list))
        self.stats_button.grid(row=1)

    def to_stats(self, game_history, game_stats):
        GameStats(self, game_history, game_stats)

class GameStats:
    def __init__(self, partner, game_history, game_stats):
        print(game_history)

        # Disable help button
        partner.stats_button.config(state=DISABLED)

        heading = "Arial 12 bold"
        content = "Arial 12"

        # Sets up child window (ie: help box)
        self.stats_box = Toplevel()

        # If users press cross at top closes
        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats, partner))

        # Set up GUI frame (Row 0)
        self.stats_frame = Frame(self.stats_box)
        self.stats_frame.grid(row=0)

        # To export (Row 1)
        self.export_instructions = Label(self.stats_frame, text="Here are your game statistics. Please use the export button to access the results of each round that you played", wrap=250, font="Arial 10 italic", justify=LEFT, fg="green", padx=10, pady=10)
        self.export_instructions.grid(row=1)

        # Starting balance (Row 2)
        self.details_frame = Frame(self.stats_frame)
        self.details_frame.grid(row=2)

        # Starting balance
        self.start_balance_label = Label(self.details_frame, text="Starting Balance: ", font=heading, anchor="e")
        self.start_balance_label.grid(row=0, column=0, padx=0)

        self.start_balance_value_label = Label(self.details_frame, font=content, text="${}".format(game_stats[0]), anchor="w")
        self.start_balance_value_label.grid(row=0, column=1, padx=0)

        # Current Balance (Row 2.2)
        self.current_balance_label = Label(self.details_frame, text="Current Balance: ", font=heading, anchor="e")
        self.current_balance_label.grid(row=1, column=0, padx=0)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("title goes here")
    something = Game(root)
    root.mainloop()
