# E X E R C I S E # 2 9 : P Y R A M I D D R A W I N G

def drawPyramid(height):
    i = 0
    x = 1
    while i < height:
        print((' '*(height-i))+('#' * x))
        x += 2
        i += 1


drawPyramid(10)
