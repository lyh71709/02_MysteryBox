import random

NUM_TRIALS = 100
winnings = 0

cost = NUM_TRIALS * 5

for item in range(0, NUM_TRIALS):
    prize = ""
    round_winnings = 0

    for thing in range(0, 3):
        prize_num = random.randint(1, 10)
        prize += " "
        if prize_num == 1:
            # 1/10 Chance
            prize += "gold"
            round_winnings += 5
        elif 1 < prize_num <= 3 :
            # 1/5 Chance
            prize += "silver"
            round_winnings += 2
        elif 3 < prize_num <= 7:
            # 2/5 Chance
            prize += "copper"
            round_winnings += 1
        else:
            prize += "lead"

    winnings += round_winnings

print("Paid In: ${}".format(cost))
print("Pay Out: ${}".format(winnings))
