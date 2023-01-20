"""
Create subroutines that will roll a dice with any number of sides (essentially as big of a number as you like)
Write one subroutine with one parameter that allows us to call a function (such as rollDice).

"""

import random

print("Infinity Dice 🎲")

numberOfSide = int(input("\nHow many sides?: "))


def rollDice(sides):
    shouldRollAgain = "yes"

    while shouldRollAgain == "yes" or shouldRollAgain == "y":
        randomNum = random.randint(1, sides)
        print("You rolled ", randomNum)
        shouldRollAgain = input("\nRoll again? ")


rollDice(numberOfSide)
