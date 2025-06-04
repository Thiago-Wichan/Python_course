# E X E R C I S E # 1 3 : S U M & P R O D U C T

def calculateSum(numbers: list[float]):
    result: float = 0
    for number in numbers:
        result += number
    return result


def calculateProduct(numbers: list[float]):
    product: float = 1
    for number in numbers:
        product *= number
    return product


assert calculateSum([]) == 0
assert calculateSum([2, 4, 6, 8, 10]) == 30
assert calculateProduct([]) == 1
assert calculateProduct([2, 4, 6, 8, 10]) == 3840

numbers_list: list[float] = []
for i in range(1, 100):
    numbers_list.append(i)


print(calculateProduct(numbers_list))
