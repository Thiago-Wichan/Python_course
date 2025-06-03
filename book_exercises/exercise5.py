# E X E R C I S E # 5 : F I Z Z B U Z Z

def fizzBuzz(upTo: int):
    numbers = range(1, (upTo+1))
    # print_list: list[str | int] = []
    for i in numbers:
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz', end=' ')
            continue
        elif i % 3 == 0:
            print('Fizz', end=' ')
            continue
        elif i % 5 == 0:
            print('Buzz', end=' ')
            continue
        else:
            print(f'{i}', end=' ')
            continue


fizzBuzz(35)
