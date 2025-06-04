# E X E R C I S E # 1 6 : M O D E

import random


def mode(numbers: list[float]):
    if len(numbers) == 0:
        return None
    most_frequent_number = None
    frequency_number = 0
    number = {}
    for i in numbers:
        if i not in number:
            number[i] = 0
        number[i] += 1
        if number[i] > frequency_number:
            most_frequent_number = i
            frequency_number = number[i]
    return most_frequent_number


# assert mode([]) == None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1
random.seed(42)
testData = [1, 2, 3, 4, 4]
for i in range(1000):
    random.shuffle(testData)
assert mode(testData) == 4
