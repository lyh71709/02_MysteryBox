import random

NUM_TRIALS = 10
winnings = 0

cost = NUM_TRIALS * 5

for item in range(0, NUM_TRIALS):
    prize = ""
    round_winnings = 0

    for thing in range(0, 3):
        prize_num = random.randint(1, 4)
        prize += " "
        if prize_num == 1:
            prize += "gold"
            round_winnings += 5
        elif prize_num == 2:
            prize += "silver"
            round_winnings += 2
        elif prize_num == 3:
            prize += "copper"
            round_winnings += 1
        else:
            prize += "lead"

    print("You won {} which is worth {}".format(prize, round_winnings))
    winnings += round_winnings

print("Paid In: ${}".format(cost))
print("Pay Out: ${}".format(winnings))
