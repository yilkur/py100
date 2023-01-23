import random
import os
import time


def generateBaseValue():
    diceOne = random.randint(1, 6)
    diceTwo = random.randint(1, 12)
    baseValue = (diceOne * diceTwo) / 2
    return baseValue


def generateCharacter():
    print('⚔️ CHARACTER BUILDER ⚔️')
    print()

    health = generateBaseValue() + 10
    strength = generateBaseValue() + 12
    name = input('Choose your character name: ')
    type = input('Choose a type (e.g. human, imp, wizard): ')

    print()
    print('Them almighty ' + name)
    print('TYPE: ' + type)
    print('HEALTH: ' + str(health))
    print('STRENGTH: ' + str(strength))
    time.sleep(2)
    print()
    print('May your name go down in Legend...')


haveAnotherCarachter = 'yes'

while haveAnotherCarachter == 'yes' or haveAnotherCarachter == 'y':
    os.system('clear')
    generateCharacter()
    print()
    haveAnotherCarachter = input('Want to create another character?: ')
