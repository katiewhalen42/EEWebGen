//Utility functions for EEWebGen
import random

def rollDice(numDice, typeDice):
    result=0
    for x in range(numDice):
        result += random.randint(1, typeDice)
    return result

def getRandDice():
    return random.choice([4, 6, 8, 10, 12, 20, 100])

def getRandDiceFace(type):
    if type != 100:
        return random.randint(1, type)
    else:
        return random.randrange(10, 100, 10)
