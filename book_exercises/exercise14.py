# E X E R C I S E # 1 4 : A V E R A G E

import random


def average(numbers: list[float]):
    total: float = 0
    if len(numbers) == 0:
        return None
    for number in numbers:
        total += number
    return total / len(numbers)
    # return sum(numbers)/len(numbers)


assert average([1, 2, 3]) == 2
assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
assert average([12, 20, 37]) == 23
assert average([0, 0, 0, 0, 0]) == 0
random.seed(42)
testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]
for i in range(1000):
    random.shuffle(testData)
assert average(testData) == 2
