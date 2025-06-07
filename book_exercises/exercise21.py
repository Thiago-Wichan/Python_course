# E X E R C I S E # 2 1 : V A L I D A T E D A T E
import datetime
from exercise20 import isLeapYear
thirty = [9, 4, 6, 11]
thirty_one = [1, 3, 5, 7, 8, 10, 12]


def isValidDate(year, month, day):
    if isLeapYear(year):
        if month in range(1, 13):
            if month == 2 and day in range(1, 30):
                return True
            elif month in thirty and day in range(1, 31):
                return True
            elif month in thirty_one and day in range(1, 32):
                return True
            else:
                return False
        else:
            return False
    else:
        if month in range(1, 13):
            if month == 2 and day in range(1, 29):
                return True
            elif month in thirty and day in range(1, 31):
                return True
            elif month in thirty_one and day in range(1, 32):
                return True
            else:
                return False
        else:
            return False


assert isValidDate(1999, 12, 31) == True
assert isValidDate(2000, 2, 29) == True
assert isValidDate(2001, 2, 29) == False
assert isValidDate(2029, 13, 1) == False
assert isValidDate(1000000, 1, 1) == True
assert isValidDate(2015, 4, 31) == False
assert isValidDate(1970, 5, 99) == False
assert isValidDate(1981, 0, 3) == False
assert isValidDate(1666, 4, 0) == False

d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days=1)
for i in range(1000000):
    assert isValidDate(d.year, d.month, d.day) == True
    d += oneDay
