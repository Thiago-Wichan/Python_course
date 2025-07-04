# E X E R C I S E # 1 8 : B U Y 8 G E T 1 F R E E

def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
    total = 0
    restCoffee = numberOfCoffees
    while restCoffee > 0:
        if restCoffee > 8:
            total += pricePerCoffee * 8
            restCoffee -= 9
        else:
            total += pricePerCoffee * restCoffee
            restCoffee -= restCoffee
    return total


assert getCostOfCoffee(7, 2.50) == 17.50
assert getCostOfCoffee(8, 2.50) == 20
assert getCostOfCoffee(9, 2.50) == 20
assert getCostOfCoffee(10, 2.50) == 22.50

for i in range(1, 4):
    assert getCostOfCoffee(0, i) == 0
    assert getCostOfCoffee(8, i) == 8 * i
    assert getCostOfCoffee(9, i) == 8 * i
    assert getCostOfCoffee(18, i) == 16 * i
    assert getCostOfCoffee(19, i) == 17 * i
    assert getCostOfCoffee(30, i) == 27 * i
