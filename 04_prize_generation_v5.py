import random

NUM_TRIALS = 100
winnings = 0

cost = NUM_TRIALS * 5

for item in range(0, NUM_TRIALS):
    #prize = ""
    round_winnings = 0

    for thing in range(0, 3):
        prize_num = random.randint(1, 100)
        #prize += " "
        if 0 < prize_num <= 5:
            # 1/20 Chance
            round_winnings += 5
        elif 5 < prize_num <= 25 :
            # 1/5 Chance
            round_winnings += 2
        elif 25 < prize_num <= 65:
            # 2/5
            round_winnings += 1
        #else:
            #prize += "lead"

    winnings += round_winnings

print("Paid In: ${}".format(cost))
print("Pay Out: ${}".format(winnings))
