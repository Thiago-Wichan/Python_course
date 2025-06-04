# E X E R C I S E # 1 2 : S M A L L E S T & B I G G E S T

def getSmallest(numbers: list[float]):
    minimum = [999999999]
    i = 0
    while i < len(numbers):
        if minimum[0] > numbers[i]:
            minimum.pop(0)
            minimum.append(numbers[i])
            i += 1
        else:
            i += 1
    if len(numbers) == 0:
        return None
    else:
        return minimum[0]


def getBiggest(numbers: list[float]):
    maximum = [0]
    i = 0
    while i < len(numbers):
        if maximum[0] < numbers[i]:
            maximum.pop(0)
            maximum.append(numbers[i])
            i += 1
        else:
            i += 1
    if len(numbers) == 0:
        return None
    else:
        return maximum[0]


assert getSmallest([1, 2, 3]) == 1
assert getSmallest([3, 2, 1]) == 1
assert getSmallest([28, 25, 42, 2, 28]) == 2
assert getSmallest([1]) == 1
assert getSmallest([]) == None

assert getBiggest([1, 2, 3]) == 3
assert getBiggest([3, 2, 1]) == 3
assert getBiggest([28, 25, 42, 2, 28]) == 42
assert getBiggest([1]) == 1
assert getBiggest([]) == None
