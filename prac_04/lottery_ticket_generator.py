"""
Prompts the user for how many "quick picks"
then generates that many lines of random numbers
"""

from random import randint


amount_of_picks = int(input("How many quick picks? "))

for i in range(amount_of_picks):
    lottery_numbers = []
    number = randint(1, 45)
    for j in range(6):
        while number in lottery_numbers:
            number = randint(1, 45)
        lottery_numbers.append(number)
        lottery_numbers.sort()
    print(lottery_numbers)
