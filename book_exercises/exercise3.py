# E X E R C I S E # 3 : O D D & E V E N

# My solution and teachers one

def isOdd(number: int):
    # division_ = (number % 2)
    # if division_ == 0:
    #     return False
    # elif division_ == 1:
    #     return True
    # else:
    #     return False
    return number % 2 == 1


def isEven(number: int):
    # division_ = (number % 2)
    # if division_ == 0:
    #     return True
    # elif division_ == 1:
    #     return False
    # else:
    #     return False
    return number % 2 == 0


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
