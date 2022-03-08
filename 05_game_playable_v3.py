from codecs import backslashreplace_errors
from tkinter import *
from functools import partial
import random


class Start:
    def __init__(self, parent):
        
        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()
        
        self.push_button = Button(self.start_frame, text="Push Now", command=self.to_game)
        self.push_button.grid(row=0, pady=10)

    def to_game(self):
        # Retrieve starting balance
        starting_balance = 50
        stakes = 1

        Game(self, stakes, starting_balance)

        # Hide start up window
        self.start_frame.destroy()

class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        # Disable low stakes button
        partner.lowstakes_button.config(state=DISABLED)

        # Initialise variables
        self.balance = IntVar()

        # Set starting balance to amount entered by user at start of game
        self.balance.set(starting_balance)

        # Get value of stakes
        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        # GUI setup
        self.game_box = Toplevel()

        # If users press cross at top, close program
        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading (Row 0)
        self.heading_label = Label(self.game_frame, text="Heading", font="Ariel 24 bold", padx=10, pady=10)
        self.heading_label.grid(row=0)

        # Instructions Label (Row 1)
        self.instructions_label = Label(self.game_frame, wrap=300, justify=LEFT, text="Press <Enter> or click the 'Open Boxes' button to reveal the contents of the mystery boxes.", font="Ariel 10", padx=10, pady=10)
        self.instructions_label.grid(row=1)

        # Boxes (Row 2)
        self.box_frame = Frame(self.game_frame)
        self.box_frame.grid(row=2, pady=10)

        photo = PhotoImage(file="question.gif")

        self.prize1_label = Label(self.game_box, text="?\n", padx=10, pady=10, image=photo)
        self.prize1_label.photo = photo
        self.prize1_label.grid(row=0, column=0)

        self.prize2_label = Label(self.game_box, text="?\n", padx=10, pady=10, image=photo)
        self.prize2_label.photo = photo
        self.prize2_label.grid(row=0, column=1, padx=10)

        self.prize3_label = Label(self.game_box, text="?\n", padx=10, pady=10, image=photo)
        self.prize3_label.photo = photo
        self.prize3_label.grid(row=0, column=2)

        # Play button (Row 3)
        self.play_button = Button(self.game_frame, text="Open Boxes", bg="#FFFF33", font="Ariel 15 bold", width=20, padx=10, pady=10, command=self.reveal_boxes)
        # Bind button to <Enter>
        self.play_button.focus()
        self.play_button.bind('<Return>', lambda e: self.reveal_boxes())
        self.play_button.grid(row=3)

        # Balance Label (Row 4)
        start_text = "Game Cost: ${}\n""\n How Much will you win?".format(stakes*5)
        self.balance_label = Label(self.game_frame, font="Ariel 12 bold", fg="grey", text=start_text, wrap=300, justify=LEFT)
        self.balance_label.grid(row=4, pady=10)

        # Help and Game stats button (Row 5)
        self.help_export_frame = Frame(self.game_frame)
        self.help_export_frame.grid(row=5, pady=10)

        self.help_button = Button(self.help_export_frame, text="Help / Rules", font="Ariel 15 bold", bg="#808080", fg="white")
        self.help_button.grid(row=0, column=1, padx=2)

        self.stats_button = Button(self.help_export_frame, text="Game Stats", font="Ariel 15 bold", bg="#003366", fg="white")
        self.stats_button.grid(row=0, column=1, padx=2)

        # Quit Button (Row 6)
        self.quit_button = Button(self.game_frame, text="Quit", fg="white", bg="#660000", font="Ariel 15 bold", width=20, command=self.to_quit, padx=10, pady=10)
        self.quit_button.grid(row=6, pady=10)

    def reveal_boxes(self):
        # retrieve the balance from the initial function
        current_balance = self.balance.get()
        stakes_multiplier = self.multiplier.get()

        round_winnings = 0
        prizes = []
        stats_prizes = []
        for item in range(0,3):
            prize_num = random.randint(1,100)

            if 0 < prize_num <= 5:
                prize = PhotoImage(file="gold_low.gif")
                prize_list = "Gold (${})".format(5*stakes_multiplier)
                round_winnings += 5 * stakes_multiplier
            elif 5 < prize_num <= 25:
                prize = PhotoImage(file="silver_low.gif")
                prize_list = "Silver (${})".format(5*stakes_multiplier)
                round_winnings += 2 * stakes_multiplier
            elif 25 < prize_num <= 65:
                prize = PhotoImage(file="copper_low.gif")
                prize_list = "Copper (${})".format(5*stakes_multiplier)
                round_winnings += 1 * stakes_multiplier
            else:
                prize = PhotoImage(file="lead.gif")
                prize_list = "Lead ($0)"

            prizes.append(prize)
            stats_prizes

        # Display prizes
        self.prize1_label.config(text=prizes[0])
        self.prize2_label.config(text=prizes[1])
        self.prize3_label.config(text=prizes[2])

        # Deduct cost of game
        current_balance -= 5 * stakes_multiplier

        # Add winnings
        current_balance += round_winnings

        # Set balance to adjusted balance
        self.balance.set(current_balance)

        balance_statement = "Game Cost: ${}\nPayback: ${}\nCurrent Balance: ${}".format(5*stakes_multiplier, round_winnings, current_balance)

        # Edit label so user can see their balance
        self.balance_label.configure(text=balance_statement)

        if current_balance < 5 * stakes_multiplier:
            self.play_button.config(state=DISABLED)
            self.game_box.focus()
            self.play_button.config(text="Game Over")

            balance_statement = "Current Balance: ${}\nYour balance is too low. You can only quit or view your stats. Sorry about that.".format(current_balance)
            self.balance_label.config(fg="660000", font="Ariel 10 bold", text=balance_statement)

    def to_quit(self):
        root.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("title goes here")
    something = Start(root)
    root.mainloop()
