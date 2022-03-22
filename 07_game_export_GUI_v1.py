from tkinter import *
from functools import partial
import re


class Game:
    def __init__(self, parent):
        self.game_stats_list = [50,6]

        self.round_stats_list = ['Silver ($5) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $6',
                                'Silver ($5) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $6', 'Lead ($0) | Silver ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $3',
                                'Silver ($5) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $6', 'Lead ($0) | Silver ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $3', 'Lead ($0) | Copper ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $2',
                                'Silver ($5) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $6', 'Lead ($0) | Silver ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $3', 'Lead ($0) | Copper ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Silver ($5) | Lead ($0) - Cost: $Lead ($0) | Payback: $5 | Current Balance: $2',
                                'Silver ($5) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $6', 'Lead ($0) | Silver ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $3', 'Lead ($0) | Copper ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Silver ($5) | Lead ($0) - Cost: $Lead ($0) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Lead ($0) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $1',
                                'Silver ($5) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $6', 'Lead ($0) | Silver ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $3', 'Lead ($0) | Copper ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Silver ($5) | Lead ($0) - Cost: $Lead ($0) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Lead ($0) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $1', 'Copper ($5) | Copper ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $4',
                                'Silver ($5) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $6', 'Lead ($0) | Silver ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $3', 'Lead ($0) | Copper ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Silver ($5) | Lead ($0) - Cost: $Lead ($0) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Lead ($0) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $1', 'Copper ($5) | Copper ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $4', 'Lead ($0) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $4',   
                                'Silver ($5) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $6', 'Lead ($0) | Silver ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $3', 'Lead ($0) | Copper ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Silver ($5) | Lead ($0) - Cost: $Lead ($0) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Lead ($0) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $1', 'Copper ($5) | Copper ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $4', 'Lead ($0) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $4', 'Copper ($5) | Lead ($0) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $3',
                                'Silver ($5) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $6', 'Lead ($0) | Silver ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $3', 'Lead ($0) | Copper ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Silver ($5) | Lead ($0) - Cost: $Lead ($0) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Lead ($0) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $1', 'Copper ($5) | Copper ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $4', 'Lead ($0) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $4', 'Copper ($5) | Lead ($0) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $3', 'Lead ($0) | Lead ($0) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $1',
                                'Silver ($5) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $6', 'Lead ($0) | Silver ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $3', 'Lead ($0) | Copper ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Silver ($5) | Lead ($0) - Cost: $Lead ($0) | Payback: $5 | Current Balance: $2', 'Lead ($0) | Lead ($0) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $1', 'Copper ($5) | Copper ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $4', 'Lead ($0) | Silver ($5) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $4', 'Copper ($5) | Lead ($0) | Silver ($5) - Cost: $Silver ($5) | Payback: $5 | Current Balance: $3', 'Lead ($0) | Lead ($0) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $1', 'Lead ($0) | Copper ($5) | Copper ($5) - Cost: $Copper ($5) | Payback: $5 | Current Balance: $2']

        self.game_frame = Frame()
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Play...", font="Arial 24 bold", padx=10, pady=10)
        self.heading_label.grid(row=0)

        # History Button (Row 1)
        self.stats_button = Button(self.game_frame, text="Game Stats", font="Ariel 14", padx=10, pady=10, command=lambda: self.to_stats(self.round_stats_list, self.game_stats_list))
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

        # Set up GUI frame
        self.stats_frame = Frame(self.stats_box)
        self.stats_frame.grid()

        # Heading (Row 0)
        self.stats_heading_label = Label(self.stats_frame, text="Game Statistics", font="Arial 19 bold")
        self.stats_heading_label.grid(row=0)

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

        self.current_balance_value_label = Label(self.details_frame, font=content, text="${}".format(game_stats[1]), anchor="w")
        self.current_balance_value_label.grid(row=1, column=1, padx=0)

        if game_stats[1] > game_stats[0]:
            win_loss = "Amount Won: "
            amount = game_stats[1] - game_stats[0]
            win_loss_fg = "green"
        else:
            win_loss = "Amount Loss: "
            amount = game_stats[0] - game_stats[1]
            win_loss_fg = "#660000"

        # Amount won / lost (Row 2.3)
        self.win_loss_label = Label(self.details_frame, text=win_loss, font=heading, anchor="e")
        self.win_loss_label.grid(row=2, column=0, padx=0)

        self.win_loss_value_label = Label(self.details_frame, font=content, text="${}".format(amount), fg=win_loss_fg, anchor="w")
        self.win_loss_value_label.grid(row=2, column=1, padx=0)

        # Rounds Played
        self.games_played_label = Label(self.details_frame, font=heading, text="Rounds Played: ", anchor="e")
        self.games_played_label.grid(row=4, column=0, padx=0)

        self.games_played_value_label = Label(self.details_frame, font=content, text=len(game_history), anchor="w")
        self.games_played_value_label.grid(row=4, column=1, padx=0)

        # Button Frame (Row 3)
        self.button_frame = Frame(self.stats_frame)
        self.button_frame.grid(row=3)

        # Export Button
        self.export_button = Button(self.button_frame, text="Export", width=10, font=("Arial", "10", "bold"), command=lambda: self.export(game_history, game_stats))
        self.export_button.grid(row=0, column=0, pady=10)

        # Dismiss Button
        self.dismiss_button = Button(self.button_frame, text="Dismiss", width=10, font=("Arial", "10", "bold"), command=partial(self.close_stats, partner))
        self.dismiss_button.grid(row=0, column=1, pady=10)

    def close_stats(self,partner):
        # Put help button back to normal...
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()

    def export(self, game_history, game_stats):
        Export(self, game_history, game_stats)

class Export:
    def __init__(self, partner, game_history, all_game_stats):
        print(game_history)

        # Sets up child window
        self.export_box = Toplevel()

        # If users press cross at top closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))
        
        # Set up GUI frame
        self.export_frame = Frame(self.export_box, width=300,)
        self.export_frame.grid()

        # Set up export heading
        self.how_heading = Label(self.export_frame, text="Export / Instructions", font="Arial 14 bold")
        self.how_heading.grid()

        # Export Instructions
        self.export_text = Label(self.export_frame, text="Enter a filename", justify=LEFT, width=40, wrap=250)
        self.export_text.grid(row=1)

        # Warning Text
        self.export_text = Label(self.export_frame, text="If the filename you enter below already exists, its contents will be replaced with your calculation history.", justify=LEFT, bg="#ffafaf", fg="maroon", font="Arial 10 italic", wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename Entry Box
        self.filename_entry = Entry(self.export_frame, width=20, font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error message label (initially blank)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon")
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and cancel buttons
        self.save_button = Button(self.save_cancel_frame, text="Save", font="Arial 15 bold", bg="#003366", fg="white", command=partial(lambda: self.save_history(partner, game_history, all_game_stats)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel", font="Arial 15 bold", bg="#660000", fg="white", command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, game_history, game_stats):

        # Regular Expression to check validity
        valid_char = "[A-Za-z0-9 ]"
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue
            elif letter == " ":
                problem = "(no spaces allowed)"
            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            self.save_error_label.config(text= "Invalid Filename - {}".format(problem))
            self.filename_entry.config(bg="#ffafaf")
            print()
        else:
            # If there are no errors, generate text file
            # Add .txt suffix
            filename = filename + ".txt"

            # Create file to hold data
            f = open(filename, "w+")

            # Heading for stats
            f.write("Game Statistics\n\n")

            # Game stats
            for round in game_stats:
                f.write("{}\n".format(round))

            # Heading for rounds
            f.write("\nRound Details\n\n")

            # Add a new line at the end of each item
            for item in game_history:
                f.write(item + "\n")

            # Close file
            f.close()

    def close_export(self,partner):
        self.export_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("title goes here")
    something = Game(root)
    root.mainloop()
