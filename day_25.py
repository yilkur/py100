"""

Let's extend Day 24's project and create a health stats generator for a character in a video game.

Create a subroutine that rolls a dice of any size and returns that number.
Then, create a second subroutine that rolls one six-sided dice and one eight-sided dice.
Multiply the number from the six-sided dice and eight-sided dice together and return that subroutine as a character's health stats for a video game.
Print out the character's health stats.
Add a loop to give the user the option to generate health stats for another character.
(We genuinely see this in video games!)

🥳 Extra points if you ask for the character's name and double extra points if you use different colors!

"""

import random


class colors:
    green = '\033[32m'
    red = '\033[31m'
    cyan = '\033[36m'


print(colors.red + '⚔️ Character Stats Generator ⚔️\n')


def rollDice(numOfSides):
    return random.randint(1, numOfSides)


def generateHealthStats():
    statOne = rollDice(6)
    statTwo = rollDice(8)
    healthStat = statOne * statTwo
    return healthStat


haveNewCharacter = 'yes'

while haveNewCharacter == 'yes':
    health = str(generateHealthStats())
    characterName = input('Name your character: ')
    print(colors.cyan + '\nThe mighty ' + characterName)
    print(colors.green + 'Their health is: ' + health + 'hp')
    haveNewCharacter = input('\nWant to create another character? ')

