# E X E R C I S E # 1 7 : D I C E R O L L
import random


def rollDice(numberOfDice: int):
    dice = random.randint(1, 6)
    total = 0
    # i = 0
    # while i < numberOfDice:
    #     sum_dice += dice
    #     i += 1
    for i in range(numberOfDice):
        total += dice
    return total


assert rollDice(0) == 0
assert rollDice(1000) != rollDice(1000)
for i in range(1000):
    assert 1 <= rollDice(1) <= 6
    assert 2 <= rollDice(2) <= 12
    assert 3 <= rollDice(3) <= 18
    assert 100 <= rollDice(100) <= 600
