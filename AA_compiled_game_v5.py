from tkinter import *
from functools import partial
import random

#Define functions
def setup_hover_button(button_name, bind_unbind, hover_colour):
    if bind_unbind == "unbind":
        button_name.unbind('<Enter>')
        button_name.unbind('<Leave>')
    else:
        leave_colour = button_name.cget("background")
        leave_font_colour = button_name.cget("foreground")
        if hover_colour == "": enter_colour = "snow4"
        else: enter_colour = hover_colour

        button_name.bind('<Enter>', lambda e: on_enter(e,enter_colour))
        button_name.bind('<Leave>', lambda e: on_leave(e,leave_colour,leave_font_colour))

def on_enter(e, colour):
    e.widget.config(background=colour, foreground= "white")

def on_leave(e, colour, font_colour):
    e.widget.config(background=colour, foreground=font_colour)

class Start:
    def __init__(self, parent):
        
        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Set initial balance to zero
        self.starting_funds = IntVar()
        self.starting_funds.set(0)

        # Mystery Heading (Row 0)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game", font="Arial 19 bold")
        self.mystery_box_label.grid(row=0)

        # Initialise Instructions (Row 1)
        self.mystery_instructions = Label(self.start_frame, font="Arial 10 italic", text="Please enter a dollar amount (between $5 and $50) in the box below. Then choose the stake. The higher the stakes the more you can win!", wrap=275, justify=LEFT, padx=10, pady=10)
        self.mystery_instructions.grid(row=1)

        # Entry Box, Button and Error Label (Row 2) 
        self.entry_error_frame = Frame(self.start_frame, width=200)
        self.entry_error_frame.grid(row=2)

        # Entry box
        self.start_amount_entry = Entry(self.entry_error_frame, font="Arial 16 bold", width=10)
        self.start_amount_entry.grid(row=0, column=0)

        # Add funds button
        self.add_funds_button = Button(self.entry_error_frame, font="Arial 14 bold", text="Add Funds", command=self.check_funds)
        self.add_funds_button.grid(row=0, column=1, padx=10)
        setup_hover_button(self.add_funds_button,"","")
        
        # Amount Error Label
        self.amount_error_label = Label(self.entry_error_frame, fg="maroon", text="", font="Arial", wrap=275, justify=LEFT)
        self.amount_error_label.grid(row=1, columnspan=2, pady=5)

        # Button Frame (Row 3)
        self.stakes_frame = Frame(self.start_frame)
        self.stakes_frame.grid(row=3)

        # Buttons go here
        button_font = "Arial 12 bold"
        
        # Orange low stakes button
        self.lowstakes_button = Button(self.stakes_frame, text="Low ($5)", command=lambda: self.to_game(1), font=button_font, bg="#FF9933")
        self.lowstakes_button.grid(row=0, column=0, pady=10)

        # Yellow medium stakes button
        self.mediumstakes_button = Button(self.stakes_frame, text="Medium ($10)", command=lambda: self.to_game(2), font=button_font, bg="#FFFF33")
        self.mediumstakes_button.grid(row=0, column=1, padx=5, pady=10)

        # Red high stakes button
        self.highstakes_button = Button(self.stakes_frame, text="High ($15)", command=lambda: self.to_game(3), font=button_font, bg="#99FF33")
        self.highstakes_button.grid(row=0, column=2, pady=10)

        # Disable all stakes buttons at start
        self.lowstakes_button.config(state=DISABLED)
        self.mediumstakes_button.config(state=DISABLED)
        self.highstakes_button.config(state=DISABLED)


    def check_funds(self):
        starting_balance = self.start_amount_entry.get()

        # Set error background colours
        error_back = "#ffafaf"
        has_errors = "no"

        # Change background to white
        self.start_amount_entry.config(bg="white")
        self.amount_error_label.config(text="")

        # Disable all stakes buttons
        self.lowstakes_button.config(state=DISABLED)
        self.mediumstakes_button.config(state=DISABLED)
        self.highstakes_button.config(state=DISABLED)
        setup_hover_button(self.lowstakes_button,"unbind","")
        setup_hover_button(self.mediumstakes_button,"unbind","")
        setup_hover_button(self.highstakes_button,"unbind","")

        try:
            starting_balance = int(starting_balance)

            if starting_balance < 5:
                has_errors= "yes"
                error_feedback = "Sorry, the least you can play is $5"
            elif starting_balance > 50:
                has_errors = "yes"
                error_feedback = "Too high! The most you can risk in this game is $50"
            elif starting_balance >= 15:
                # Enable all buttons
                self.lowstakes_button.config(state=NORMAL)
                self.mediumstakes_button.config(state=NORMAL)
                self.highstakes_button.config(state=NORMAL)
                setup_hover_button(self.lowstakes_button,"", "#BD7124")
                setup_hover_button(self.mediumstakes_button,"", "#C4C427")
                setup_hover_button(self.highstakes_button,"", "#6BB025")
            elif starting_balance >= 10:
                # Enable low and medium stakes buttons
                self.lowstakes_button.config(state=NORMAL)
                self.mediumstakes_button.config(state=NORMAL)
                setup_hover_button(self.lowstakes_button,"", "#BD7124")
                setup_hover_button(self.mediumstakes_button,"", "#C4C427")
            else:
                self.lowstakes_button.config(state=NORMAL)
                setup_hover_button(self.lowstakes_button,"", "#BD7124")
        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a dollar amount (no text / decimals)"

        if has_errors == "yes":
            self.start_amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)
        else:
            # Set starting balance to amount entered by user
            self.starting_funds.set(starting_balance)
        

    def to_game(self, stakes):
        starting_balance = self.starting_funds.get()

        # Hide start up window
        self.start_frame.destroy()
  
        Game(self, stakes, starting_balance)

class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        # Initialise variables
        self.balance = IntVar()

        # Set starting balance to amount entered by user at start of game
        self.balance.set(starting_balance)

        # Get value of stakes
        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        # List for holding statistics
        self.round_stats_list = []
        self.game_stats_list = [starting_balance, starting_balance]

        # GUI setup
        self.game_box = Toplevel()

        # If users press cross at top, close program
        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading (Row 0)
        self.heading_label = Label(self.game_frame, text="Mystery Box", font="Ariel 24 bold", padx=10, pady=10)
        self.heading_label.grid(row=0)

        # Instructions Label (Row 1)
        self.instructions_label = Label(self.game_frame, wrap=300, justify=LEFT, text="Press <Enter> or click the 'Open Boxes' button to reveal the contents of the mystery boxes.", font="Ariel 10", padx=10, pady=10)
        self.instructions_label.grid(row=1)

        # Boxes (Row 2)
        self.box_frame = Frame(self.game_frame)
        self.box_frame.grid(row=2, pady=10)

        photo = PhotoImage(file="question.gif")

        self.prize1_label = Label(self.box_frame, text="?\n", padx=10, pady=10, image=photo)
        self.prize1_label.photo = photo
        self.prize1_label.grid(row=0, column=0)

        self.prize2_label = Label(self.box_frame, text="?\n", padx=10, pady=10, image=photo)
        self.prize2_label.photo = photo
        self.prize2_label.grid(row=0, column=1, padx=10)

        self.prize3_label = Label(self.box_frame, text="?\n", padx=10, pady=10, image=photo)
        self.prize3_label.photo = photo
        self.prize3_label.grid(row=0, column=2)

        # Play button (Row 3)
        self.play_button = Button(self.game_frame, text="Open Boxes", bg="#FFFF33", font="Ariel 15 bold", width=20, padx=10, pady=10, command=self.reveal_boxes)
        # Bind button to <Enter>
        self.play_button.focus()
        self.play_button.bind('<Return>', lambda e: self.reveal_boxes())
        self.play_button.grid(row=3)
        setup_hover_button(self.play_button, "", "#CDCD2C")

        # Balance Label (Row 4)
        start_text = "Game Cost: ${}\n""\n How Much will you win?".format(stakes*5)
        self.balance_label = Label(self.game_frame, font="Ariel 12 bold", fg="grey", text=start_text, wrap=300, justify=LEFT)
        self.balance_label.grid(row=4, pady=10)

        # Help and Game stats button (Row 5)
        self.help_export_frame = Frame(self.game_frame)
        self.help_export_frame.grid(row=5, pady=10)

        self.help_button = Button(self.help_export_frame, text="Help / Rules", font="Ariel 15 bold", bg="#808080", fg="white", command=self.help)
        self.help_button.grid(row=0, column=0, padx=2)
        setup_hover_button(self.help_button, "", "#323232")

        self.stats_button = Button(self.help_export_frame, text="Game Stats", font="Ariel 15 bold", bg="#003366", fg="white", command=lambda: self.to_stats(self.round_stats_list, self.game_stats_list))
        self.stats_button.grid(row=0, column=1, padx=2)
        setup_hover_button(self.stats_button, "", "#001223")

        # Quit Button (Row 6)
        self.quit_button = Button(self.game_frame, text="Quit", fg="white", bg="#660000", font="Ariel 15 bold", width=20, command=self.to_quit, padx=10, pady=10)
        self.quit_button.grid(row=6, pady=10)
        setup_hover_button(self.quit_button, "", "#400000")

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
            stats_prizes.append(prize_list)

        photo1 = prizes[0]
        photo2 = prizes[1]
        photo3 = prizes[2]

        # Display prizes
        self.prize1_label.config(image=photo1)
        self.prize1_label.photo = photo1
        self.prize2_label.config(image=photo2)
        self.prize2_label.photo = photo2
        self.prize3_label.config(image=photo3)
        self.prize3_label.photo = photo3

        # Deduct cost of game
        current_balance -= 5 * stakes_multiplier

        # Add winnings
        current_balance += round_winnings

        # Set balance to adjusted balance
        self.balance.set(current_balance)
        self.game_stats_list[1] = current_balance

        balance_statement = "Game Cost: ${}\nPayback: ${}\nCurrent Balance: ${}".format(5*stakes_multiplier, round_winnings, current_balance)

        # Add round results to stats list
        round_summary = "{} | {} | {} - Cost: ${} | Payback: ${} | Current Balance: ${}".format(stats_prizes[0], stats_prizes[1], stats_prizes[2], stats_prizes[2], 5 * stakes_multiplier, round_winnings, current_balance)
        self.round_stats_list.append(round_summary)
        print(self.round_stats_list)

        # Edit label so user can see their balance
        self.balance_label.configure(text=balance_statement)

        if current_balance < 5 * stakes_multiplier:
            self.play_button.config(state=DISABLED)
            self.game_box.focus()
            self.play_button.config(text="Game Over")

            balance_statement = "Current Balance: ${}\nYour balance is too low. You can only quit or view your stats. Sorry about that.".format(current_balance)
            self.balance_label.config(fg="#660000", font="Ariel 10 bold", text=balance_statement)

    def to_quit(self):
        root.destroy()

    def help(self):
        print("You asked for help")
        get_help = Help(self)

    def to_stats(self, game_history, game_stats):
        GameStats(self, game_history, game_stats)

class Help:
    def __init__(self, partner):

        background = "orange"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()
        
        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # Set up Help heading (Row 0)
        self.how_heading = Label(self.help_frame, text="Help/Instructions", font=("Arial", "14", "bold"), bg=background)
        self.how_heading.grid(row=0)

        # Help text (Label, Row 1)
        self.help_text = Label(self.help_frame, text="I am currently busy, help yourself SMH", justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (Row 2)
        self.dismiss_button = Button(self.help_frame, text="Dismiss", width=10, bg=background, font=("Arial", "10", "bold"), command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, pady=10)
        setup_hover_button(self.dismiss_button, "", "dark orange")

    def close_help(self,partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

class GameStats:
    def __init__(self, partner, game_history, game_stats):
        print(game_history)

        # Disable help button
        partner.stats_button.config(state=DISABLED)
        setup_hover_button(partner.stats_button,"unbind","")

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

        # Dismiss Button (Row 3)
        self.dismiss_button = Button(self.stats_frame, text="Dismiss", width=10, font=("Arial", "10", "bold"), command=partial(self.close_stats, partner))
        self.dismiss_button.grid(row=3, pady=10)
        setup_hover_button(self.dismiss_button, "", "")

    def close_stats(self,partner):
        # Put help button back to normal...
        partner.stats_button.config(state=NORMAL)
        setup_hover_button(partner.stats_button,"","#001D39")
        self.stats_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()
