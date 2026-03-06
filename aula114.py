# função que multiplica e outra que indica se número é ímpar ou par

# def multiplication(*args):
#     total = 1
#     for n in args:
#         total *= n
#     return total


# def evenOrOdd(number):
#     if number % 2 == 0:
#         return f'{number} is Even'
#     return f'{number} is Odd'


# print(multiplication(7, 10, 5))
# print(evenOrOdd(10))


def multiplier(number):
    def multiplied_number(multi_number):
        result = number * multi_number
        return f'Your result is {result}'
    return multiplied_number


duplicator = multiplier(2)
triplicator = multiplier(3)
quadrupler = multiplier(4)

print(duplicator(7))
print(triplicator(7))
print(quadrupler(7))
