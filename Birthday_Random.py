# From the course "First steps in computing and python"
# 3.4.12 lesson 3 - loops
# random number which are raffle till the right birthday date

import random

def count_rolls_until_6():
    res = random.choice([1, 2, 3, 4, 5, 6])
    # print(res)
    count_rolls = 1
    while res != 6:
        res = random.choice([1, 2, 3, 4, 5, 6])
        # print(res)
        count_rolls = count_rolls + 1

    return count_rolls


days = [i for i in range(1, 32)]
months = [i for i in range(1, 13)]


def birthday(day, month):
    # Write your solution here
    bdd = random.choice(days)
    bdm = random.choice(months)
    print(bdd)
    print(bdm)

    count_try = 0

    while bdd != day or bdm != month:
        bdd = random.choice(days)
        bdm = random.choice(months)
        print(bdd)
        print(bdm)

        count_try += 1

    return count_try

day = 1
month = 1
print("It took", birthday(day, month), "trials to draw this birthday:", day, ".", month)