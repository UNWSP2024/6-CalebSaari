import math
import random


def randDice():
    roll_1 = random.randint(1,6)
    roll_2 = random.randint(1,6)
    return roll_1 + roll_2

def main():
    Dice_Total = 0
    Total = 0
    for x in range(100):
        Dice_Total = randDice()
        Total += Dice_Total
    avg = Total/100
    print("The average roll combination was",avg)

main()

# Caleb Saari 2/27/25 Wk6 Program 1: Random Dice