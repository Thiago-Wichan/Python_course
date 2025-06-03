# E X E R C I S E # 4 : A R E A & V O L U M E

def negativeCheck(*numbers):
    for i in numbers:
        if i < 0:
            raise ValueError


def area(length, width):
    negativeCheck(length, width)
    area = length * width
    return area


def perimeter(length, width):
    negativeCheck(length, width)
    perimeter = (length + width) * 2
    return perimeter


def volume(length, width, heigth):
    negativeCheck(length, width, heigth)
    volume = length * width * heigth
    return volume


def surfaceArea(length, width, heigth):
    negativeCheck(length, width, heigth)
    surface = ((length * width)*2) \
        + ((length * heigth)*2) + ((width * heigth)*2)
    return surface


assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400
assert surfaceArea(10, 10, 10) == 600
assert surfaceArea(9999, 0, 9999) == 199960002
assert surfaceArea(5, 8, 10) == 340

print(perimeter(-10, 5))
