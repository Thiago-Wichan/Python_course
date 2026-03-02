# E X E R C I S E # 2 6 : H A N D S H A K E S


def printHandshakes(people: list[str]):
    handshakes: int = 0
    for i in range(len(people)):
        for x in range(i, len(people)):
            if x == i:
                continue
            # print(f'{people[i]} shakes hands with {people[x]}')
            handshakes += 1
    return handshakes


assert printHandshakes(['Alice', 'Bob']) == 1
assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3
assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6
