
def isOdd(n: float):
    # if n % 2:
    #     return True
    # else:
    #     return False
    return n % 2 == 1


def isEven(n: float):
    # if n % 2:
    #     return False
    # else:
    #     return True
    return n % 2 == 0


assert isOdd(42) == False
assert isOdd(9999) == True
assert isOdd(-10) == False
assert isOdd(-11) == True
assert isOdd(3.1415) == False
assert isEven(42) == True
assert isEven(9999) == False
assert isEven(-10) == True
assert isEven(-11) == False
assert isEven(3.1415) == False
